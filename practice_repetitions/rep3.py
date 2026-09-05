inventory = [
    {"item": "Keyboard", "stock": "15"},
    {"item": "Mouse", "stock": "out_of_stock"},
    {"item": "Monitor"},
    {"item": "Headset", "stock": "8"},
]

clean_records = []

#1 Safe Getter
for inv in inventory:
    item = inv.get("item")
    raw_stock = inv.get("stock")

    #2 Guard Check for missing stock
    if raw_stock is None:
        print(f"Skipping [{item}]: stock not listed")
        continue

    #3. Defensive Conversion
    try:
        item_num = int(raw_stock)
        print(f"Verified [{item}]: [{item_num}] units available")
        clean_records.append({"item": item, "stock": item_num})
    except ValueError:
        print(f"Skipping [{item}]: invalid stock count [{raw_stock}]")

print("\nFinal Clean Records:")
print(clean_records)