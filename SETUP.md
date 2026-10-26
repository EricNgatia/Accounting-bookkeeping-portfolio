# Setup instructions

## Option A — Excel only

1. Download `accounting_bookkeeping_portfolio.xlsx`.
2. Open it with Microsoft Excel or LibreOffice Calc.
3. Enable formula recalculation if prompted.
4. Explore Dashboard, Sales, Collections, Expenses, Receivables, and Profit & Loss.

## Option B — Regenerate the report with Python

You need Python 3.10 or later.

### Windows PowerShell

```powershell
cd accounting-bookkeeping-portfolio
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python generate_report.py
```

### macOS / Linux

```bash
cd accounting-bookkeeping-portfolio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python generate_report.py
```

The script reads the fictional `data/sales.csv` and `data/expenses.csv` files and writes `reports/monthly_profit_and_loss.csv`.

## Before publishing to GitHub

- Review every file for names, emails, account numbers, client identifiers, and employer data.
- Do not upload the original macro-enabled workbook.
- Publish only the recreated sample workbook and fictional CSVs.
- In GitHub, create a **Public** repository named `accounting-bookkeeping-portfolio`, add a short description, and upload the contents of this project folder.
- Keep `README.md` at the repository root so employers see the project overview immediately.
