# SelTox – Toxicity of Inorganic Nanoparticles on Bacteria

---

## Original Data

**Title:** SelTox dataset – Toxicity of inorganic nanoparticles in various normal and pathogenic bacterial strains  
**Description:** The dataset contains experimental information on the toxicity of inorganic nanoparticles tested against different bacterial strains, including both normal and multidrug-resistant (MDR) types.  
**Total number of records:** 3244  
**Number of features (columns):** 36  
**Data type:** Mixed  
**Application:** Nanomaterials  
**Automatic validation:** Yes

---

## Data Scheme

### SelTox Dataset – Column Descriptions

| **Column Name**                     | **Description**                                                                 |
|------------------------------------|---------------------------------------------------------------------------------|
| sn                                 | Internal index for entries.                                                    |
| np                                 | Name of the nanoparticle (e.g., Ag, Au, ZnO).                                  |
| coating                            | Surface coating or modification (1 = presence, 0 = none).                       |
| bacteria                           | Name of the tested bacterial strain.                                           |
| mdr                                | Indicator for multidrug-resistant strain (1 = MDR, 0 = non-MDR).               |
| strain                             | Specific strain identifier (if provided).                                      |
| np_synthesis                       | Synthesis method of the nanoparticle.                                          |
| method                             | Assay type used (e.g., MIC, ZOI).                                              |
| mic_np_µg_ml                       | MIC value in µg/mL for the nanoparticle.                                       |
| concentration                      | Concentration used for ZOI measurement.                                        |
| zoi_np_mm                          | ZOI (Zone of Inhibition) in millimeters.                                       |
| np_size_min_nm                     | Minimum nanoparticle size (nm).                                                |
| np_size_max_nm                     | Maximum nanoparticle size (nm).                                                |
| np_size_avg_nm                     | Average nanoparticle size (nm).                                                |
| shape                              | Morphology of the nanoparticle (e.g., spherical, rod).                         |
| time_set_hours                     | Duration of the antibacterial assay in hours.                                  |
| zeta_potential_mV                  | Zeta potential (in mV); blank if not reported.                                 |
| solvent_for_extract                | Solvent used in green synthesis (if applicable).                               |
| temperature_for_extract_C          | Temperature for extract preparation (°C).                                      |
| duration_preparing_extract_min     | Duration (in minutes) of extract preparation.                                  |
| precursor_of_np                    | Chemical precursor used for nanoparticle synthesis (e.g., AgNO₃).              |
| concentration_of_precursor_mM      | Concentration of precursor in millimolar.                                      |
| hydrodynamic_diameter_nm           | Hydrodynamic diameter in nanometers.                                           |
| ph_during_synthesis                | pH during nanoparticle synthesis.                                              |
| reference                          | External source or citation URL.                                               |
| doi                                | DOI of the publication.                                                        |
| article_list                       | Article ID in dataset.                                                         |
| pdf                                | Filename of the PDF in archive for reference checking.                         |
| access                             | Access status (1 = open access, 0 = closed access).                            |

---

## Metadata

| **Column Name**    | **Description**                                                             |
|--------------------|------------------------------------------------------------------------------|
| journal_name       | Name of the journal.                                                        |
| publisher          | Name of the publisher.                                                      |
| year               | Year of publication.                                                        |
| title              | Title of the article.                                                       |
| journal_is_oa      | Whether the journal is Open Access (`True` / `False`).                      |
| is_oa              | Whether the article itself is Open Access (`True` / `False`).               |
| oa_status          | Open Access status (e.g., green, gold, hybrid, closed).                     |
| pdf                | Name of the PDF file in the dataset.                                        |
| access             | Access status code (1 = open, 0 = closed).                                  |

!!! note "Key Notes"
    - `mdr`: 1 = Multidrug-resistant strain, 0 = Non-resistant  
    - Units are embedded in column names (e.g., nm, mM, °C, mm)  
    - Fields like `strain`, `zeta_potential`, `hydrodynamic diameter` may be blank if data is not reported  
    - `coating`: 0 = no coating, 1 = coating present  
    - Validation and verification were conducted based on original articles in PDF format

---

## Text Description

The SelTox dataset provides detailed experimental data on the antibacterial activity of inorganic nanoparticles against both normal and multidrug-resistant bacterial strains. It captures key physicochemical properties of nanoparticles (e.g., size, shape, synthesis method), assay conditions (e.g., MIC, ZOI), and biological targets (bacterial species and resistance status).

Each record includes:

- Nanoparticle specifications (material, synthesis method, size, zeta potential)  
- Biological target information (bacterial species, MDR status)  
- Assay type and result (MIC, ZOI)  
- Conditions of synthesis (e.g., solvent, temperature, pH)  
- Metadata and publication references (DOI, journal, year, etc.)

The goal of the dataset is to support research in nanotoxicology by enabling analysis of how nanoparticle characteristics correlate with antibacterial efficacy, particularly against drug-resistant strains.

---

## Validation Results

The SelTox dataset underwent **51 corrections** (**48 pattern-based** and **3 isolated**). 
Errors were mostly located in `np_synthesis`, `strain`, and `bacteria` columns, 
typically reflecting inconsistent terminology for biological strains or procedural details. 
Most issues were recurring and resolved via rule-based updates.



---
