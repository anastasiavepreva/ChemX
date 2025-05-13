# Benzimidazole Antibiotics – Chemical Structures and Antimicrobial Activity

---

## Original Data

**Title:** Benzimidazole antibiotics – chemical structures and antimicrobial activity  
**Description:** This dataset contains information on the chemical structures of benzimidazole-based antibiotics in SMILES format, along with their antimicrobial activity measured as Minimum Inhibitory Concentration (MIC) values against different Staphylococcus aureus and Escherecia coli strains. In addition to structures and target values, the dataset includes metadata such as source articles, extraction pages, origin type (table, text, image).  
**Total number of records:** 1721  
**Number of extracted features (columns):** 3 (main: SMILES and MIC), though the full table contains over 25 metadata columns  
**Input data type:** Mixed  
**Domain:** Small molecules / antibacterial compounds  
**Automatic validation:** Yes

---
## Extraction Prompt

This dataset was created using a specialized prompt for extracting information about benzimidazole antibiotics and their antimicrobial activity. The extraction system was configured to:

**System Message:**
"Domain-specific chemical information extraction assistant specializing in chemistry of small molecules, particularly antibiotics and their properties."

**Extraction Parameters:**
- Target compounds: Benzimidazole antibiotics
- Target properties: MIC or pMIC measurements
- Test organisms: Staphylococcus aureus and Escherichia coli
- Required fields:
  - `compound_id`: Molecule identifier within the article
  - `smiles`: SMILES representation of benzimidazole antibiotic
  - `target_type`: MIC or pMIC
  - `target_relation`: =, <, or >
  - `target_value`: Numeric value
  - `target_units`: Measurement units
  - `bacteria`: Test organism name

**Extraction Rules:**
1. Each MIC/pMIC mention extracted separately
2. No filtering or deduplication
3. Ranges preserved as given
4. Complete SMILES strings constructed from scaffolds and residues
5. Only S. aureus and E. coli measurements included
6. Missing fields marked as "NOT_DETECTED"

---

## Data Scheme

### Column Descriptions

| **Column Name**       | **Description**                                                                 |
|------------------------|---------------------------------------------------------------------------------|
| `smiles`              | Extracted chemical structure in isomeric SMILES format                          |
| `doi`                 | DOI of the article from which the data was extracted                            |
| `title`               | Title of the article                                                            |
| `publisher`           | Publisher                                                                       |
| `year`                | Year of publication                                                             |
| `access`              | Access type (1 = open access, 0 = closed access)                                |
| `compound_id`         | Compound identifier in the article                                              |
| `target_type`         | Type of target measurement (e.g., MIC or pMIC)                                  |
| `target_relation`     | Relation symbol (e.g., =, >, <)                                                  |
| `target_value`        | Target value                                                                    |
| `target_units`        | Units of the target value (e.g., µg/mL)                                         |
| `bacteria`            | Bacterial species against which the compound was tested                         |
| `bacteria_unified`    | Unified name of the bacterial species (e.g., *Escherichia coli*)                |
| `page_bacteria`       | Page number where the bacterium is mentioned in the article                     |
| `origin_bacteria`     | Source of the bacterium mention (table, figure, text, image)                    |
| `section_bacteria`    | Section of the article (if `origin_bacteria = text`)                            |
| `subsection_bacteria` | Subsection (if `origin_bacteria = text`)                                        |
| `page_target`         | Page number where the target value is provided                                  |
| `origin_target`       | Source of the target value (table, figure, text, image)                         |
| `section_target`      | Section of the article (if `origin_target = text`)                              |
| `subsection_target`   | Subsection (if `origin_target = text`)                                          |
| `page_scaffold`       | Page with the chemical scaffold or full molecule diagram                        |
| `origin_scaffold`     | Origin of the scaffold image (table, figure, or unnumbered image)               |
| `page_residue`        | Page with substituent structures (if molecule is scaffold + residues)           |
| `origin_residue`      | Origin of the residue image (table, figure, or unnumbered image)                |

---

## Metadata

| **Field Name**    | **Description**                                           |
|-------------------|-----------------------------------------------------------|
| `doi`            | DOI of the original article                                |
| `title`          | Title of the publication                                   |
| `publisher`      | Publisher                                                  |
| `year`           | Year of publication                                        |
| `access`         | Access type (0 = closed, 1 = open access)                  |

!!! note "Key Notes"
    - **SMILES molecules** may be presented:  
      - As complete structures (use `scaffold` only)  
      - As scaffold + substituents (use both `scaffold` and `residue` columns)  
    - **Target values (MIC/pMIC)** are extracted with full context: value, units, source, and page  
    - **Bacterial names** are provided in both raw and unified formats  
    - **Data origin types** include:  
      - `table with number` (e.g., table 1)  
      - `figure with number` (e.g., scheme 1)  
      - `image` – unnumbered image inside the text  
      - `text` – if extracted directly from the article's text  
    - **Section/subsection** fields are filled only when data is extracted from text or image  

---

## Text Description

The goal of this dataset is to collect and structure chemical and biological data on benzimidazole-based antibiotics and their activity against bacterial pathogens. The primary target property is **MIC (Minimum Inhibitory Concentration)** expressed in µg/mL.

Each record includes:

- A **chemical structure** in SMILES format  
- Information about the **bacterial strain** tested  
- The **target value** (type, relation, numeric value, unit)  
- **Metadata** about the source article (DOI, journal, year, publisher, access)  
- **Detailed information on the source** in the article (page, table, figure, text, or image)

The dataset is intended for tasks such as **scientific information extraction**, **QSAR modeling**, **structure–activity analysis**, and **antibacterial research** involving small molecules.

---

## Validation Results

The Benzimidazoles dataset contained 
**77 corrections** (**63 pattern-based**, **14 isolated**), 
with the primary error loci being `smiles`, `target_value`, and `compound_id`. 
Common mistakes included inconsistent or incomplete `SMILES` structures and naming mismatches, 
often reflecting variable conventions across original publications.




