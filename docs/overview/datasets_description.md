# Dataset Overview

---

## Introduction

This section summarizes the datasets included in the **Chemical Data Extraction Benchmark (ChemX)** — a curated collection designed to support training and evaluation of models for multimodal information extraction from chemistry publications.

The datasets span a wide range of chemical subdomains and include annotations from text, tables, and visual content such as plots and chemical diagrams.

!!! note "Data Quality"
    All datasets were manually annotated and rigorously cross-validated by chemistry experts to ensure high accuracy and consistency.

---

## Data Types and Sources

The datasets were constructed from full-text PDFs of peer-reviewed articles, combining both automated extraction and manual correction. Each dataset may include:

- Experimental values (e.g., MIC, logP, lgK, catalytic constants)  
- Chemical identifiers and structures (e.g., SMILES, compound names)  
- Tabular and visual content (figures, plots, spectra, diagrams)  
- Source metadata (DOI, title, authors, journal, year, accessibility)

Data originated from:

- Main article bodies  
- Supplementary materials  
- Structured tables and unstructured figures  
- OCR and model-assisted extraction workflows

!!! tip "Multimodal Composition"
    ChemX datasets contain text, table, and figure-based data, enabling the evaluation of models that process diverse input formats.

---

## Dataset Structure and Organization

Each dataset is provided in a structured tabular format (CSV or Parquet), and is accompanied by:

- Full provenance metadata  
- A detailed schema describing fields and units  
- Validation outputs (where applicable)  
- A Croissant metadata file for interoperability via Hugging Face

!!! note "Supporting Documentation"
    All datasets include source article lists, annotation guidelines, and usage notes.

---

## Summary Table of Datasets

| Dataset Name           | Domain          | Records | Modalities             | Expert Validation | Link                                    |
|------------------------|-----------------|---------|------------------------|--------------------|-----------------------------------------|
| Cytotoxicity           | Nanomaterials   | 5535    | Text, tables, figures  | ✅                  | [Learn more](../datasets/dataset_1.md)  |
| SelTox                 | Nanomaterials   | 3286    | Text, tables, figures  | ✅                  | [Learn more](../datasets/dataset_2.md)  |
| Synergy                | Nanomaterials   | 3226    | Text, tables, diagrams | ✅                  | [Learn more](../datasets/dataset_3.md)  |
| Nanozymes              | Nanomaterials   | 1133    | Text, diagrams         | ✅                  | [Learn more](../datasets/dataset_4.md)  |
| Magnetic nanomaterials | Nanomaterials   | 2579    | Text, tables           | ✅                  | [Learn more](../datasets/dataset_11.md) |
| Benzimidazoles         | Small molecules | 1721    | SMILES, numeric values | ✅                  | [Learn more](../datasets/dataset_5.md)  |
| Oxazolidinones         | Small molecules | 3103    | SMILES, numeric values | ✅                  | [Learn more](../datasets/dataset_6.md)  |
| Chelate Complexes      | Small molecules | 907     | SMILES, lgK            | ✅                  | [Learn more](../datasets/dataset_7.md)  |
| Eye Drops              | Small molecules | 163     | SMILES, permeability   | ✅                  | [Learn more](../datasets/dataset_8.md)  |
| Photostability         | Small molecules | 70      | SMILES, photostability | ✅                  | [Learn more](../datasets/dataset_9.md)  |

--- 

## How to Use the Datasets

The ChemX datasets support a variety of research and development workflows:

- Training and evaluating information extraction systems (e.g., LLMs, OCR, image-text models)  
- Developing QSAR models and exploring structure–property relationships  
- Benchmarking multimodal AI for chemistry-focused applications  
- Supporting tasks in materials design, drug discovery, and toxicity prediction

!!! tip "Benchmark Usage"
    These datasets are already being used to evaluate state-of-the-art models on real-world chemical extraction tasks.

---

## Access to the Datasets

You can access the datasets via:

- [Hugging Face Datasets Hub](https://huggingface.co/ai-chem)  
- The [GitHub repository](https://github.com/ai-chem/CDEB)  
- Direct downloads (CSV/Parquet)  
- An upcoming PyPI Python package for programmatic access

!!! note "Croissant Files"
    Hugging Face releases include Croissant metadata files for structured dataset interoperability and schema validation.

---

## Example of Loading a Dataset in Python

```python
import pandas as pd

# Direct link to Parquet file
parquet_url = "https://huggingface.co/datasets/ai-chem/Nanozymes/resolve/main/data/train-00000-of-00001.parquet"

# Loading with pandas and pyarrow
df = pd.read_parquet(parquet_url, engine="pyarrow")

df.head()
```

---

# Summary

- ChemX provides a multimodal benchmark covering key chemical subfields  
- Datasets are expert-validated and rich in metadata  
- Designed for reproducible, scalable training and evaluation of AI models in chemistry  
- Fully documented and accessible through open platforms