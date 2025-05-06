# gpt-json2csv-dataset

Convert GPT-style instruction/output JSON to a clean question–answer CSV with Python & pandas.

## Features
- 💡 **Simple**: one-file script (`json2csv.py`) — no CLI boilerplate  
- 📝 **Keeps only what matters**: extracts `instruction` ➜ `question`, `output` ➜ `answer`  
- 🐼 **pandas-powered**: fast, reliable, supports large datasets  
- 📄 **UTF-8 CSV**: ready for spreadsheet apps or ML tooling

## Requirements
- Python 3.9 +
- pandas >= 1.5

You can install the dependency with:

```bash
pip install -r requirements.txt
# or
pip install pandas
