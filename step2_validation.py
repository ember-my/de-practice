orders = [
    {"order_id": 1, "customer": "Mark", "items": "4"},
    {"order_id": 2, "customer": "Sarah", "items": 0},
    {"order_id": 3, "customer": "John", "items": "two"},
    {"order_id": 4, "customer": "Ella"},
    {"order_id": 5, "customer": "Liam", "items": 12},
]

for row in orders:
    order_id = row.get("order_id")
    customer = row.get("customer")
    items_raw = row.get("items")

    # 1. Missing key check
    if items_raw is None:
        print(f"Order {order_id} ({customer}): missing item count")
        continue

    #3. Defensive conversion
    try:
        clean_amount = int(orders_items)

        if clean_amount <= 0:
            print(f"Skipping {row.get('customer')}: invalid negative or zero value ({clean_amount})")
            continue

        print(f"Valid: {row.get('customer')}: got {clean_amount: .2f}")

    except ValueError:
        print(f"Skipping {row.get('customer')}: could not convert '{orders_items}' to a number")

