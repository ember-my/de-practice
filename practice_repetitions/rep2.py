transactions = [
    {"user": "Alice", "amount": "250"},
    {"user": "Bob", "amount": "free"},
    {"user": "Charlie"},
    {"user": "Diana", "amount": "1200"}
]


for tran in transactions:
    user = tran.get("user")
    raw_amount = tran.get("amount")

    # 1. Guard Check
    if raw_amount is None:
        print(f"Skipping [{user}]: missing amount")
        continue

    try:
        amount_num = int(raw_amount)
        print(f"Valid [{user}]: '[{amount_num}]' is a valid amount")
    except ValueError:
        print(f"Skipping [{user}]: invalid amount '[{raw_amount}]' ")
        