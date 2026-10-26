"""Generate a simple monthly finance summary from fictional portfolio CSVs."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

sales = pd.read_csv(DATA / "sales.csv", parse_dates=["Date"])
expenses = pd.read_csv(DATA / "expenses.csv", parse_dates=["Date"])
sales["Month"] = sales["Date"].dt.to_period("M").astype(str)
expenses["Month"] = expenses["Date"].dt.to_period("M").astype(str)

revenue = sales.groupby("Month")["Invoice_Amount"].sum()
cost_of_sales = expenses[expenses["Category"].eq("Cost of Sales")].groupby("Month")["Amount"].sum()
total_expenses = expenses.groupby("Month")["Amount"].sum()

summary = pd.concat([revenue.rename("Sales_Revenue"),
                     cost_of_sales.rename("Cost_of_Sales"),
                     total_expenses.rename("Total_Expenses")], axis=1).fillna(0)
summary["Gross_Profit"] = summary["Sales_Revenue"] - summary["Cost_of_Sales"]
summary["Operating_Expenses"] = summary["Total_Expenses"] - summary["Cost_of_Sales"]
summary["Net_Profit_Before_Tax"] = summary["Sales_Revenue"] - summary["Total_Expenses"]
summary["Gross_Margin_Pct"] = summary["Gross_Profit"].div(summary["Sales_Revenue"]).fillna(0)
summary["Net_Margin_Pct"] = summary["Net_Profit_Before_Tax"].div(summary["Sales_Revenue"]).fillna(0)
summary.to_csv(REPORTS / "monthly_profit_and_loss.csv", float_format="%.2f")
print(summary.round(2).to_string())
