# Chelate Complexes

## Original Data

**Title**: Chelate Complexes  
**Description**:  
The dataset contains data on thermodynamic stability constants (lgK) of chelate complexes formed by gallium (Ga), gadolinium (Gd), technetium (Tc), lutetium (Lu), and a variety of chelating ligands. These complexes are studied as potential contrast agents in magnetic resonance imaging (MRI) and other diagnostic applications.

- **Total number of records**: 907  
- **Number of features (columns)**: 20  
- **Application**: Small molecules

---

## Data Scheme

### Dataset – Column Descriptions

| **Column Name**         | **Description**                                                                               |
|--------------------------|-----------------------------------------------------------------------------------------------|
| pdf                     | PDF filename in the archive                                                                  |
| doi                     | DOI of the article                                                                            |
| doi_sourse              | Original DOI if the entry is cited from a review article                                     |
| supplementary           | Source flag: 0 – main article, 1 – supplementary materials                                   |
| title                   | Article title                                                                                 |
| publisher               | Publisher name                                                                                |
| year                    | Year of publication                                                                           |
| access                  | 1 = Open Access, 0 = Closed                                                                   |
| compound_id             | Identifier of the compound in the article                                                     |
| compound_name           | Name of the compound as cited                                                                 |
| SMILES                  | Canonical SMILES of ligand or ligand environment                                              |
| SMILES_type             | "ligand" = single ligand only, "environment" = full complex without metal                     |
| metal                   | Type of metal forming the complex                                                             |
| target                  | Stability constant (logK)                                                                     |
| page_smiles             | Page number where the ligand structure is found                                               |
| origin_smiles           | Source of SMILES extraction (e.g., figure 2, scheme 1, table 3)                               |
| page_metal              | Page number where the metal is mentioned                                                      |
| origin_metal            | Source of metal information (e.g., title, table caption, figure)                              |
| page_target_value       | Page where target value (logK) is found                                                       |
| origin_target_value     | Source of the target value                                                                    |


## Metadata

| **Column Name**     | **Description**                                               |
|----------------------|---------------------------------------------------------------|
| doi                  | Digital Object Identifier of the source article              |
| pdf                  | Filename of the article in the archive                        |
| title                | Title of the article                                          |
| publisher            | Publisher of the article                                      |
| year                 | Year of publication                                           |
| access               | 1 = Open Access, 0 = Closed Access                            |
---

## Key Notes

**Objective**:  
To collect and standardize thermodynamic data for metal–ligand complexes from the literature, with a focus on compounds likely to be used as contrast agents in medical applications.

**Extracted entities** include:
- `compound_id` – compound's identifier
- `compound_name` – compound's abbreviated name
- `smiles` – ligand structure in canonical SMILES notation
- `metal` – metal forming the complex
- `target` – thermodynamic stability constant (lgK)

**Notes**:
- All structures are converted into canonical SMILES format using RDKit.
- Stereochemistry is intentionally stripped to ensure standardization.
- The dataset includes only structures and values that were directly available in the source documents and satisfied certain extraction criteria.

---

## Text Description

This dataset provides curated measurements of the thermodynamic stability constants (lgK) for metal–ligand complexes, extracted from scientific publications. These stability constants reflect the strength of binding between metal (such as Gd, Ga, Tc, Lu) and chelating organic ligands.

Each record represents a distinct complex and includes:
- an extracted ligand structure (`smiles`)
- the central metal ion involved (`metal`)
- the thermodynamic constant (`target`, as lgK)
- bibliographic metadata and direct page/section references

This dataset can be used to facilitate the study of metal–ligand binding behavior and to serve as a benchmark for information extraction tools in chemical and biomedical domains.

---

## Validation Results

The Complexes dataset exhibited 
**212 corrections** (**190 pattern-based** and **22 isolated**) across **907 rows** and **6 columns**. 
Errors were concentrated in the `compound_name`, `compound_id`, and `SMILES` columns. 
Recurring issues involved incomplete mapping of compounds to figure annotations (e.g., missing IDs like “9A”), 
and tautomeric or scaffold inconsistencies in `SMILES` strings due to batch extraction from multi-ligand diagrams. 
These errors frequently repeated within figure groups, enabling the derivation of correction rules.

![Complexes_bar_total_corrections.svg](..%2Fassets%2FComplexes_bar_total_corrections.svg)

