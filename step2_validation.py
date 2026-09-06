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

    # 2. Defensive conversion & boundary check
    try:
        item_count = int(items_raw)

        if item_count <= 0:
            print(f"Order {order_id} ({customer}): items must be greater than 0 ({item_count})")
            continue

        print(f"VALID: Order {order_id} for {customer}: {item_count} items confirmed")

    except ValueError:
        print(f"Order {order_id} ({customer}): invalid item format ('{items_raw}')")