# Cytotoxicity of nanoparticles in nor-
mal and cancer cell lines
---


## Original Data

**Title:** Cytotoxicity of nanoparticles in normal and cancer cell lines  
**Description:** The dataset contains information on the toxicity of inorganic nanoparticles on various normal and cancer cell lines.  
**Total number of records:** 5476  
**Number of features (columns):** 34  
**Data type:** Mixed  
**Application:** Nanomaterials  
**Automatic validation:** Yes

---

## Data Scheme

Below is a description of all the fields present in the dataset.

### Cytotoxicity Dataset – Column Descriptions

| **Column Name**             | **Description**                                                                 |
|----------------------------|---------------------------------------------------------------------------------|
| sn                         | Index of the sample (serial number).                                           |
| material                   | Composition of the nanoparticle/material tested (e.g., SiO₂, Ag).              |
| shape                      | Physical shape of the particle (e.g., Sphere, Rod).                            |
| coat_functional_group      | Surface coating or functionalization (e.g., CTAB, PEG).                        |
| synthesis_method           | Synthesis method (e.g., Precipitation, Commercial).                            |
| surface_charge             | Reported surface charge (e.g., Negative, Positive).                            |
| size_in_medium_nm          | Hydrodynamic size in biological medium (nm).                                   |
| zeta_in_medium_mv          | Zeta potential in medium (mV; blank if not measured).                          |
| potential_mv               | Surface charge in solution (mV).                                               |
| no_of_cells_cells_well     | Cell density per well in the assay.                                            |
| cell_type                  | Specific cell line name (e.g., PC12, A549).                                    |
| human_animal               | Origin of cells (A = Animal, H = Human).                                       |
| cell_source                | Species/organism (e.g., Rat, Human).                                           |
| cell_tissue                | Tissue origin of the cell line (e.g., Adrenal Gland, Lung).                    |
| cell_morphology            | Cell shape (e.g., Irregular, Epithelial).                                      |
| cell_age                   | Developmental stage of cells (e.g., Adult, Embryonic).                         |
| time_hr                    | Exposure duration in hours.                                                    |
| concentration              | Tested concentration of the material (e.g., µg/mL).                            |
| test                       | Cytotoxicity assay type (e.g., MTT, LDH).                                      |
| test_indicator             | Reagent measured (e.g., TetrazoliumSalt for MTT).                              |
| viability_%                | Cell viability percentage relative to control.                                 |
| doi                        | Digital Object Identifier (DOI) of the article.                                |
| article_list               | Identifier for the article in the dataset.                                     |
| core_nm                    | Primary particle size (nm).                                                    |
| hydrodynamic_nm            | Size in solution including coatings (nm).                                      |
| journal_name               | Name of the publishing journal.                                                |
| publisher                  | Publisher of the article.                                                      |
| year                       | Year of publication.                                                           |
| title                      | Title of the article from which data was extracted.                            |
| journal_is_oa             | Whether the journal is Open Access (TRUE/FALSE).                               |
| is_oa                     | Whether the specific article is Open Access (TRUE/FALSE).                      |
| oa_status                 | Open Access status (e.g., hybrid, gold, closed).                               |
| pdf                        | Filename of the corresponding PDF in the PDF archive.                         |
| access                     | Access status (1 = open, 0 = closed).                                          |

---

## Metadata

All metadata is included in the main table and also used for source validation.

| **Column Name**   | **Description**                                                            |
|------------------|----------------------------------------------------------------------------|
| journal_name     | Name of the publishing journal.                                            |
| publisher        | Publisher of the article.                                                  |
| year             | Year of publication.                                                       |
| title            | Title of the article.                                                      |
| journal_is_oa    | Whether the journal is Open Access (TRUE/FALSE).                           |
| is_oa            | Whether the specific article is Open Access (TRUE/FALSE).                  |
| oa_status        | Open Access status at article level (e.g., hybrid, gold, closed).          |
| pdf              | File name of the article PDF in archive.                                   |
| access           | Access code (1 = open access, 0 = closed access).                          |

!!! note "Key Notes"
    - `human/animal`: "A" for Animal, "H" for Human  
    - `viability (%)`: Values >100% may indicate proliferation stimulation  
    - Blanks: Missing values (e.g., zeta in medium) imply unreported data  

---

## Text Description

The dataset contains experimental data on the effects of inorganic nanoparticles on human and animal cells. The main focus is on the assessment of cytotoxicity using standard tests (e.g., MTT) to understand how different nanoparticle characteristics (shape, size, charge, coating) affect cell survival.

Each entry includes:

- Nanoparticle characteristics (material, shape, size, charge, etc.)
- Cell line information (source, tissue, morphology, etc.)
- Experimental conditions (exposure time, concentration, etc.)
- Results of cell survival tests
- Publication metadata (DOI, journal, year, etc.)

The aim of the dataset is to contribute to the investigation of the patterns between nanoparticle parameters and their cytotoxic effects.

---

## Validation Results

In the Cytotox dataset, a total of **1,351 corrections** were identified, nearly all of which (**1,350**) were **pattern-based**. 
These were mostly found in the `cell_type`, `test`, and `test_indicator` columns. 
The predominant problems involved terminology inconsistencies, abbreviation mismatches, and stylistic variation across sources. 
The high pattern consistency enabled efficient rule-based correction.



---
