# Synergy – Toxicity of Drug, Nanoparticle, and Their Synergistic Effect on Bacterial Strains

---

## Original Data

**Title:** Synergy dataset – Toxicity of drug, nanoparticle, and their synergistic effect on bacterial strains  
**Description:** The dataset contains experimental data on the antibacterial activity of individual drugs, nanoparticles (NPs), and their combinations against various bacterial strains. It includes measurements of inhibition zones, MIC values, viability, and calculated synergy metrics (e.g., FIC, fold increase).  
**Total number of records:** 3226  
**Number of features (columns):** 34  
**Data type:** Mixed  
**Application:** Nanomaterials  
**Automatic validation:** Yes  

A complete data table can be found in the internal dataset file: `synergy_NeurIPS_updated_data`

---

## Data Scheme

### Synergy Dataset – Column Descriptions

| **Column Name**                                | **Description**                                                                 |
|------------------------------------------------|---------------------------------------------------------------------------------|
| sn                                             | Internal index of the record                                                   |
| NP                                             | Nanoparticle name (Ag, Au, CuO, etc.)                                          |
| bacteria                                       | Bacteria species                                                               |
| strain                                         | Strain identifier (e.g., ATCC 25922, MTCC 443)                                 |
| NP_synthesis                                   | Method of nanoparticle synthesis (e.g., green, chemical)                       |
| drug                                           | Name of the antibiotic tested                                                  |
| drug_dose_µg_disk                              | Dose of drug in disc diffusion assay                                           |
| NP_concentration_µg_ml                         | NP concentration in µg/mL                                                      |
| NP_size_min_nm                                 | Minimum NP size in nanometers                                                  |
| NP_size_max_nm                                 | Maximum NP size in nanometers                                                  |
| NP_size_avg_nm                                 | Average NP size in nanometers                                                  |
| shape                                          | Morphology of the NP                                                           |
| method                                         | Assay method used                                                              |
| ZOI_drug_mm_or_MIC _µg_ml                      | Zone of inhibition or MIC for drug alone                                       |
| error_ZOI_drug_mm_or_MIC_µg_ml                 | Standard deviation for `ZOI_drug_mm_or_MIC`                                    |
| ZOI_NP_mm_or_MIC_np_µg_ml                      | ZOI or MIC for NP alone                                                        |
| error_ZOI_NP_mm_or_MIC_np_µg_ml                | Standard deviation for NP assay                                                |
| ZOI_drug_NP_mm_or_MIC_drug_NP_µg_ml            | ZOI or MIC for drug + NP                                                       |
| error_ZOI_drug_NP_mm_or_MIC_drug_NP_µg_ml      | Standard deviation for combination                                              |
| fold_increase_in_antibacterial_activity        | Fold increase in combination efficiency                                        |
| zeta_potential_mV                              | Surface charge in mV                                                           |
| MDR                                            | Indicates multidrug resistance (R = resistant)                                 |
| FIC                                            | Fractional Inhibitory Concentration index                                      |
| effect                                         | Type of synergy (synergistic, additive…)                                       |
| reference                                      | Full citation or source                                                        |
| doi                                            | Digital Object Identifier                                                      |
| article_list                                   | Internal article identifier                                                    |
| time_hr                                        | Time of exposure in hours                                                      |
| coating_with_antimicrobial_peptide_polymers    | Presence or name of coating                                                    |
| combined_MIC                                   | MIC value of the full system (NP + coating)                                    |
| peptide_MIC                                    | MIC value of peptide alone                                                     |
| viability_%                                    | Viability of bacterial sample                                                  |
| viability_error                                | Associated error for viability                                                 |
| journal_name                                   | Name of source journal                                                         |
| publisher                                      | Publisher                                                                       |
| year                                           | Year of publication                                                            |
| title                                          | Title of the article                                                           |
| journal_is_oa                                  | Whether the journal is Open Access                                             |
| is_oa                                          | Whether the article is OA                                                      |
| oa_status                                      | OA level (green, hybrid)                                                       |
| pdf                                            | PDF filename in archive                                                        |
| access                                         | 1 = OA, 0 = closed                                                             |
---

## Metadata

| **Column Name**      | **Description**                                      |
|----------------------|------------------------------------------------------|
| journal_name         | Journal name                                         |
| publisher            | Publisher                                            |
| year                 | Year of publication                                  |
| title                | Article title                                        |
| journal_is_oa        | Whether the journal is Open Access                   |
| is_oa                | Whether the article is Open Access                   |
| oa_status            | Type of OA (green, hybrid, closed)                  |
| pdf                  | PDF filename                                         |
| access               | 1 = OA, 0 = closed                                    |

!!! note "Key Notes"
    - **Units**: Embedded directly in column names (e.g., nm, mV, mm)  
    - **Missing values**: Represented as blank cells (e.g., for Drug, peptide_MIC, etc.)  
    - **Synergy metrics**: `FIC` and `fold_increase_in_antibacterial_activity` quantify interaction strength between drug and NP  
    - **MDR**: Indicates resistance status (R = Resistant)  
    - **Coating**: Captures presence of peptide/polymer coatings with antimicrobial properties  

---

## Text Description

The **Synergy dataset** contains experimental data focused on evaluating the combined antibacterial effects of inorganic nanoparticles and conventional antibiotics. It includes tests performed on multiple bacterial strains, including standard and multidrug-resistant (MDR) variants.

The dataset captures:

- Physicochemical properties of nanoparticles (size, shape, zeta potential, synthesis method)  
- Drug-specific details (name, dose, MIC, effect)  
- Antibacterial activity metrics:  
  - Drug alone  
  - Nanoparticle alone  
  - Drug + NP combination  
- Synergy indicators (FIC, fold increase)  
- Bacterial viability after treatment  
- Metadata including publication source, year, and access status

This dataset is intended to support research in **nanomedicine** and **antimicrobial resistance**, particularly in the design and evaluation of **nanoparticle-drug combinations** with synergistic effects.

---

## Validation Results

Validation was performed manually using the original PDF articles located in the folder: `synergy_article_list`.

Each dataset entry was cross-checked for:

- Consistency with original source data  
- Accuracy of numerical values and units (e.g., MIC, ZOI)  
- Correctness of metadata (journal, DOI, title)

Validation results are contained in: `Validation_synergy_NeurIPS_updated_data`

Key fields in the validation file include:

- `verification required`  
- `verified_by`  
- `verification_date`  
- `has_mistake_in_data`  
- `has_mistake_in_metadata`  
- `entry_status`

---
