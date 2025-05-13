# Benchmarking

---

## General Concept

Benchmarking in the **ChemX** project is aimed at evaluating the performance of automated systems for extracting chemical information from scientific literature.

The evaluation compares different approaches and types of models, including:

- large language models (**LLMs**),
- multimodal systems,
- multi-agent systems.

The goal is to identify the strengths and weaknesses of existing tools and methodologies, and to obtain practical insights into the capabilities of current models for chemical data extraction.

---

## Methodology

The benchmarking covers a wide range of chemical domains, including nanomaterials and small molecules. Experiments were conducted in two key evaluation settings:

### Mono-agent (single models)

Individual language models such as **GPT-4o** and **LLaMA-4** were evaluated independently. The models processed input in PDF and JPEG formats and were tasked with extracting chemical information, including:

- chemical entity recognition,
- relation and property extraction,
- construction of property–value pairs.

### Multi-agent (agent-based workflows)

For more complex tasks, the **NanoMINER** system was used, involving multiple specialized agents. Specifically:

- a YOLO-based agent was used for extracting information from images,
- a GPT-4o-based agent was used for text-based entity recognition.

This approach is designed for handling multimodal documents that include textual descriptions, tables, and figures.

---

## Benchmarking Tasks

The evaluation covers the following types of extraction tasks:

- **Entity Recognition** — extracting chemical entities such as compounds, materials, properties;
- **Property–Value Extraction** — extracting property–value pairs from scientific text;
- **Figure–Text Linking** — linking visual elements (figures) with their corresponding textual descriptions.

---

## Evaluation Metrics

To measure the quality of extracted information, the following metrics were used:

- **Precision** — the proportion of correctly extracted elements out of all predicted elements.
- **Recall** — the proportion of correctly extracted elements out of all relevant (ground truth) elements.
- **F1 Score** — the harmonic mean of precision and recall.
- **Error Rate** — the number of errors in extraction; lower values indicate better performance.
- **Task-Specific Metrics** — additional metrics used in multimodal tasks, such as the accuracy of text–figure linking.

These metrics allow for a comprehensive assessment of the reliability of LLM-based and agent-based systems when working with complex chemical documents.

---

## Experiment Results

The results showed that:

- **GPT-4o** and **LLaMA-4** demonstrated high precision and recall in text-based tasks, especially for chemical entity recognition.

- However, these models showed reduced performance when processing multimodal data, such as linking figures to their textual context.

- The **NanoMINER** system, which follows a multi-agent architecture, performed better in multimodal tasks, particularly in linking figures to corresponding textual segments and extracting data from figure content.

---

## Code Example: Column-wise Metric Calculation

Below is the code used to compute precision, recall, and F1 score for each column individually:

```python
def calc_metrics(
    df_true: pd.DataFrame,
    df_pred: pd.DataFrame
) -> pd.DataFrame:
    
    metrics = {}
    from copy import deepcopy
    for col in df_true.columns:
        if col == "pdf": continue
        true_values = list(df_true[col].astype(str).values)
        pred_values = list(df_pred[col].astype(str).values)

        tv = deepcopy(true_values)
        pv = deepcopy(pred_values)
        tp = 0

        for val in tv:
            if val in pv:
                pv.pop(pv.index(val))
                tp += 1

        fp = 0
        tv = deepcopy(true_values)
        pv = deepcopy(pred_values)

        for val in pv:
            if val in tv:
                tv.pop(tv.index(val))
            else:
                fp += 1

        fn = 0
        tv = deepcopy(true_values)
        pv = deepcopy(pred_values)

        for val in tv:
            if val in pv:
                pv.pop(pv.index(val))
            else:
                fn += 1

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

        metrics[col] = {
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "precision": precision,
            "recall": recall,
            "f1": f1
        }
    return pd.DataFrame(metrics).T
```