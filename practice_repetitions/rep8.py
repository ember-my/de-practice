import csv

# 1. Initialize aggregation dictionary
customer_totals = {}

# 2. Open CSV file safely
with open("orders.csv", mode="r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        # Extracting fields using .get()
        customer = row.get("customer")
        raw_total = row.get("order_total")

        # 3. Guard checks for None or empty strings
        # NOTE: This kind of guard check is for csv specific data files
        if not customer or customer.strip() == "":
            print(f"Skipping record: missing required customer -> [{customer}]")
            continue

        if not raw_total or raw_total.strip() == "":
            print(f"Skipping [{customer}]: missing order amount")
            continue

        # 4. Defensive conversion:
        try:
            total_num = int(raw_total)
            print(f"Verified [{customer}]: [{total_num}] total order/s")
        except ValueError:
            print(f"Skipping [{customer}]: invalid order value [{raw_total}]")
            continue

        # 5. Total Order Aggregation
        if customer not in customer_totals:
            customer_totals[customer] = total_num
        else:
            customer_totals[customer] += total_num

print(f"\n Total Order Summary:")
for customer, count in customer_totals.items():
    print(f"Customer {customer:<10} -> Count {count}")



