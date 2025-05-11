# Loading and Working with ChemEx Datasets

This section demonstrates a basic usage scenario of one of the ChemEx datasets hosted on Hugging Face. The following code is fully reproducible in Google Colab or any Jupyter-based environment.

The demo uses the **cytox_NeurIPS_updated_data** dataset, which contains cytotoxicity data for various nanomaterials.  
This example includes:

- Loading the dataset into a pandas DataFrame using the `datasets` library  
- Accessing the underlying Parquet file directly  
- Programmatically downloading and parsing the Croissant metadata description

---

## 1. Installing Dependencies

```python
!pip install pandas datasets requests pyarrow
```

---

## 2. Loading the Dataset via Hugging Face Datasets

To quickly access pre-processed datasets, we use the `datasets` library. It automatically fetches the `.parquet` file and converts it to a pandas DataFrame.

```python
from datasets import load_dataset

# Unique dataset identifier on Hugging Face
dataset_id = "ai-chem/Nanozymes"

dataset = load_dataset(dataset_id)
df = dataset["train"].to_pandas()

df.head()
```

📌 Using `datasets` provides automatic integration with Croissant metadata.

---

## 3. Alternative: Load the Raw Parquet File

If you prefer direct control over file access — for example, loading a specific chunk — you can work directly with the raw `.parquet` file using pandas:

```python
import pandas as pd

# Direct link to Parquet file
parquet_url = "https://huggingface.co/datasets/ai-chem/Nanozymes/resolve/main/data/train-00000-of-00001.parquet"

# Loading with pandas and pyarrow
df = pd.read_parquet(parquet_url, engine="pyarrow")

df.head()
```

📌 Ensure that the link points to the raw file using `/resolve/` instead of `/blob/`.

---

## 4. Download and View Croissant Metadata

Each dataset in ChemEx includes a **Croissant file** — a machine-readable schema and metadata description in JSON-LD format.  
It is used for structural validation, typing, and metadata inspection.

```python
import requests

# Direct link to Croissant JSON file
url = "https://huggingface.co/api/datasets/ai-chem/Nanozymes/croissant"

# Downloading
response = requests.get(url)

# Saving locally
with open("dataset.croissant.json", "wb") as f:
    f.write(response.content)
```

---

## 5. Load and Inspect Metadata Structure

Open the Croissant file and display its contents:

```python
import json

with open("dataset.croissant.json", "r") as f:
    croissant_data = json.load(f)

# View in readable form
print(json.dumps(croissant_data, indent=2))
```

Optional: You can explore `recordSet`, `field`, and `dataType` to understand the schema.

---

## Summary

This basic workflow demonstrates:

- Two approaches for accessing tabular data (via `datasets` and raw file streams)  
- Integration with open metadata and reproducibility standards (Croissant)  
- Compatibility between Hugging Face datasets, pandas, and JSON-based ecosystems

---

## References

- [Dataset page on Hugging Face](https://huggingface.co/datasets/ai-chem/Nanozymes)  
- [Hugging Face Datasets documentation](https://huggingface.co/docs/datasets/)  
- [Croissant Specification (MLCommons)](https://mlcommons.org/croissant/)
