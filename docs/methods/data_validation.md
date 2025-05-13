## Validation Process

To validate data integrity, we applied a stratified manual validation procedure.

From each article included in a dataset, we randomly selected approximately 20% of entries and reviewed them manually against the original source materials — including PDFs, figures, and supplementary tables.  
At least one entry from each article was always validated, even if 20% resulted in less than one.

Errors were detected manually and could include:  
– typos or transcription mistakes,  
– structural inconsistencies (e.g. incorrect SMILES),  
– unit mismatches,  
– or curator-inferred values not explicitly stated in the article.

Rather than rigidly classifying errors, we distinguished between:  
**Generalizable errors** – repeated patterns across entries or articles  
**Isolated errors** – one-off mistakes specific to a single entry

If even one error was found in the sample from an article, we reviewed all remaining entries from that article, regardless of whether they were in the original sample.  
This helped us uncover patterns not visible during initial sampling and enabled corrections to scale beyond individual entries.

Even isolated errors could trigger broader review and improvements across the dataset if they indicated hidden patterns.

For generalizable issues, we formulated simple correction rules:
- which field was affected,
- how often it repeated,
- and the appropriate fix — such as structure replacement, unit normalization, or removal of speculative values.

All fixes and decisions were documented and shared with the dataset curators.  
Isolated issues were fixed individually.

**The "Eye Drops" and "Co-crystals" datasets were fully reviewed in their entirety due to their small size.**