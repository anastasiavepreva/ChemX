import openai
import base64
import pandas as pd
from tqdm import tqdm
import argparse, os, json

def parameter():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dataset', type=str, choices=['oxazolidinone', 'benzimidazole', 'cocrystals', 'complexes', 'nanozymes', 'magnetic', 'cytotoxicity', 'seltox', 'synergy'])
    parser.add_argument('--openai_api_key', type=str)
    return parser.parse_args()

def get_querry(dataset):
    df_promt = pd.read_csv('data/prompts.csv')
    description = df_promt['description'][df_promt['dataset'] == dataset].item()
    instructions = df_promt['instructions'][df_promt['dataset'] == dataset].item()
    system_prompt = description + instructions
    instruction_prompt = df_promt['prompt'][df_promt['dataset'] == dataset].item()
    return system_prompt, instruction_prompt

def get_querry_by_condition(dataset, condition):
    df_promt = pd.read_csv('data/prompts.csv')
    description = df_promt['description'][(df_promt['dataset'] == dataset) & (df_promt['condition'] == condition)].item()
    instructions = df_promt['instructions'][(df_promt['dataset'] == dataset) & (df_promt['condition'] == condition)].item()
    system_prompt = description + instructions
    instruction_prompt = df_promt['prompt'][(df_promt['dataset'] == dataset) & (df_promt['condition'] == condition)].item()
    return system_prompt, instruction_prompt

def main():
    
    args = vars(parameter())
    dataset = args['dataset']
    openai.api_key = args['openai_api_key']
    
    images_folder = os.path.normpath(f'data/images/{dataset}')
    
    # prepare prompts
    df_dataset = pd.read_csv(f'data/datasets/{dataset}.csv')
    if dataset != 'complexes':
        system_prompt, instruction_prompt = get_querry(dataset)        
    
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
            system_prompt, instruction_prompt = get_querry_by_condition(dataset, df_dataset['metal'][df_dataset['pdf'] == folder.split('\\')[-1]].iloc[0])
        
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

    if not os.path.exists(f'result/from_image/{dataset}'):
        os.makedirs(f'result/from_image/{dataset}')
    df.to_csv(f'result/from_image/{dataset}/gpt_4o_results.csv', sep='\t', index=False)
    
if __name__ == "__main__":
    main()