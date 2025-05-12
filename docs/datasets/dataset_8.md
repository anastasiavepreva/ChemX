# Eye Drops

---

## Original Data

**Title:** Eye Drops  
**Description:**  
The dataset contains data on the corneal permeability of small molecules represented in SMILES format. The compounds are primarily pharmaceutical substances, and the dataset was compiled to support the development of predictive models for corneal permeability – a key factor in ophthalmic drug delivery.

**Total number of records:** 163  
**Number of features (columns):** 12
**Data type:** Tables  
**Application:** Small molecules  
**Automatic validation:** Yes

---

## Data Scheme

### Dataset – Column Descriptions

| **Column Name**   | **Description**                                                                 |
|-------------------|---------------------------------------------------------------------------------|
| smiles            | SMILES of the compound. Manually drawn and curated based on compound name      |
| name              | Name of the pharmaceutical compound                                             |
| perm (cm/s)       | Corneal permeability (direct or calculated)                                     |
| logP              | Logarithm of corneal permeability (direct or calculated)                        |
| doi               | DOI of the article (if available)                                               |
| PMID              | PubMed ID (if available)                                                        |
| title             | Title of the source article                                                     |
| publisher         | Publisher of the article                                                        |
| year              | Year of publication                                                             |
| access            | Access status: 1 = open, 0 = closed                                              |
| page              | Page number where the data was located                                          |
| origin            | Source location within the article (e.g., table 3)                              |

---

## Metadata

| **Column Name** | **Description**                           |
|------------------|-------------------------------------------|
| doi              | Digital Object Identifier of the article |
| PMID             | PubMed ID                                 |
| title            | Article title                             |
| publisher        | Publisher                                 |
| year             | Year of publication                       |
| access           | 1 = Open Access, 0 = Closed Access        |
| page             | Page number with relevant data            |
| origin           | Source location inside the article        |

!!! note "Key Notes"
    - **Objective:** Extraction and structuring of corneal permeability data for small molecules used in ophthalmology  
    - **Extracted entities:**  
      • SMILES of compound  
      • Corneal permeability (`perm (cm/s)`)  
      • Logarithm of permeability (`logP`)  
    - **SMILES were not directly extracted from the articles** – they were drawn manually based on compound names and additional table information  
    - Additional metadata is included to support traceability (e.g., PMID, DOI, title, publisher, year)  
    - Validation includes manual verification and error flagging for both data and metadata  

---

## Text Description

The Eye Drops dataset compiles structured data on the corneal permeability of pharmaceutical compounds, which is a critical property for evaluating the effectiveness of topical ophthalmic drugs. The dataset includes 163 entries, each representing a distinct compound.

For each entry, the following are recorded:

- SMILES structure  
- Compound name  
- Permeability (in cm/s)  
- logP value  

SMILES structures were obtained manually based on compound names presented in the articles, especially when names were incomplete or represented as derivatives. Where only logP or permeability values were available, the corresponding missing value was calculated.

Comprehensive metadata is provided for each entry, including bibliographic details (e.g., title, publisher, year, access type, page, and origin of data). Each entry has been manually reviewed and verified where necessary, with flags indicating any errors found in content or metadata.

---

## Validation Results

In the Eye Drops dataset, 
**23 corrections** were applied (**20 pattern-based** and **3 isolated**) 
across **163 rows**. Affected fields included `perm (cm/s)`, `name`, and `smiles`. 
Errors stemmed from inconsistencies between compound names and structures, 
along with occasional misentries in permeability values.

![Eye Drops_bar_total_corrections.svg](..%2Fassets%2FEye%20Drops_bar_total_corrections.svg)



