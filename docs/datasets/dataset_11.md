# Magnetic Nanomaterials

---

## Original Data

**Title:** Magnetic Nanomaterials  
**Description:**  
The dataset contains comprehensive information about magnetic nanoparticles, including core-shell structures and their magnetic properties. It combines three distinct datasets: two focusing on MRI and hyperthermia applications (from Pasha Kim), and one dedicated to exchange bias phenomena.

**Total number of records:** 2578  
**Number of features (columns):** 39  
**Data type:** Mixed  
**Application:** Nanomaterials  
**Automatic validation:** Yes

---

## Data Scheme

### Dataset Structure
The dataset is organized into several key categories:

1. **Compositional Data**
   - Core and shell materials
   - Multiple shell layers (where applicable)
   - Normalized compositions

2. **Physical Characteristics**
   - Size measurements from various techniques
   - Morphological properties
   - Crystallographic information

3. **Magnetic Properties**
   - SQUID measurements
   - Exchange bias parameters
   - Magnetization data

4. **Application-specific Parameters**
   - MRI-related properties
   - Hyperthermia characteristics

### Magnetic Nanomaterials – Column Descriptions

| **Category**           | **Column Name**                    | **Description**                                               |
|------------------------|------------------------------------|---------------------------------------------------------------|
| Composition            | name                               | Sample or material name (if given)                            |
|                        | np_core                            | Material of the nanoparticle core                             |
|                        | np_shell                           | Material of the shell                                         |
|                        | np_shell_2                         | Second shell layer (optional)                                 |
|                        | core_shell_formula                 | Combined formula for core-shell system                        |
| Structural Properties  | np_hydro_size                      | Hydrodynamic size (nm)                                        |
|                        | xrd_scherrer_size                  | Size from XRD using Scherrer equation                         |
|                        | emic_size                          | Size from electron microscopy                                 |
|                        | space_group_core                   | Core crystallographic space group                             |
|                        | space_group_shell                  | Shell crystallographic space group                            |
|                        | xrd_crystallinity                  | Crystallinity status based on XRD                             |
| Magnetic Properties    | squid_h_max                        | Max magnetic field in SQUID (kOe)                             |
|                        | fc_field_T                         | Field-cooled field strength (T)                               |
|                        | squid_temperature                  | SQUID measurement temperature (K)                             |
|                        | squid_sat_mag                      | Saturation magnetization (emu/g)                              |
|                        | coercivity                         | Coercive field strength (kOe)                                 |
|                        | squid_rem_mag                      | Remanent magnetization (emu/g)                                |
|                        | exchange_bias_shift_Oe             | Exchange bias field shift (Oe)                                |
|                        | vertical_loop_shift_M_vsl_emu_g    | Vertical loop shift (emu/g)                                   |
|                        | hc_kOe                             | Coercive field from hysteresis loop (kOe)                     |
| MRI / Hyperthermia     | htherm_sar                         | Specific absorption rate (W/g)                                |
|                        | mri_r1                             | MRI relaxation rate r1 (mM⁻¹·s⁻¹)                             |
|                        | mri_r2                             | MRI relaxation rate r2 (mM⁻¹·s⁻¹)                             |
| Experimental Details   | zfc_h_meas                         | Field used for ZFC measurement (kOe)                          |
|                        | instrument                         | Instrument used for measurement (e.g., SQUID)                 |
| Metadata               | doi                                | DOI of the publication                                        |
|                        | title                              | Article title                                                 |
|                        | journal                            | Journal name                                                  |
|                        | publisher                          | Publisher name                                                |
|                        | year                               | Year of publication                                           |
|                        | pdf                                | Filename of the associated PDF                                |
|                        | access                             | Access status: 1 = OA, 0 = closed                             |
| Validation             | verification required              | Whether manual verification is needed                         |
|                        | verified_by                        | Name of validator                                             |
|                        | verification_date                  | Date of verification                                          |
|                        | has_mistake_in_matadata            | Whether metadata has a mistake                               |
|                        | comment                            | Notes by validator                                            |
| Internal IDs           | article_name_folder                | Internal folder name for the article                         |
|                        | supp_info_name_folder              | Supplementary info folder name                               |

---

## Metadata

| **Field**                | **Description**                                  |
|--------------------------|--------------------------------------------------|
| doi                      | Digital Object Identifier                        |
| title                    | Title of the article                             |
| journal                  | Name of the journal                              |
| publisher                | Publisher’s name                                 |
| year                     | Year published                                   |
| pdf                      | PDF file name in the archive                     |
| access                   | 1 = open access, 0 = closed                      |

---

!!! note "Key Notes"
    - **Purpose:** Extraction and structuring of magnetic properties data from nanoparticle research
    - **Key Features:**
      • Comprehensive magnetic characterization
      • Multiple size measurement techniques
      • Detailed crystallographic information
      • Application-specific parameters (MRI, hyperthermia)
    - **Data Sources:** Combines three distinct datasets with different focus areas
    - **Validation:** Includes both automated and manual verification processes

---

## Text Description

The Magnetic Nanomaterials Dataset is a comprehensive collection of data focusing on magnetic nanoparticles and their properties. It encompasses information from three distinct datasets, each contributing unique aspects of magnetic nanomaterial characterization:

- Core-shell structures and compositions
- Magnetic properties measured through various techniques
- Application-specific characteristics for medical applications
- Detailed structural and morphological information

The dataset is particularly valuable for researchers working in:
- Magnetic resonance imaging (MRI)
- Magnetic hyperthermia
- Exchange bias phenomena
- Nanoparticle synthesis and characterization

---

## Validation Results

**Validation process includes:**

- Automated data extraction verification
- Manual cross-checking of numerical values
- Verification of unit conversions and standardization
- Structure and composition validation
- Metadata completeness checking

Each entry undergoes verification with flags for:
- Data accuracy (`has_mistake_in_data`)
- Metadata accuracy (`has_mistake_in_metadata`)
- Verification status tracking
- Validator assignment and dating

---
