# Inventory Reorder Alert
## Description
This project reads inventory data from a CSV file and checks which items need to be restocked. It generates a restock report and exports the results to a new CSV file.
## Features
- Read inventory data from CSV
- Check stock against reorder threshold
- Mark items as Low or Critical
- Suggest reorder quantity
- Export restock report to CSV
- Print a simulated email alert
## Files
- `inventory_alert.py` - Main Python script
- `inventory.csv` - Input inventory data
- `restock_report.csv` - Generated report
## How to Run
```bash
python inventory_alert.py
```
## Output
The program:
- Displays the restock report in the terminal.
- Creates a `restock_report.csv` file with items that need restocking.
