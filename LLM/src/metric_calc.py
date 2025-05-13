import json
import sys
import pandas as pd
import argparse
import numpy as np
from rdkit import Chem

from rdkit import RDLogger 
RDLogger.DisableLog('rdApp.*')

EXTRACTED_COLUMNS = {
    'oxazolidinone': ['compound_id', 'smiles', 'target_type', 'target_relation', 'target_value', 'target_units', 'bacteria'],
    'benzimidazole': ['compound_id', 'smiles', 'target_type', 'target_relation', 'target_value', 'target_units', 'bacteria'],
    'cocrystals': ['name_cocrystal', 'ratio_cocrystal', 'name_drug', 'SMILES_drug', 'name_coformer', 'SMILES_coformer', 'photostability_change'],
    'complexes': ['compound_id', 'compound_name', 'SMILES', 'SMILES_type', 'target'],
    'nanozymes': ['formula', 'activity', 'syngony', 'length', 'width', 'depth', 'surface', 'km_value', 'km_unit', 'vmax_value', 'vmax_unit', 'reaction_type', 'c_min', 'c_max', 'c_const', 'c_const_unit', 'ccat_value', 'ccat_unit', 'ph', 'temperature'],
    'magnetic': ["name", "np_core", "np_shell", "core_shell_formula", "np_shell_2", "np_hydro_size", "xrd_scherrer_size", "emic_size", "space_group_core", "space_group_shell", "squid_sat_mag", "squid_rem_mag", "exchange_bias_shift_Oe", "vertical_loop_shift_M_vsl_emu_g", "hc_kOe", "squid_h_max", "zfc_h_meas", "instrument", "fc_field_T", "squid_temperature", "coercivity", "htherm_sar", "mri_r1", "mri_r2"],
    'cytotoxicity': ["material", "shape", "coat_functional_group", "synthesis_method", "surface_charge", "core_nm", "size_in_medium_nm", "hydrodynamic_nm", "potential_mv", "zeta_in_medium_mv", "no_of_cells_cells_well", "human_animal", "cell_source", "cell_tissue", "cell_morphology", "cell_age", "time_hr", "concentration", "test", "test_indicator", "viability_%"],
    'seltox': ["np", "coating", "bacteria", "mdr", "strain", "np_synthesis", "method", "mic_np_µg_ml", "concentration", "zoi_np_mm", "np_size_min_nm", "np_size_max_nm", "np_size_avg_nm", "shape", "time_set_hours", "zeta_potential_mV", "solvent_for_extract", "temperature_for_extract_C", "duration_preparing_extract_min", "precursor_of_np", "concentration_of_precursor_mM", "hydrodynamic_diameter_nm", "ph_during_synthesis"],
    'synergy': ["NP", "bacteria", "strain", "NP_synthesis", "drug", "drug_dose_µg_disk", "NP_concentration_µg_ml", "NP_size_min_nm", "NP_size_max_nm", "NP_size_avg_nm", "shape", "method", "ZOI_drug_mm_or_MIC _µg_ml", "error_ZOI_drug_mm_or_MIC_µg_ml", "ZOI_NP_mm_or_MIC_np_µg_ml", "error_ZOI_NP_mm_or_MIC_np_µg_ml", "ZOI_drug_NP_mm_or_MIC_drug_NP_µg_ml", "error_ZOI_drug_NP_mm_or_MIC_drug_NP_µg_ml", "fold_increase_in_antibacterial_activity", "zeta_potential_mV", "MDR", "FIC", "effect", "time_hr", "coating_with_antimicrobial_peptide_polymers", "combined_MIC", "peptide_MIC", "viability_%",  "viability_error"]
}

NUMERIC_COLUMNS = {
    'oxazolidinone': ['target_value'],
    'benzimidazole': ['target_value'],
    'cocrystals': [],
    'complexes': ['target'],
    'nanozymes': ['length', 'width', 'depth', 'km_value', 'vmax_value', 'c_min', 'c_max', 'c_const', 'ccat_value', 'ph', 'temperature'],
    'magnetic': ["np_hydro_size", "xrd_scherrer_size", "emic_size", "squid_sat_mag", "squid_rem_mag", "exchange_bias_shift_Oe", "vertical_loop_shift_M_vsl_emu_g", "hc_kOe", "squid_h_max", "zfc_h_meas", "fc_field_T", "squid_temperature", "coercivity", "htherm_sar", "mri_r1", "mri_r2"],
    'cytotoxicity': ["core_nm", "size_in_medium_nm", "hydrodynamic_nm", "potential_mv", "zeta_in_medium_mv", "no_of_cells_cells_well", "time_hr", "concentration", "viability_%"],
    'seltox': ["mdr", "mic_np_µg_ml", "concentration", "zoi_np_mm", "np_size_min_nm", "np_size_max_nm", "np_size_avg_nm", "time_set_hours", "zeta_potential_mV", "temperature_for_extract_C", "duration_preparing_extract_min", "concentration_of_precursor_mM", "hydrodynamic_diameter_nm", "ph_during_synthesis"],
    'synergy': ["drug_dose_µg_disk", "NP_concentration_µg_ml", "NP_size_min_nm", "NP_size_max_nm", "NP_size_avg_nm", "ZOI_drug_mm_or_MIC _µg_ml", "error_ZOI_drug_mm_or_MIC_µg_ml", "ZOI_NP_mm_or_MIC_np_µg_ml", "error_ZOI_NP_mm_or_MIC_np_µg_ml", "ZOI_drug_NP_mm_or_MIC_drug_NP_µg_ml", "error_ZOI_drug_NP_mm_or_MIC_drug_NP_µg_ml", "fold_increase_in_antibacterial_activity", "zeta_potential_mV", "FIC", "time_hr", "combined_MIC", "peptide_MIC", "viability_%",  "viability_error"]    
}

SMILES_COLS = {
    'oxazolidinone': ['smiles'],
    'benzimidazole': ['smiles'],
    'cocrystals': ['SMILES_drug', 'SMILES_coformer'],
    'complexes': ['SMILES'],   
    'nanozymes': [],
    'magnetic': [],
    'cytotoxicity': [],
    'seltox': [],
    'synergy': []
}

def convert_comma(x):
    """Converts commas to periods in a string, if possible."""
    try:
        return str(x.replace(',', '.'))
    except:
        return str(x)
    
def select_open_access(df_dataset):
    """Filters and returns the rows with open access (access == 1) articles in the dataset."""
    return df_dataset.loc[df_dataset['access'] == 1]

def prepare_dataset(dataset, n_cols, s_cols):
    """Prepares the dataset by cleaning, converting columns, and processing open-access rows."""
    df_dataset = pd.read_csv(f'data/datasets/{dataset}.csv')
    
    for col in n_cols:
        df_dataset[col] = df_dataset[col].apply(lambda x: convert_comma(x))
    
    if dataset in ['oxazolidinone', 'benzimidazole']:
        df_dataset.target_relation = df_dataset.target_relation.apply(lambda x: '=' if x == "'='" else x)

    df_dataset = df_dataset.fillna('NOT_DETECTED')
    
    if dataset in ['oxazolidinone', 'benzimidazole', 'cocrystals', 'complexes']:
        for col in s_cols:
            df_dataset[col] = df_dataset[col].apply(lambda x: Chem.MolToSmiles(Chem.MolFromSmiles(x)) if Chem.MolFromSmiles(x) != None else x)

    return select_open_access(df_dataset)

def prepare_result(dataset, source, cols, s_cols):
    """Processes the results from PDF, image, or single-agent source, and formats them into a DataFrame."""
    if source == 'pdf':
        df_output = pd.read_csv(f'result/from_pdf/{dataset}_result.csv')
    elif source == 'image':
        df_output = pd.read_csv(f'result/from_image/{dataset}_result.csv', sep='\t')
    elif source == 'single_agent':
        df_result = pd.read_csv(f'result/from_single_agent/{dataset}/pred.csv')
        if dataset in ['cytotoxicity', 'seltox', 'synergy', 'magnetic']:
            df_result['pdf'] = df_result['pdf'].apply(lambda x: x + '.pdf')
        return df_result.drop_duplicates()

    processed_rows = []
    for pdf in df_output['pdf']:
        result_json = json.loads(df_output['output'][df_output['pdf'] == pdf].item())
        for sample in result_json['samples']:
            row = {k: v for k, v in zip(cols, [sample.get(col) for col in cols])}
            if dataset in ['cytotoxicity', 'seltox', 'synergy', 'magnetic']:
                row['pdf'] = pdf + '.pdf'
            else:
                row['pdf'] = pdf
            processed_rows.append(row)
    df_result = pd.DataFrame(processed_rows)

    if dataset in ['oxazolidinone', 'benzimidazole', 'cocrystals', 'complexes']:
        for col in s_cols:
            df_result[col] = df_result[col].apply(lambda x: Chem.MolToSmiles(Chem.MolFromSmiles(x)) if Chem.MolFromSmiles(x) != None else x)
        
    if source == 'pdf':
        df_result['pdf'] = df_result['pdf'].apply(lambda x: x[:-4])
    elif source == 'image':
        df_result['pdf'] = df_result['pdf'].apply(lambda x: x.split("\\")[-1])

    return df_result.drop_duplicates()

def empty_metrics(cols):
    """Creates an empty DataFrame to store metrics (tp, fp, fn, precision, recall, f1) for specified columns."""
    metrics = dict()
    for col in cols:
        metrics[col] = {"tp": 0, "fp": 0, "fn": 0, "precision": 0, "recall": 0, "f1": 0}
    return pd.DataFrame(metrics).T

def calc_metrics(
    df_true: pd.DataFrame,
    df_pred: pd.DataFrame) -> pd.DataFrame:

    """Calculates precision, recall, F1 score, and confusion matrix metrics for each column in the true and predicted DataFrames."""

    metrics = {}
    from copy import deepcopy
    for col in df_true.columns:
        true_values = list(df_true[col].astype(str).values)
        pred_values = list(df_pred[col].astype(str).values)

        tv = deepcopy(true_values)
        pv = deepcopy(pred_values)

        tp = 0

        for val in tv:
            if val in pv:
                pv.pop(pv.index(val))
                tp += 1

        fp = 0

        tv = deepcopy(true_values)
        pv = deepcopy(pred_values)

        for val in pv:
            if val in tv:
                tv.pop(tv.index(val))
            else:
                fp += 1

        fn = 0

        tv = deepcopy(true_values)
        pv = deepcopy(pred_values)

        for val in tv:
            if val in pv:
                pv.pop(pv.index(val))
            else:
                fn += 1

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

        metrics[col] = {
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "precision": precision,
            "recall": recall,
            "f1": f1
        }

    return pd.DataFrame(metrics).T

def get_parameters():
    """Parses and returns command-line arguments for dataset selection and extraction approach identification."""
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dataset', type=str, choices=['oxazolidinone', 'benzimidazole', 'cocrystals', 'complexes', 'nanozymes', 'magnetic', 'cytotoxicity', 'seltox', 'synergy'])
    parser.add_argument('--source', type=str, choices=['image', 'pdf', 'single_agent'])
    return parser.parse_args()

def main():
    """
    Analyzes the performance of predictions by calculating evaluation metrics (precision, recall, F1 score) for a specified dataset.

    This function:
        - Loads command-line arguments to get the dataset name and data source.
        - Prepares the dataset by cleaning and processing columns based on the dataset type.
        - Prepares the results from a specified source (PDF, image, or single agent).
        - Calculates metrics (precision, recall, F1 score) for each article by comparing the dataset values and results.
        - Aggregates the metrics and averages them across all articles in the dataset.
        - Saves the resulting metrics to a CSV file for further analysis.
    """
    args = vars(get_parameters())
    dataset = args['dataset']
    source = args['source']
    cols = EXTRACTED_COLUMNS[dataset]
    n_cols = NUMERIC_COLUMNS[dataset]
    s_cols = SMILES_COLS[dataset]
    
    df_dataset = prepare_dataset(dataset, n_cols, s_cols)
    df_result = prepare_result(dataset, source, cols, s_cols)
    df_dataset['pdf'] = df_dataset['pdf'].apply(lambda x: x.lower())
    df_result['pdf'] = df_result['pdf'].apply(lambda x: x.lower())

    df_metrics = empty_metrics(cols)
    access_articles = df_dataset['pdf'].unique()

    if dataset in ['magnetic', 'seltox']:
        access_articles = set(np.load(f'src/{dataset}_articles.npy'))

    print(f'Analyze {len(access_articles)} articles...')

    for article in access_articles:
        df_dataset_doi = df_dataset.loc[df_dataset['pdf'] == article][cols]
        df_result_doi = df_result.loc[df_result['pdf'] == article][cols]
        df_metrics_doi = calc_metrics(df_dataset_doi, df_result_doi)
        df_metrics += df_metrics_doi

    df_metrics = df_metrics / len(access_articles)
    print(df_metrics)
    
    path_to_save = f'result/metrics/metrics_{dataset}_from_{source}.csv'
    df_metrics.to_csv(path_to_save)
    
    print(f'Saved to {path_to_save}!')
        
if __name__ == "__main__":
    main()