# ChemX: A Collection of Chemistry Datasets for Benchmarking Automated Information Extraction

A multimodal benchmark for evaluating machine learning models that extract structured chemical data from scientific literature.

---

## About the Project

**ChemX** is a curated benchmark suite aimed at assessing and improving the performance of AI systems in extracting structured chemical information from scientific articles across multiple modalities: text, tables, and figures.

The benchmark covers diverse chemical topics, including nanomaterials, small molecules, chelate complexes, and their properties relevant for various applications.

!!! tip "Project Goal"
    Enable reliable and scalable chemical knowledge extraction by combining multimodal data annotation with expert validation, thereby accelerating downstream scientific research.

![Текст](assets/main_page-0001.jpg)
---

## Key Features

- **10 manually annotated datasets** across a range of chemical subfields  
- **Over 16,000 structured records** extracted from peer-reviewed literature  
- **Multimodal data sources**: text passages, tables, chemical diagrams, figures  
- **Provenance and annotation metadata** for every data point  
- **Expert-reviewed annotations** ensuring high data quality  
- **Standardized evaluation benchmarks** for NLP, vision, and multimodal models  

---

## Why It Matters

Despite advances in large language and vision-language models, scientific chemistry lags behind in AI adoption due to the lack of reliable, multimodal, annotated benchmarks.

!!! quote "The Solution"
    ChemX closes this gap by providing a transparent, high-quality benchmark for evaluating and training data extraction systems, validated by domain experts.

---

## How to Use ChemX

- Train and test models to extract chemical entities, values, units, and relationships  
- Compare performance across extraction tasks using a unified evaluation framework  
- Explore multimodal learning for chemistry-specific document analysis  
- Use structured chemical data for tasks like toxicity modeling, material design, and reaction planning  

---

## Site Sections

### Overview
[Motivation](overview/project_motivation.md), annotation pipeline, and an [overview of all datasets](overview/datasets_description.md).

### Datasets

#### Nanomaterials
- [Cytotoxicity Dataset](datasets/dataset_1.md/) — Nanoparticle toxicity in mammalian cells  
- [SelTox Dataset](datasets/dataset_2.md/) — Nanoparticle toxicity in microbial systems  
- [Synergy Dataset](datasets/dataset_3.md/) — Antibiotic–nanoparticle interaction effects  
- [Nanozymes Dataset](datasets/dataset_4.md/) — Enzymatic activity of nanozymes  
- [Magnetic Nanomaterials](datasets/dataset_11.md/) — Magnetic property extraction  

#### Small Molecules
- [Benzimidazole Antibiotics](datasets/dataset_5.md/) — Inhibitory concentrations of benzimidazoles  
- [Oxazolidinone Antibiotics](datasets/dataset_6.md/) — Activity profiling of oxazolidinones  
- [Chelate Metal Complexes](datasets/dataset_7.md/) — Thermodynamic parameters of chelates  
- [Eye Drops](datasets/dataset_8.md/) — Corneal permeability and pharmaceutical properties   
- [Cocrystal Photostability](datasets/dataset_9.md/) — Stability of pharmaceutical co-crystals

### Methods
Detailed pipeline for annotation, validation, and benchmarking:

- [Approach](methods/approach.md)
- [Data Extraction](methods/data_extraction.md)  
- [Data Validation](methods/data_validation.md)  
- [Benchmarking](methods/benchmarking.md)  

### [Guideline](tutorial.md)
Examples for training and evaluating extraction models with CDEB datasets.

### [About the Project](about/team.md)
Team, how to cite the project, version history, and acknowledgments.

---

## Quick Start

```python
from datasets import load_dataset

# Unique dataset identifier on Hugging Face
dataset_id = "ai-chem/Nanozymes"
dataset = load_dataset(dataset_id)
df = dataset["train"].to_pandas()
df.head()
```
