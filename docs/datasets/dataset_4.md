# Nanozymes – Catalytic Properties of Nanozyme Materials

---

## Original Data

**Title:** Nanozymes dataset – Comprehensive information about nanozyme materials and their catalytic activity  
**Description:** This dataset captures essential experimental information on nanozymes, including their chemical composition, structural and morphological properties, catalytic behavior, and reaction conditions. Data was manually extracted from scientific publications, with each row representing a unique experimental setup or measurement. The dataset supports the exploration of structure–activity relationships and benchmarking of nanozyme performance under varying conditions.  
**Total number of records:** 1135  
**Number of features (columns):** 27  
**Data type:** Mixed  
**Application:** Nanomaterials  
**Automatic validation:** No

---

## Data Scheme

### Nanozymes Dataset – Column Descriptions

| **Column Name**        | **Description**                                                                 |
|------------------------|---------------------------------------------------------------------------------|
| formula                | Chemical formula of the nanozyme (e.g., Fe₃O₄, CeO₂)                            |
| activity               | Catalytic activity type (e.g., peroxidase, oxidase)                             |
| syngony                | Crystal system (e.g., cubic, hexagonal)                                         |
| length                 | Nanoparticle length in nm                                                       |
| width                  | Width in nm                                                                     |
| depth                  | Depth or thickness in nm                                                        |
| surface                | Surface functionalization or modification (e.g., PEG, PVP)                      |
| km_value               | Michaelis constant (Km)                                                         |
| km_unit                | Unit for Km value (e.g., mM, µM)                                                |
| vmax_value             | Maximum rate of reaction (Vmax)                                                 |
| vmax_unit              | Unit for Vmax value (e.g., µmol/min, mM/s)                                      |
| target_source          | Source of target activity value in publication                                  |
| reaction_type          | Substrate and co-substrate used in the reaction (e.g., TMB + H₂O₂)              |
| c_min                  | Minimum substrate concentration (in mM)                                         |
| c_max                  | Maximum substrate concentration (in mM)                                         |
| c_const                | Constant concentration of co-substrate                                          |
| c_const_unit           | Unit of co-substrate concentration (e.g., mM, µM)                               |
| ccat_value             | Catalyst (nanozyme) concentration used                                          |
| ccat_unit              | Unit of catalyst concentration (e.g., mg/mL)                                    |
| ph                     | pH at which reaction was carried out                                            |
| temperature            | Temperature in Celsius                                                          |
| doi                    | DOI of the source article                                                       |
| pdf                    | PDF filename in the dataset                                                     |
| access                 | Access status (1 = open access, 0 = closed access)                              |
| title                  | Title of the source publication                                                 |
| journal                | Journal name                                                                    |
| year                   | Year of publication                                                             |
---

## Metadata

| **Column Name**   | **Description**                                                |
|------------------|----------------------------------------------------------------|
| journal          | Name of the journal                                            |
| title            | Title of the original article                                  |
| doi              | Digital Object Identifier of the article                       |
| year             | Year of publication                                            |
| access           | Access status (1 = Open Access, 0 = Closed Access)             |
| pdf              | Filename of the source article's PDF in the archive            |

!!! note "Key Notes"
    - **Units**: All concentration- and activity-related units are embedded directly in column names or represented in separate "unit" columns  
    - **Surface**: If blank, indicates no surface modification or not reported  
    - **Missing values**: Parameters not provided in an article are left blank in the dataset  
    - Each row corresponds to a distinct experiment (not just a unique article)  
    - Dataset is intended for benchmarking and structure–activity analysis of nanozymes  

---

## Text Description

The **Nanozymes dataset** aggregates detailed experimental measurements related to the catalytic properties of synthetic enzyme-mimicking nanoparticles (nanozymes). These materials mimic natural enzymes and are used in biosensing, environmental detection, and therapeutic applications.

For each experiment, the dataset captures:

- **Composition and structure**: including chemical formula and crystal system (syngony)  
- **Morphology**: dimensions of the particles (length, width, depth)  
- **Surface chemistry**: coating or functional groups, if present  
- **Catalytic performance**: Michaelis constant (Km), maximum reaction rate (Vmax), type of catalytic reaction  
- **Reaction conditions**: substrate concentrations, catalyst concentration, pH, temperature  

The dataset supports comprehensive **benchmarking of nanozyme activity** and deeper investigation into **structure–function relationships**. It also facilitates **machine learning** and **data-driven modeling** in nanozyme design.

---

## Validation Results

The Nanozymes dataset underwent **439 corrections** across **1,135 rows** and **21 columns**, comprising **398 pattern-based** and **41 isolated issues**. 
The most frequently affected fields were `syngony`, `formula`, and `temperature`. 
Common errors included inferred values not explicitly stated in the source material—particularly crystal symmetry—along with formatting inconsistencies in chemical formulas and unit reporting. 
Many corrections followed recurring patterns within individual articles, allowing reliable extrapolation across related entries.



