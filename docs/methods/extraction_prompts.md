# Extraction Prompts

## Overview

This page contains the standardized extraction prompts used to build the ChemX benchmark datasets. Each prompt is tailored to extract a specific type of chemical or biomedical information from scientific literature, ensuring **semantic consistency**, **structured formatting**, and **high-quality validation**.

All prompts follow the same structure:

- **System Message** – Defines the assistant’s role and domain knowledge.
- **Extraction Protocol** – Provides detailed instructions on what to extract, how to handle edge cases, and how to deal with missing or ambiguous information.
- **Required Fields** – Lists all expected fields with data types and example values.
- **Extraction Rules** – Custom constraints and logic relevant to each domain.
- **Output Format** – JSON array format illustrating the expected data structure.

These prompts are used with **large language models (LLMs)** for **automated extraction of structured data** from scientific documents. All extracted data is further subjected to **manual validation and expert review**.

---

## Dataset Prompts by Category

> Click on any dataset name to jump to its corresponding prompt.

### Nanomaterials:

- [Cytotox](#cytotox)
- [SelTox](#seltox)
- [Synergy](#synergy)
- [Nanozymes](#nanozymes)
- [Nanomag](#nanomag)

### Small Molecules:

- [Benzimidazoles](#benzimidazole-antibiotics)
- [Oxazolidinones](#oxazolidinone-antibiotics)
- [Co-crystals](#cocrystals)

### Metal Complexes:

- [Chelate Complexes – Ga](#complexes-ga)
- [Chelate Complexes – Gd](#complexes-gd)
- [Chelate Complexes – Tc](#complexes-tc)
- [Chelate Complexes – Lu](#complexes-lu)

---

### Looking for the actual datasets?

See the full descriptions on the [Datasets Overview](../overview/datasets_description.md) page.

---

## Benzimidazole Antibiotics

### System Message
```python
{
    "description": "You are a domain-specific chemical information extraction assistant.",
    "instructions": "You specialize in chemistry of small molecules. In particular, your area is antibiotics and their properties."
}
```

### Extraction Protocol

Your task is to extract **every** mention of MIC or pMIC measurements against Staphylococcus aureus and Escherichia coli bacteria for **ALL** benzimidazole antibiotics from a scientific article and output a **JSON array** of objects **only** (no markdown, no commentary, no extra text).

#### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `compound_id` | string | ID of a molecule within the article, as cited in the text | `"5a"`, `"Compound 3"` |
| `smiles` | string | Full SMILES representation of a benzimidazole antibiotic | |
| `target_type` | string | Type of measurement, either `"MIC"` or `"pMIC"`, exactly as stated | |
| `target_relation` | string | One of `"="`, `"<"`, or `">"`. If no relation symbol is shown, use `"="` | |
| `target_value` | number | The numeric value of MIC/pMIC (without quotes) | |
| `target_units` | string | MIC units | `"μg/mL"`, `"mg/L"` |
| `bacteria` | string | The organism against which MIC/pMIC was measured, named exactly as in the text | |

#### Extraction Rules

1. Extract **each** MIC/pMIC mention as a separate object. If multiple MIC/pMIC are reported for the same compound against different bacteria, list them as separate entries.

2. Do **not** filter, group, summarize, or deduplicate. Include repeated mentions and duplicates if they occur in different contexts.

3. If a range is given (e.g., "2–8 μg/mL"), leave it as a range.

4. If a molecule is fully depicted in a figure, write it as a SMILES string. If a molecule is depicted as a scaffold and residues separately in different places of an article, connect them by compound ID into one molecule and write it as a single SMILES string.

5. Extract only measurements with Staphylococcus aureus and Escherichia coli. Record full names, abbreviations, or any related taxonomic identifiers of bacteria.

6. If you cannot find a required field for an object, re-check the context; if it's still absent, set that field's value to `"NOT_DETECTED"`.

7. The example output shows only two extracted samples, however your output should contain **all** MIC or pMIC measurements of benzimidazole antibiotics present in the article.

### Output Format

```json
[
  {
    "compound_id": "11h",
    "smiles": "O=C(OCC)C1=C(N(C(=O)N(C1C2=C(C=CS2)C)[H])[H])C[N]3C=NC4=C3C=C(C=C4)[N+](=O)[O-]",
    "target_type": "MIC",
    "target_relation": "<",
    "target_value": 1,
    "target_units": "mmol/l",
    "bacteria": "methicillin-susceptible S. aureus"
  },
  {
    "compound_id": "5a",
    "smiles": "CCN1C=C(C(=O)C2=CC(=C(C=C21)N3CCN(CC3)C4=NC=CC(=N4)N)F)C(=O)O",
    "target_type": "pMIC",
    "target_relation": "<",
    "target_value": 2,
    "target_units": "μg/mL",
    "bacteria": "Escherichia coli"
  }
]
```

---

## Oxazolidinone Antibiotics

### System Message
```python
{
    "description": "You are a domain-specific chemical information extraction assistant.",
    "instructions": "You specialize in chemistry of small molecules. In particular, your area is antibiotics and their properties."
}
```

### Extraction Protocol

Your task is to extract **every** mention of MIC or pMIC values for oxazolidinone antibiotics from a scientific article and output a **JSON array** of objects **only** (no markdown, no commentary, no extra text).

#### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `compound_id` | string | ID of a molecule within the article, as cited in the text | `"5a"`, `"Compound 3"` |
| `smiles` | string | Full SMILES representation of an oxazolidinone antibiotic | |
| `target_type` | string | Type of measurement, either `"MIC"` or `"pMIC"`, exactly as stated | |
| `target_relation` | string | One of `"="`, `"<"`, or `">"`. If no relation symbol is shown, use `"="` | |
| `target_value` | number | The numeric value of MIC/pMIC (without quotes) | |
| `target_units` | string | MIC units | `"μg/mL"`, `"mg/L"` |
| `bacteria` | string | The organism against which MIC/pMIC was measured, named exactly as in the text. Record full names, abbreviations, or any related taxonomic identifiers of bacteria. | |

#### Extraction Rules

1. Extract **each** MIC or pMIC mention as a separate object.

2. Do **not** filter, group, summarize, or deduplicate. Include repeated mentions and duplicates if they occur in different contexts.

3. If a range is given (e.g., "2–8 μg/mL"), leave it as a range.

4. If a molecule is fully depicted in a figure, write it as a SMILES string. If a molecule is depicted as a scaffold and residues separately in different places of an article, connect them by compound ID into one molecule and write it as a single SMILES string.

5. If multiple measurement types appear for the same compound and bacterium (e.g., MIC₅₀, MIC₉₀), extract each separately.

6. If you cannot find a required field for an object, re-check the context; if it's still absent, set that field's value to `"NOT_DETECTED"`.

7. The example output shows only two extracted samples, however your output should contain **all** MIC or pMIC measurements of oxazolidinone antibiotics present in the article.

### Output Format

```json
[
  {
    "compound_id": "12b",
    "smiles": "CC1=CC=C(C=C1)C(=O)Nc2ccc(cc2)C(=O)N3CCCCC3=O",
    "target_type": "MIC",
    "target_relation": "<",
    "target_value": 1,
    "target_units": "mmol/l",
    "bacteria": "methicillin-susceptible S. aureus"
  },
  {
    "compound_id": "5a",
    "smiles": "CC1=CC=CC=C1N2C=NC3=CC=CC=C23",
    "target_type": "MIC",
    "target_relation": "=",
    "target_value": 2,
    "target_units": "μg/mL",
    "bacteria": "Escherichia coli"
  }
]
```

---

## Cocrystals

### System Message
```python
{
    "description": "You are a domain-specific chemical information extraction assistant.",
    "instructions": "You specialize in the chemistry of cocrystals and their properties. Your area of expertise includes analyzing cocrystals, their components, and photostability changes."
}
```

### Extraction Protocol

Your task is to extract **every** mention of photostability for co-crystals from a scientific article, and output a **JSON array** of objects **only** (no markdown, no commentary, no extra text).

#### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `name_cocrystal` | string | Name of cocrystal, as cited in the text | `"CAR-HCT"`, `"DMZ-SAC"` |
| `ratio_cocrystal` | string | Molar ratio of the cocrystal components | `"2:1"`, `"0.5:1"` |
| `name_drug` | string | Name of the drug in the cocrystal as cited in the text | `"Carvedilol"`, `"Epalrestat"` |
| `SMILES_drug` | string | Full SMILES representation of drug | |
| `name_coformer` | string | Name of the coformer in the cocrystal as cited in the text | `"Saccharin"`, `"Oxalic acid"` |
| `SMILES_coformer` | string | Full SMILES representation of coformer | |
| `photostability_change` | string | One of `"decrease"`, `"does not change"`, or `"increase"`. Trend of photostability for both the cocrystal and the drug | |

#### Extraction Rules

1. Extract **each** photostability mention as a separate object.

2. Do **not** filter, group, summarize, or deduplicate. Include repeated mentions and duplicates if they occur in different contexts.

3. If multiple polymorphic forms (e.g., CBZ-SAC Form I, CBZ-SAC Form II) appear for the same drug and coformer in the same ratio, extract each separately.

4. If you cannot find a required field for an object, re-check the context; if it's still absent, set that field's value to `"NOT_DETECTED"`.

5. The example output shows only two extracted samples, however your output should contain **all** mentions of photostability for co-crystals present in the article.

### Output Format

```json
[
  {
    "name_cocrystal": "CAR-HCT",
    "ratio_cocrystal": "2:1",
    "name_drug": "Carvedilol",
    "SMILES_drug": "C1=CC(=C(C=C1O)O)C=CC2=CC(=CC(=C2)O)O",
    "name_coformer": "Saccharin",
    "SMILES_coformer": "O=C(O)CC(O)C(=O)O",
    "photostability_change": "decrease"
  },
  {
    "name_cocrystal": "DMZ-SAC",
    "ratio_cocrystal": "0.5:1",
    "name_drug": "Epalrestat",
    "SMILES_drug": "C1=CC(=C(C=C1O)O)C=CC2=CC(=CC(=C2)O)O",
    "name_coformer": "Oxalic acid",
    "SMILES_coformer": "C(=C/C(=O)O)\\C(=O)O",
    "photostability_change": "does not change"
  }
]
```

---


## Complexes - Ga

### System Message
```python
{
    "description": "You are a domain-specific chemical information extraction assistant.",
    "instructions": "You specialize in the chemistry of organometallic complexes and their properties."
}
```

### Extraction Protocol

Your task is to extract **every** mention of organometallic complexes and chelate ligands from scientific article, and output a **JSON array** of objects **only** (no markdown, no commentary, no extra text).

#### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `compound_id` | string | ID of a complex within the article, as cited in the text | `"L3"`, `"A31"` |
| `compound_name` | string | Abbreviated or full name of the complex or ligand as cited in the text | `"DOTA"`, `"tebroxime"` |
| `SMILES` | string | Full SMILES representation of ligand environment or single ligand.<br>— If a complete organometallic complex is shown, extract all ligand structures **without mentioning the metal**.<br>— If only a chelate ligand is shown, extract **only its structure**. | |
| `SMILES_type` | string | One of `"ligand"` or `"environment"` | |
| `target_value` | number | The numeric value of logarithms of thermodynamic stability constants lgK or logK | |

**Note on SMILES format:**
- If a complete organometallic complex is shown, extract all ligand structures without mentioning the metal
- For a chelate ligand without a complete organometallic complex, extract only that ligand's structure

#### Extraction Rules

1. Extract **each** mention of `target_value` (lgK or logK) as a separate object.

2. Do **not** filter, group, summarize, or deduplicate. Include repeated mentions and duplicates if they occur in different contexts.

3. If a molecule is fully depicted in a figure, write it as a SMILES string. If a molecule is depicted as a scaffold and residues separately in different places of an article, connect them by compound ID or name into one molecule and write it a single SMILES string.

4. If multiple thermodynamic stability constants appear for the same complex or ligand extract each separately.

5. Extract only structures that comply with these rules:
   5.1. The complexes must contain **Ga** as the metal or the ligands must belong to complexes of that metal.
   5.2. The complete molecular structure shall be given without errors in it or identifiers.
   5.3. Compounds must contain more than one carbon (exclude CO, Me).
   5.4. Compounds must not contain polymeric structures, attached biomolecules or carboranes, undefined radicals, undeciphered designations (e.g., amino acids) beyond the simplest abbreviations (i.e., Me, Et, Pr, Bu, Ph, Ac), names of radicals instead of their structure, or incomplete indication of the ligand structure (e.g., L = P, N).
   5.5. Compounds must not be reaction intermediate or precursor.

6. If you cannot find a required field for an object, re-check the context; if it's still absent, set that field's value to `"NOT_DETECTED"`.

7. The example output shows only two extracted samples, however your output should contain **all** mentions of organometallic complexes and/or chelate ligands present in the article.

### Output Format

```json
[
    {
        "compound_id": "L3",
        "compound_name": "DOTA",
        "SMILES": "O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O",
        "SMILES_type": "ligand",
        "target": 21.3
    },
    {
        "compound_id": "A31",
        "compound_name": "tebroxime",
        "SMILES": "[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC",
        "SMILES_type": "environment",
        "target": 17.9
    }
]
```

---

## Complexes - Gd

### System Message
```python
{
    "description": "You are a domain-specific chemical information extraction assistant.",
    "instructions": "You specialize in the chemistry of organometallic complexes and their properties."
}
```

### Extraction Protocol

Your task is to extract **every** mention of organometallic complexes and chelate ligands from scientific article, and output a **JSON array** of objects **only** (no markdown, no commentary, no extra text).

#### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `compound_id` | string | ID of a complex within the article, as cited in the text | `"L3"`, `"A31"` |
| `compound_name` | string | Abbreviated or full name of the complex or ligand as cited in the text | `"DOTA"`, `"tebroxime"` |
| `SMILES` | string | Full SMILES representation of ligand environment or single ligand | See note below |
| `SMILES_type` | string | One of `"ligand"` or `"environment"` | |
| `target_value` | number | The numeric value of logarithms of thermodynamic stability constants lgK or logK | |

**Note on SMILES format:**
- If a complete organometallic complex is shown, extract all ligand structures without mentioning the metal (e.g., "COc1cc(C=CC([O-])CC([O-])CC([O-])C=Cc2ccc(O)c(OC)c2)ccc1O. [C-]#[O+].[C-]#[O+].[C-]#[O+].[OH-]")
- For a chelate ligand without a complete organometallic complex, extract only that ligand's structure (e.g., 'O=C(O)CN(CCN(CC(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O')

#### Extraction Rules

1. Extract **each** mention of `target_value` (lgK or logK) as a separate object.

2. Do **not** filter, group, summarize, or deduplicate. Include repeated mentions and duplicates if they occur in different contexts.

3. If a molecule is fully depicted in a figure, write it as a SMILES string. If a molecule is depicted as a scaffold and residues separately in different places of an article, connect them by compound ID or name into one molecule and write it a single SMILES string.

4. If multiple thermodynamic stability constants appear for the same complex or ligand extract each separately.

5. Extract only structures that comply with these rules:
   5.1. The complexes must contain **Gd** as the metal or the ligands must belong to complexes of that metal.
   5.2. The complete molecular structure shall be given without errors in it or identifiers.
   5.3. Compounds must contain more than one carbon (exclude CO, Me).
   5.4. Compounds must not contain polymeric structures, attached biomolecules or carboranes, undefined radicals, undeciphered designations (e.g., amino acids) beyond the simplest abbreviations (i.e., Me, Et, Pr, Bu, Ph, Ac), names of radicals instead of their structure, or incomplete indication of the ligand structure (e.g., L = P, N).
   5.5. Compounds must not be reaction intermediate or precursor.

6. If you cannot find a required field for an object, re-check the context; if it's still absent, set that field's value to `"NOT_DETECTED"`.

7. The example output shows only two extracted samples, however your output should contain **all** mentions of organometallic complexes and/or chelate ligands present in the article.

### Output Format

```json
[
    {
        "compound_id": "L3",
        "compound_name": "DOTA",
        "SMILES": "O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O",
        "SMILES_type": "ligand",
        "target": 21.3
    },
    {
        "compound_id": "A31",
        "compound_name": "tebroxime",
        "SMILES": "[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC",
        "SMILES_type": "environment",
        "target": 17.9
    }
]
```

---


## Complexes - Tc

### System Message
```python
{
    "description": "You are a domain-specific chemical information extraction assistant.",
    "instructions": "You specialize in the chemistry of organometallic complexes and their properties."
}
```

### Extraction Protocol

Your task is to extract **every** mention of organometallic complexes and chelate ligands from scientific article, and output a **JSON array** of objects **only** (no markdown, no commentary, no extra text).

#### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `compound_id` | string | ID of a complex within the article, as cited in the text | `"L3"`, `"A31"` |
| `compound_name` | string | Abbreviated or full name of the complex or ligand as cited in the text | `"DOTA"`, `"tebroxime"` |
| `SMILES` | string | Full SMILES representation of ligand environment or single ligand | See note below |
| `SMILES_type` | string | One of `"ligand"` or `"environment"` | |
| `target_value` | number | The numeric value of logarithms of thermodynamic stability constants lgK or logK | |

**Note on SMILES format:**
- If a complete organometallic complex is shown, extract all ligand structures without mentioning the metal (e.g., "COc1cc(C=CC([O-])CC([O-])CC([O-])C=Cc2ccc(O)c(OC)c2)ccc1O. [C-]#[O+].[C-]#[O+].[C-]#[O+].[OH-]")
- For a chelate ligand without a complete organometallic complex, extract only that ligand's structure (e.g., 'O=C(O)CN(CCN(CC(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O')

#### Extraction Rules

1. Extract **each** mention of `target_value` (lgK or logK) as a separate object.

2. Do **not** filter, group, summarize, or deduplicate. Include repeated mentions and duplicates if they occur in different contexts.

3. If a molecule is fully depicted in a figure, write it as a SMILES string. If a molecule is depicted as a scaffold and residues separately in different places of an article, connect them by compound ID or name into one molecule and write it a single SMILES string.

4. If multiple thermodynamic stability constants appear for the same complex or ligand extract each separately.

5. Extract only structures that comply with these rules:
   5.1. The complexes must contain **Tc** as the metal or the ligands must belong to complexes of that metal.
   5.2. The complete molecular structure shall be given without errors in it or identifiers.
   5.3. Compounds must contain more than one carbon (exclude CO, Me).
   5.4. Compounds must not contain polymeric structures, attached biomolecules or carboranes, undefined radicals, undeciphered designations (e.g., amino acids) beyond the simplest abbreviations (i.e., Me, Et, Pr, Bu, Ph, Ac), names of radicals instead of their structure, or incomplete indication of the ligand structure (e.g., L = P, N).
   5.5. Compounds must not be reaction intermediate or precursor.

6. If you cannot find a required field for an object, re-check the context; if it's still absent, set that field's value to `"NOT_DETECTED"`.

7. The example output shows only two extracted samples, however your output should contain **all** mentions of organometallic complexes and/or chelate ligands present in the article.

### Output Format

```json
[
    {
        "compound_id": "L3",
        "compound_name": "DOTA",
        "SMILES": "O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O",
        "SMILES_type": "ligand",
        "target": 21.3
    },
    {
        "compound_id": "A31",
        "compound_name": "tebroxime",
        "SMILES": "[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC",
        "SMILES_type": "environment",
        "target": 17.9
    }
]
```

---

## Complexes - Lu

### System Message
```python
{
    "description": "You are a domain-specific chemical information extraction assistant.",
    "instructions": "You specialize in the chemistry of organometallic complexes and their properties."
}
```

### Extraction Protocol

Your task is to extract **every** mention of organometallic complexes and chelate ligands from scientific article, and output a **JSON array** of objects **only** (no markdown, no commentary, no extra text).

#### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `compound_id` | string | ID of a complex within the article, as cited in the text | `"L3"`, `"A31"` |
| `compound_name` | string | Abbreviated or full name of the complex or ligand as cited in the text | `"DOTA"`, `"tebroxime"` |
| `SMILES` | string | Full SMILES representation of ligand environment or single ligand | See note below |
| `SMILES_type` | string | One of `"ligand"` or `"environment"` | |
| `target_value` | number | The numeric value of logarithms of thermodynamic stability constants lgK or logK | |

**Note on SMILES format:**
- If a complete organometallic complex is shown, extract all ligand structures without mentioning the metal (e.g., "COc1cc(C=CC([O-])CC([O-])CC([O-])C=Cc2ccc(O)c(OC)c2)ccc1O. [C-]#[O+].[C-]#[O+].[C-]#[O+].[OH-]")
- For a chelate ligand without a complete organometallic complex, extract only that ligand's structure (e.g., 'O=C(O)CN(CCN(CC(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O')

#### Extraction Rules

1. Extract **each** mention of `target_value` (lgK or logK) as a separate object.

2. Do **not** filter, group, summarize, or deduplicate. Include repeated mentions and duplicates if they occur in different contexts.

3. If a molecule is fully depicted in a figure, write it as a SMILES string. If a molecule is depicted as a scaffold and residues separately in different places of an article, connect them by compound ID or name into one molecule and write it a single SMILES string.

4. If multiple thermodynamic stability constants appear for the same complex or ligand extract each separately.

5. Extract only structures that comply with these rules:
   5.1. The complexes must contain **Lu** as the metal or the ligands must belong to complexes of that metal.
   5.2. The complete molecular structure shall be given without errors in it or identifiers.
   5.3. Compounds must contain more than one carbon (exclude CO, Me).
   5.4. Compounds must not contain polymeric structures, attached biomolecules or carboranes, undefined radicals, undeciphered designations (e.g., amino acids) beyond the simplest abbreviations (i.e., Me, Et, Pr, Bu, Ph, Ac), names of radicals instead of their structure, or incomplete indication of the ligand structure (e.g., L = P, N).
   5.5. Compounds must not be reaction intermediate or precursor.

6. If you cannot find a required field for an object, re-check the context; if it's still absent, set that field's value to `"NOT_DETECTED"`.

7. The example output shows only two extracted samples, however your output should contain **all** mentions of organometallic complexes and/or chelate ligands present in the article.

### Output Format

```json
[
    {
        "compound_id": "L3",
        "compound_name": "DOTA",
        "SMILES": "O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O",
        "SMILES_type": "ligand",
        "target": 21.3
    },
    {
        "compound_id": "A31",
        "compound_name": "tebroxime",
        "SMILES": "[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC.[C-]#[N+]CC(C)(C)OC",
        "SMILES_type": "environment",
        "target": 17.9
    }
]
```

---

## Nanozymes

### System Message
```python
{
    "description": "You are a domain-specific chemical information extraction assistant.",
    "instructions": "You specialize in nanozymes."
}
```

### Extraction Protocol

Your task is to extract **every** mention of experiments for **ALL** nanozymes from a scientific article and output a **JSON array** of objects **only** (no markdown, no commentary, no extra text).

#### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `formula` | string | Chemical formula of the nanozyme | "Fe3O4", "CuO" |
| `activity` | string | Catalytic activity type | "peroxidase", "oxidase", "catalase", "laccase" |
| `syngony` | string | Crystal unit of the nanozyme | "cubic", "hexagonal", "tetragonal", "monoclinic", "orthorhombic", "trigonal", "amorphous", "triclinic" |
| `length` | number | Length of nanozyme particle in nanometers | |
| `width` | number | Width of nanozyme particle in nanometers | |
| `depth` | number | Depth of nanozyme particle in nanometers | |
| `surface` | string | Surface molecule | "naked", "poly(ethylene oxide)" |
| `km_value` | number | Michaelis constant value | |
| `km_unit` | string | Unit for Michaelis constant | "mM" |
| `vmax_value` | number | Molar maximum reaction rate value | |
| `vmax_unit` | string | Unit for maximum reaction rate | "µmol/min", "mol/min" |
| `reaction_type` | string | Reaction type with substrate and co-substrate | "TMB + H2O2", "ABTS + H2O2" |
| `c_min` | number | Minimum substrate concentration (mM) | |
| `c_max` | number | Maximum substrate concentration (mM) | |
| `c_const` | number | Constant co-substrate concentration | |
| `c_const_unit` | string | Unit for co-substrate concentration | |
| `ccat_value` | number | Catalyst concentration in assays | |
| `ccat_unit` | string | Unit for catalyst concentration | |
| `ph` | number | pH level of experiments | |
| `temperature` | number | Temperature in Celsius | |

#### Extraction Rules

1. Extract **each** nanozyme mention as a separate object.

2. Do **not** filter, group, summarize, or deduplicate. Include repeated mentions and duplicates if they occur in different contexts.

3. If you cannot find a required field for an object, re-check the context; if it's still absent, set that field's value to `"NOT_DETECTED"`.

4. The example output shows only two extracted samples, however your output should contain **all** nanozymes present in the article.

### Output Format

```json
[
  {
    "formula": "Fe3O4",
    "activity": "peroxidase",
    "syngony": "cubic",
    "length": 10,
    "width": 10,
    "depth": 2.5,
    "surface": "naked",
    "km_value": 0.2,
    "km_unit": "mM",
    "vmax_value": 2.5,
    "vmax_unit": "µmol/min",
    "reaction_type": "TMB + H2O2",
    "c_min": 0.01,
    "c_max": 1.0,
    "c_const": 1.0,
    "c_const_unit": "mM",
    "ccat_value": 0.05,
    "ccat_unit": "mg/mL",
    "ph": 4.0,
    "temperature": 25
  },
  {
    "formula": "CeO2",
    "activity": "oxidase",
    "syngony": "cubic",
    "length": 5,
    "width": 5,
    "depth": 200,
    "surface": "poly(ethylene oxide)",
    "km_value": 54.05,
    "km_unit": "mM",
    "vmax_value": 7.88,
    "vmax_unit": "10-8 M s-1",
    "reaction_type": "TMB",
    "c_min": 0.02,
    "c_max": 0.8,
    "c_const": 800,
    "c_const_unit": "μM",
    "ccat_value": 0.02,
    "ccat_unit": "mg/mL",
    "ph": 5.5,
    "temperature": 37
  }
]
```

---

## Nanomag

### System Message
```python
{
    "description": "You are a domain-specific chemical information extraction assistant.",
    "instructions": "You specialize in nanomaterials characterization, specifically in magnetic nanoparticles and their physical properties."
}
```

### Extraction Protocol

Your task is to extract **every** mention of magnetic properties for **ALL** nanoparticles from a scientific article and output a **JSON array** of objects **only** (no markdown, no commentary, no extra text).

#### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| **Composition** |
| `name` | string | Material name | "BFO", "cobalt iron oxide" |
| `np_core` | string | Composition of material core | "Gd2O3", "Fe1Fe2O4" |
| `np_shell` | string | Composition of material shell | "chitosan", "Au1" |
| `core_shell_formula` | string | Combined core-shell formula | "Cr2O3-Co" |
| `np_shell_2` | string | First additional shell layer | "PEG-5000" |
| `np_shell_3` | string | Second additional shell layer | "Curcumin" |
| **Size Measurements** |
| `np_hydro_size` | number | Size from DLS (nm) | |
| `xrd_scherrer_size` | number | Crystal size from XRD (nm) | |
| `emic_size` | number | Size from electron microscopy (nm) | |
| **Crystal Structure** |
| `crystal_structure_core_shell` | string | Crystallographic structures | "hexagonal, cubic" |
| `space_group_core` | string | Space group of core | "fd-3m", "p4/mmm" |
| `space_group_shell` | string | Space group of shell | "fd-3m", "p4/mmm" |
| `xrd_crystallinity` | string | Crystallinity type | "crystalline", "amorphous" |
| **Magnetic Properties** |
| `squid_sat_mag` | number | Saturation magnetization (emu/g) | |
| `squid_rem_mag` | number | Remanent magnetization (emu/g) | |
| `exchange_bias_shift_Oe` | number | Exchange bias (Oe) | |
| `vertical_loop_shift_M_vsl_emu_g` | number | Vertical loop shift (emu/g) | |
| `hc_kOe` | number | Coercivity (Oe) | |
| **Measurement Conditions** |
| `squid_h_max` | number | Maximum magnetic field (kOe) | |
| `zfc_h_meas` | number | ZFC measurement field (kOe) | |
| `instrument` | string | Experimental instrument | "Quantum Design 7 T SQUID" |
| `fc_field_T` | number | FC field (Tesla) | |
| `squid_temperature` | number | SQUID temperature (K) | |
| `coercivity` | number | Coercivity (kOe) | |
| **Additional Properties** |
| `htherm_sar` | number | Specific absorption rate (W/g) | |
| `mri_r1` | number | MRI relaxation rate r1 (mM⁻¹·s⁻¹) | |
| `mri_r2` | number | MRI relaxation rate r2 (mM⁻¹·s⁻¹) | |
| `blocking_temperature_K` | number | Blocking temperature (K) | |
| `curie_temperature_K` | number | Curie temperature (K) | |

#### Extraction Rules

1. Extract **each** nanoparticle mention as a separate object.

2. Do **not** filter, group, summarize, or deduplicate. Include repeated mentions and duplicates if they occur in different contexts.

3. If you cannot find a required field for an object, re-check the context; if it's still absent, set that field's value to `"NOT_DETECTED"`.

4. Unit conversions for magnetic properties:
   - For coercivity/exchange bias: 1T = 1000 Oe, 1 mT = 10000 Oe, 1kOe = 1000 Oe
   - For magnetization measurements: 1 A·m²/kg = 1 emu/g, 1 μ₀M(T) = 0.01257 emu/g

5. Preserve signs for exchange bias and vertical loop shift (default to + if not specified).

6. Extract **all** magnetic nanoparticles present in the article.

### Output Format

```json
[
  {
    "name": "Bismuth Ferrite",
    "np_core": "BiFeO3",
    "np_shell": "chitosan",
    "core_shell_formula": "BiFeO3-chitosan",
    "np_shell_2": "PEG-5000",
    "np_shell_3": "Curcumin",
    "np_hydro_size": 120,
    "xrd_scherrer_size": 45,
    "emic_size": 50,
    "crystal_structure_core_shell": "rhombohedral, amorphous",
    "space_group_core": "R3c",
    "space_group_shell": "P2_1",
    "xrd_crystallinity": "partially crystalline",
    "squid_sat_mag": 40.5,
    "squid_rem_mag": 22.1,
    "exchange_bias_shift_Oe": 180,
    "vertical_loop_shift_M_vsl_emu_g": 5.6,
    "hc_kOe": 3.2,
    "squid_h_max": 5.0,
    "zfc_h_meas": 1.5,
    "instrument": "Quantum Design 7 T SQUID magnetometer",
    "fc_field_T": 0.1,
    "squid_temperature": 300,
    "coercivity": 3.5,
    "htherm_sar": 1.2,
    "mri_r1": 4.5,
    "mri_r2": 5.3,
    "blocking_temperature_K": 350,
    "curie_temperature_K": 800
  }
]
```

---

## Synergy

### System Message
```python
{
    "description": "You are a domain-specific chemical information extraction assistant.",
    "instructions": "You specialize in antimicrobial drug nanoparticle synergy."
}
```

### Extraction Protocol

Your task is to extract **every** mention of nanoparticle properties, drug details, and their synergistic antibacterial effects from a scientific article, and output a **JSON array** of objects **only**.

#### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| **Nanoparticle Properties** |
| `NP` | string | Nanoparticle name | "Ag", "Au" |
| `NP_synthesis` | string | Synthesis method | "chemical synthesis" |
| `NP_concentration_µg_ml` | number | Nanoparticle concentration | |
| `NP_size_min_nm` | number | Minimum particle size (nm) | |
| `NP_size_max_nm` | number | Maximum particle size (nm) | |
| `NP_size_avg_nm` | number | Average particle size (nm) | |
| `shape` | string | Particle morphology | "spherical", "rod-shaped" |
| `zeta_potential_mV` | number | Surface charge (mV) | |
| **Bacterial Information** |
| `bacteria` | string | Bacterial species | "Escherichia coli" |
| `strain` | string | Strain identifier | "ATCC 25922" |
| `MDR` | string | Multidrug resistance status | "Yes", "No" |
| **Drug Properties** |
| `drug` | string | Antibiotic name | "Ampicillin" |
| `drug_dose_µg_disk` | number | Drug dosage | |
| **Experimental Methods** |
| `method` | string | Assessment technique | "MIC", "disc_diffusion" |
| `time_hr` | number | Exposure duration (hours) | |
| **Activity Measurements** |
| `ZOI_drug_mm_or_MIC _µg_m` | number | Drug activity | |
| `error_ZOI_drug_mm_or_MIC_µg_ml` | number | Drug activity error | |
| `ZOI_NP_mm_or_MIC_np_µg_ml` | number | NP activity | |
| `error_ZOI_NP_mm_or_MIC_np_µg_ml` | number | NP activity error | |
| `ZOI_drug_NP_mm_or_MIC_drug_NP_µg_ml` | number | Combined activity | |
| `error_ZOI_drug_NP_mm_or_MIC_drug_NP_µg_ml` | number | Combined activity error | |
| **Synergy Metrics** |
| `fold_increase_in_antibacterial_activity` | number | Activity enhancement | |
| `FIC` | number | Fractional Inhibitory Concentration | |
| `effect` | string | Interaction type | "synergistic", "additive" |
| **Additional Parameters** |
| `coating_with_antimicrobial_peptide_polymers` | string | Surface modification | |
| `combined_MIC` | number | Combined MIC (µg/ml) | |
| `peptide_MIC` | number | Peptide MIC (µg/ml) | |
| `viability_%` | number | Bacterial survival (%) | |
| `viability_error` | number | Viability measurement error | |

#### Extraction Rules

1. Extract **each** nanoparticles mention as a separate object.

2. Do **not** filter, group, summarize, or deduplicate. Include repeated mentions and duplicates if they occur in different contexts.

3. If you cannot find a required field for an object, re-check the context; if it's still absent, set that field's value to `"NOT_DETECTED"`.

4. Extract **all** nanoparticles present in the article.

### Output Format

```json
[
  {
    "NP": "Ag",
    "bacteria": "Pseudomonas aeruginosa",
    "strain": "ATCC 27853",
    "NP_synthesis": "Green synthesis using Gloeophyllum striatum",
    "drug": "Ampicillin",
    "drug_dose_µg_disk": 16.0,
    "NP_concentration_µg_ml": 32.0,
    "NP_size_min_nm": 10.0,
    "NP_size_max_nm": 40.0,
    "NP_size_avg_nm": 20.0,
    "shape": "spherical",
    "method": "MIC",
    "ZOI_drug_mm_or_MIC _µg_ml": 16.0,
    "error_ZOI_drug_mm_or_MIC_µg_ml": 1.40,
    "ZOI_NP_mm_or_MIC_np_µg_ml": 32.0,
    "error_ZOI_NP_mm_or_MIC_np_µg_ml": 2.43,
    "ZOI_drug_NP_mm_or_MIC_drug_NP_µg_ml": 8.0,
    "error_ZOI_drug_NP_mm_or_MIC_drug_NP_µg_ml": 1.50,
    "fold_increase_in_antibacterial_activity": 2.0,
    "zeta_potential_mV": -34.0,
    "MDR": "R",
    "FIC": 0.5,
    "effect": "synergistic",
    "time_hr": 24.0,
    "coating_with_antimicrobial_peptide_polymers": "AP Lysozyme hen egg-white",
    "combined_MIC": 12,
    "peptide_MIC": 400,
    "viability_%": 87.0,
    "viability_error": 2.40
  }
]
```

---

## Seltox

### System Message
```python
{
    "description": "You are a domain-specific chemical information extraction assistant.",
    "instructions": "You specialize in antimicrobial nanoparticles."
}
```

### Extraction Protocol

Your task is to extract information for **ALL** antimicrobial nanoparticles from a scientific article and output a **JSON array** of objects **only** (no markdown, no commentary, no extra text).

#### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `np` | string | Nanoparticle name | "Ag", "Au", "ZnO" |
| `coating` | string | Surface coating/modification | "1" for coating, "0" for none |
| `bacteria` | string | Bacterial strain tested | "Escherichia coli", "Staphylococcus aureus" |
| `mdr` | number | Multidrug-resistant strain indicator | 1 (MDR), 0 (not MDR) |
| `strain` | string | Specific strain identifier | "ATCC 25922" |
| `np_synthesis` | string | Synthesis method | "green_synthesis", "chemical_synthesis" |
| `method` | string | Assay type | "MIC", "ZOI", "MBC", "MBEC" |
| `mic_np_µg_ml` | number | Minimum Inhibitory Concentration | μg/mL |
| `concentration` | number | Concentration for ZOI | μg/mL |
| `zoi_np_mm` | number | Zone of Inhibition | mm |
| `np_size_min_nm` | number | Minimum nanoparticle size | nm |
| `np_size_max_nm` | number | Maximum nanoparticle size | nm |
| `np_size_avg_nm` | number | Average nanoparticle size | nm |
| `shape` | string | Morphology | "spherical", "triangular" |
| `time_set_hours` | number | Experiment duration | hours |
| `zeta_potential_mV` | number | Surface charge | mV |
| `solvent_for_extract` | string | Solvent used in green synthesis | "water", "ethanol" |
| `temperature_for_extract_C` | number | Extract preparation temperature | °C |
| `duration_preparing_extract_min` | number | Extract preparation time | minutes |
| `precursor_of_np` | string | Chemical precursor | "AgNO3" |
| `concentration_of_precursor_mM` | number | Precursor concentration | mM |
| `hydrodynamic_diameter_nm` | number | Hydrodynamic size | nm |
| `ph_during_synthesis` | number | pH of synthesis solution | |

#### Extraction Rules

1. Extract solvents and precursors as strings without parsing into molecular components.

2. Extract **each** nanoparticle mention as a separate object.

3. Do **not** filter, group, summarize, or deduplicate. Include repeated mentions and duplicates if they occur in different contexts.

4. If you cannot find a required field for an object, re-check the context; if it's still absent, set that field's value to `"NOT_DETECTED"`.

5. The example output shows only two extracted samples, however your output should contain **all** nanoparticles present in the article.

### Output Format

```json
[
  {
    "np": "Ag",
    "coating": "0",
    "bacteria": "Enterococcus faecalis",
    "mdr": 0,
    "strain": "ATCC 29212",
    "np_synthesis": "Green synthesis using Ixora brachypoda",
    "method": "MIC",
    "mic_np_µg_ml": 32.0,
    "concentration": 10,
    "zoi_np_mm": 15,
    "np_size_min_nm": 10.0,
    "np_size_max_nm": 40.0,
    "np_size_avg_nm": 20.0,
    "shape": "spherical",
    "time_set_hours": 24,
    "zeta_potential_mV": -27.9,
    "solvent_for_extract": "water",
    "temperature_for_extract_C": 21.0,
    "duration_preparing_extract_min": 1440,
    "precursor_of_np": "AgNO3",
    "concentration_of_precursor_mM": 1.0,
    "hydrodynamic_diameter_nm": 55,
    "ph_during_synthesis": 8.5
  },
  {
    "np": "ZnO",
    "coating": "0",
    "bacteria": "Klebsiella pneumoniae",
    "mdr": 1,
    "strain": "K-36",
    "np_synthesis": "Green synthesis using Phyllanthus emblica",
    "method": "MIC",
    "mic_np_µg_ml": 6.25,
    "concentration": 64,
    "zoi_np_mm": 12,
    "np_size_min_nm": 20.0,
    "np_size_max_nm": 20.0,
    "np_size_avg_nm": 20.0,
    "shape": "spherical",
    "time_set_hours": 24.0,
    "zeta_potential_mV": -32,
    "solvent_for_extract": "methanol",
    "temperature_for_extract_C": 60,
    "duration_preparing_extract_min": 60,
    "precursor_of_np": "Zn(NO3).6.H2O",
    "concentration_of_precursor_mM": 10,
    "hydrodynamic_diameter_nm": 30,
    "ph_during_synthesis": 7.0
  }
]
```

---


## Cytotox

### System Message
```python
{
    "description": "You are a domain-specific chemical information extraction assistant.",
    "instructions": "You specialize in cytotoxic nanoparticles."
}
```

### Extraction Protocol

Your task is to extract information for **ALL** cytotoxic nanoparticles from a scientific article and output a **JSON array** of objects **only** (no markdown, no commentary, no extra text).

#### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| **Material Properties** |
| `material` | string | Nanoparticle composition | "SiO2", "Ag" |
| `shape` | string | Physical shape | "Sphere", "Rod" |
| `coat_functional_group` | string | Surface coating | "CTAB", "PEG" |
| `synthesis_method` | string | Synthesis method | "Precipitation", "Commercial" |
| `surface_charge` | string | Surface charge type | "Negative", "Neutral", "Positive" |
| **Size Measurements** |
| `core_nm` | number | Primary particle size (nm) | |
| `size_in_medium_nm` | number | Size in biological medium (nm) | |
| `hydrodynamic_nm` | number | Size with coatings (nm) | |
| **Surface Properties** |
| `potential_mv` | number | Surface charge (mV) | |
| `zeta_in_medium_mv` | number | Zeta potential in medium (mV) | |
| **Cell Parameters** |
| `no_of_cells_cells_well` | number | Cell density per well | |
| `human_animal` | string | Cell origin | "A" (Animal), "H" (Human) |
| `cell_source` | string | Species/organism | "Rat", "Human" |
| `cell_tissue` | string | Tissue origin | "Adrenal Gland", "Lung" |
| `cell_morphology` | string | Cell shape | "Irregular", "Epithelial" |
| `cell_age` | string | Developmental stage | "Adult", "Embryonic" |
| **Experimental Conditions** |
| `time_hr` | number | Exposure duration (hours) | |
| `concentration` | number | Material concentration | |
| `test` | string | Cytotoxicity assay | "MTT", "LDH" |
| `test_indicator` | string | Measured reagent | "TetrazoliumSalt" |
| `viability_%` | number | Cell viability percentage | |

#### Extraction Rules

1. For multiple values:
   - Prioritize TEM measurements for core_nm
   - Note concentration units from context
   - Extract viability as reported (>100% allowed)

2. Data priority:
   - Table data over text
   - Note assumptions for ambiguous data

3. Extract **each** nanoparticle mention as a separate object.

4. Do **not** filter, group, summarize, or deduplicate.

5. Use `"NOT_DETECTED"` for missing fields after recheck.

6. Include **all** nanoparticles from the article.

### Output Format

```json
[
  {
    "material": "SiO2",
    "shape": "Rod",
    "coat_functional_group": "PEG",
    "synthesis_method": "Precipitation",
    "surface_charge": "Negative",
    "core_nm": 20.0,
    "size_in_medium_nm": 25.0,
    "hydrodynamic_nm": 30.0,
    "potential_mv": -15.0,
    "zeta_in_medium_mv": -10.0,
    "no_of_cells_cells_well": 5000.0,
    "human_animal": "H",
    "cell_source": "Human",
    "cell_tissue": "Lung",
    "cell_morphology": "Epithelial",
    "cell_age": "Adult",
    "time_hr": 24.0,
    "concentration": 100.0,
    "test": "MTT",
    "test_indicator": "TetrazoliumSalt",
    "viability_%": 85.0
  },
  {
    "material": "Fe3O4",
    "shape": "Sphere",
    "coat_functional_group": "Dextran",
    "synthesis_method": "Thermal Decomposition",
    "surface_charge": "Positive",
    "core_nm": 10.0,
    "size_in_medium_nm": 15.0,
    "hydrodynamic_nm": 18.0,
    "potential_mv": -30.0,
    "zeta_in_medium_mv": -15.0,
    "no_of_cells_cells_well": 10000.0,
    "human_animal": "A",
    "cell_source": "Dog",
    "cell_tissue": "Kidney",
    "cell_morphology": "Epithelial",
    "cell_age": "Adult",
    "time_hr": 24.0,
    "concentration": 300.0,
    "test": "MTT",
    "test_indicator": "TetrazoliumSalt",
    "viability_%": 115.09
  }
]
```
