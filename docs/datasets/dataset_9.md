# Improved Photostability due to Multi-Component Crystals Formation

---

## Original Data

**Title:** Improved Photostability due to Multi-Component Crystals Formation  
**Description:**  
The dataset contains information on photostable drug molecules and their multi-component crystalline forms (cocrystals or salts). For each entry, data is extracted on the drug, coformer, their molecular structures in SMILES format, the ratio in the crystal, and the change in photostability relative to the original drug.

**Total number of records:** 70  
**Number of features (columns):** 37
**Data type:** Mixed  
**Application:** Small molecules  
**Automatic validation:** Yes

---

## Data Scheme
### Dataset – Column Descriptions

| **Column Name**                     | **Description**                                                                 |
|------------------------------------|---------------------------------------------------------------------------------|
| name_cocrystal                     | Name of the multi-component crystal                                            |
| name_cocrystal_type_file           | Source type (text, manuscript, figure, etc.)                                   |
| name_cocrystal_origin              | Origin in article (figure 1, table 2, etc.)                                    |
| name_cocrystal_page                | Page number where cocrystal is mentioned                                       |
| ratio_cocrystal                    | Component ratio used to form the cocrystal                                     |
| ratio_cocrystal_page              | Page number for reported ratio                                                 |
| ratio_cocrystal_origin            | Source of ratio (e.g., text, table)                                            |
| name_drug                          | Drug name as reported in the article                                           |
| SMILES_drug                        | Canonical SMILES of the drug molecule                                          |
| name_coformer                      | Name of the coformer                                                           |
| SMILES_coformer                    | Canonical SMILES of the coformer molecule                                      |
| photostability_change              | Change in photostability ("increase", "does not change", "decrease")           |
| photostability_change_origin       | Origin (e.g., figure, table, text)                                             |
| photostability_change_page         | Page number where photostability is reported                                   |
| doi                                | Digital Object Identifier                                                      |
| title                              | Title of the publication                                                       |
| journal                            | Name of the journal                                                            |
| authors                            | List of authors                                                                |
| year                               | Year of publication                                                            |
| access                             | 1 = open access, 0 = closed                                                    |
| pdf                                | Filename of article’s PDF                                                      |
| page                               | Page number or article identifier                                              |
| supplementary                      | 1 = supplementary material, 0 = main article                                   |
---

## Metadata

| **Column Name**      | **Description**                                                             |
|-----------------------|-----------------------------------------------------------------------------|
| pdf                  | PDF filename used                                                          |
| doi                  | Digital Object Identifier                                                   |
| supplementary        | Indicates source location: 0 = main; 1 = supplementary                     |
| authors              | List of authors                                                            |
| title                | Title of the article                                                       |
| journal              | Journal name                                                               |
| year                 | Year of publication                                                        |
| page                 | Page number or article ID where data was found                             |
| access               | 1 = Open Access, 0 = Closed Access                                          |

!!! note "Key Notes"
    - **Objective:** Extraction of chemical structures of drugs and coformers forming a multi-component crystal (cocrystal or salt), and the corresponding change in photostability of the solid form compared to the original drug  
    - **Extracted entities:**  
      • Name of cocrystal (`name cocrystal`)  
      • Component ratio (`ratio cocrystal`)  
      • Drug name and SMILES (`name drug`, `SMILES drug`)  
      • Coformer name and SMILES (`name coformer`, `SMILES coformer`)  
      • Photostability change (`photostability change`)  
    - **Metadata includes:**  
      • Bibliographic information (DOI, authors, journal, title, year, open access)  
      • Source type and page (manuscript, figure, table, etc.)  
      • Supplementary material indicator  
    - **Not included when:**  
      • Crystalline structure (Refcode) is not specified  
      • There are errors in data transferred from figures  
      • Photodegradation mechanism of the original molecule is not described  

---

## Text Description

This dataset focuses on the photostability of pharmaceutical molecules and the effect of forming multi-component crystals (cocrystals or salts) with coformers. Photostability is a critical property in drug formulation, as exposure to light can degrade therapeutic compounds.

The dataset captures the relationship between the crystal form and the photostability of the drug by documenting:

- The identity and ratio of components in the crystal  
- Molecular structures of the drug and coformer (in SMILES format)  
- Reported change in photostability compared to the original drug  

Information was extracted from peer-reviewed publications and supplementary materials. SMILES structures were taken from figures or manually interpreted based on names and structures. Each record includes a detailed citation trail (DOI, journal, authors, etc.) and data source within the article (e.g., table, figure, or text).

Manual validation flags indicate entries needing correction or further review.

---

## Validation Results

**Validation process description:**

- Manual extraction of drug/coformer names and their SMILES from figures and text  
- Recording the component ratio and photostability change as described in the article  
- Cross-checking SMILES for accuracy and consistency  
- Flagging issues such as:  
  • Errors in SMILES (drug or coformer)  
  • Missing or inaccurate origin details  
  • Unclear photostability interpretation  

**Validation metadata includes:**

- `verification_required`: Whether manual review was needed  
- `verified_by`: Validator's name  
- `verification_date`: Date of review  
- `has_mistake_in_data`: Whether data errors were found  
- `has_mistake_in_metadata`: Whether metadata errors were found  
- `entry_status`: Final status (e.g., Verified, Requires correction)  
- `comment`: Notes on specific issues (e.g., incorrect SMILES)  

---
