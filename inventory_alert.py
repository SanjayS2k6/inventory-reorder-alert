import csv
INPUT_FILE = "inventory.csv"
OUTPUT_FILE = "restock_report.csv"
restock_items = []
try:
    with open(INPUT_FILE, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                item = row["Item Name"].strip()
                qty = row["Current Quantity"].strip()
                threshold = row["Reorder Threshold"].strip()
                if qty == "" or threshold == "":
                    print(f"Skipping invalid row: {row}")
                    continue
                qty = int(qty)
                threshold = int(threshold)
                if threshold <= 0:
                    print(f"Invalid threshold for {item}")
                    continue

                # Check stock
                if qty < threshold:

                    if qty < threshold * 0.25:
                        priority = "Critical"
                    else:
                        priority = "Low"

                    # Suggested healthy stock = 2 × threshold
                    reorder_qty = (threshold * 2) - qty

                    restock_items.append({
                        "Item Name": item,
                        "Current Quantity": qty,
                        "Threshold": threshold,
                        "Priority": priority,
                        "Suggested Reorder": reorder_qty
                    })

            except (ValueError, KeyError):
                print(f"Malformed row skipped: {row}")

except FileNotFoundError:
    print("Inventory file not found.")
    exit()


print("\n========== RESTOCK REPORT ==========")

if not restock_items:
    print("All inventory levels are healthy.")
else:
    for item in restock_items:
        print(
            f"{item['Item Name']} | "
            f"Stock: {item['Current Quantity']} | "
            f"Threshold: {item['Threshold']} | "
            f"Priority: {item['Priority']} | "
            f"Reorder: {item['Suggested Reorder']}"
        )

with open(OUTPUT_FILE, mode="w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "Item Name",
            "Current Quantity",
            "Threshold",
            "Priority",
            "Suggested Reorder"
        ]
    )

    writer.writeheader()
    writer.writerows(restock_items)

print(f"\nReport exported to '{OUTPUT_FILE}'")
print("\n========== EMAIL ALERT ==========")

print("Subject: Inventory Restock Alert\n")

if restock_items:
    print("The following items require restocking:\n")

    for item in restock_items:
        print(
            f"- {item['Item Name']} "
            f"({item['Priority']}) "
            f"- Current Stock: {item['Current Quantity']}, "
            f"Suggested Reorder: {item['Suggested Reorder']}"
        )

else:
    print("No items require restocking today.")