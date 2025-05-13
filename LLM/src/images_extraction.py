import openai
import base64
import pandas as pd
from tqdm import tqdm
import argparse, os, json

from constants import datasets

def get_parameters():
    """Parses and returns command-line arguments for dataset selection and OpenAI API key."""
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dataset', type=str, choices=datasets, required=True)
    parser.add_argument('--openai_api_key', type=str, required=True)
    return parser.parse_args()

def get_query(dataset):
    """Retrieves prompt components for a specified dataset."""
    df_promt = pd.read_csv('data/prompts.csv')
    description = df_promt['description'][df_promt['dataset'] == dataset].item()
    instructions = df_promt['instructions'][df_promt['dataset'] == dataset].item()
    system_prompt = description + instructions
    instruction_prompt = df_promt['prompt'][df_promt['dataset'] == dataset].item()
    return system_prompt, instruction_prompt

def get_query_by_condition(dataset, condition):
    """Retrieves prompt components for a specified dataset by condition (for 'complexes' dataset)."""
    df_promt = pd.read_csv('data/prompts.csv')
    description = df_promt['description'][(df_promt['dataset'] == dataset) & (df_promt['condition'] == condition)].item()
    instructions = df_promt['instructions'][(df_promt['dataset'] == dataset) & (df_promt['condition'] == condition)].item()
    system_prompt = description + instructions
    instruction_prompt = df_promt['prompt'][(df_promt['dataset'] == dataset) & (df_promt['condition'] == condition)].item()
    return system_prompt, instruction_prompt

def main():
    """
    Main entry point for information extraction from images using OpenAI's GPT-4o model.

    This function:
        - Parses command-line arguments to retrieve the dataset name and OpenAI API key.
        - Loads images from the specified dataset folder.
        - Constructs prompts based on dataset-specific information.
        - Encodes image files as base64 and embeds them in the model's input message.
        - Sends the constructed prompt and image data to the GPT-4o model using OpenAI's API,
          expecting structured JSON responses.
        - Aggregates the model responses into a DataFrame and exports the results to a TSV file.
    """
    args = vars(get_parameters())
    dataset = args['dataset']
    openai.api_key = args['openai_api_key']
    
    images_folder = os.path.normpath(f'data/images/{dataset}')
    
    # prepare prompts
    df_dataset = pd.read_csv(f'data/datasets/{dataset}.csv')
    if dataset != 'complexes':
        system_prompt, instruction_prompt = get_query(dataset)        
    
    # load expected output json structure
    with open(f'data/json/{dataset}.json', 'r') as file:
        structure_json = json.load(file)
    
    df = pd.DataFrame()

    pdf = []
    prompt = []
    output = []
    
    folders = [folder.path for folder in os.scandir(images_folder) if folder.is_dir()]
    
    for folder in tqdm(folders):
        
        if dataset == 'complexes':
            system_prompt, instruction_prompt = get_query_by_condition(dataset, df_dataset['metal'][df_dataset['pdf'] == folder.split('\\')[-1]].iloc[0])
        
        # go into folder and get all image paths
        image_paths = [os.path.join(folder, filename)
        for filename in os.listdir(folder)
        if filename.lower().endswith('.jpg')
        ]

        # add images to message content
        message_content = [{"type": "text", "text": instruction_prompt}]
        for path in image_paths:
            with open(path, "rb") as image_file:
                base64_image = base64.b64encode(image_file.read()).decode("utf-8")

                mime_type = "image/jpg"

                message_content.append({
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{mime_type};base64,{base64_image}"
                    }
                })
                
        # get model response
        response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": message_content
            }
        ],
        max_tokens=10000,
        response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": f"{dataset}",
                        "schema": structure_json,
                        "strict": True,
                        },
                    }
        )
        
        # add results to a table
        pdf.append(folder)
        prompt.append(instruction_prompt)
        output.append(response.choices[0].message.content)

    # save results
    df['pdf'] = pdf
    df['prompt'] = system_prompt + instruction_prompt
    df['output'] = output

    df.to_csv(f'result/from_image/{dataset}_result.csv', sep='\t', index=False)
    
if __name__ == "__main__":
    main()