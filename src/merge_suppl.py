from pypdf import PdfWriter
import argparse, os
from tqdm import tqdm

def parameter():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dataset', type=str, choices=['oxazolidinone', 'benzimidazole', 'cocrystals', 'complexes', 'nanozymes', 'magnetic', 'cytotoxicity', 'seltox', 'synergy'])
    return parser.parse_args()

def main():
    args = vars(parameter())
    dataset = args['dataset']
    
    path_to_pdfs = f'data/pdfs/pdf_{dataset}/'
    
    # create new path for merged pdfs
    path_to_merged_pdfs = f'data/pdfs/pdf_{dataset}_merged/'
    if not os.path.exists(path_to_merged_pdfs):
        os.makedirs(path_to_merged_pdfs)
    
    for filename in tqdm(os.listdir(path_to_pdfs)):
        # if file is supplementary information, merge it with the article
        if filename.endswith('_si.pdf') or filename.endswith('_SI.pdf'):
            article_filename = filename.replace('_si', '').replace('_SI', '')
            suppl_filename = filename
            try:    
                input1 = open(path_to_pdfs + article_filename, "rb")
                input2 = open(path_to_pdfs + suppl_filename, "rb")
                merger = PdfWriter()
                merger.append(input1)
                merger.append(input2)
                output = open(path_to_merged_pdfs + article_filename, "wb")
                merger.write(output)
                merger.close()
                output.close()
            except:
                print(f'Cannot process {filename}')
        else:
            continue
        
if __name__ == "__main__":
    main()