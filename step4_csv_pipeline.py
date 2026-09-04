import csv

input_file = "customers.csv"

# Storage for the aggregated city counts
city_order_totals = {}

print("--- Processing Ingestion File ---")

with open(input_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cust_id = row.get("customer_id")
        name = row.get("name")
        city = row.get("city")
        raw_orders = row.get("total_orders")

        # Validation 1: Skip if required values are missing or blank
        if not city or not raw_orders:
            print(f"Skipping row {cust_id} ({name}): missing city or orders")
            continue

        # Validation 2: Defensive type casting
        try:
            orders = int(raw_orders)
        except ValueError:
            print(f"Skipping row {cust_id} ({name}): invalid order count '{raw_orders}'")
            continue

        # Validation 3: Business rule check (checks if orders <= 0)
        if orders <= 0:
            print(f"Skipping {cust_id} ({name}): non positive order count ({orders})")
            continue

        # In-memory aggregation: Sum total orders by City
        if city not in city_order_totals:
            city_order_totals[city] = orders
        else:
            city_order_totals[city] += orders

print("\n === Summary: Valid Orders by City ===")
for city, total in city_order_totals.items():
    print(f"City {city:<12} -> Total Orders: {total}")