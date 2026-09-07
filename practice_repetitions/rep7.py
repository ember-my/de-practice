payments = [
    {"user": "Alice", "amount": "100"},
    {"user": "Bob", "amount": "50"},
    {"user": "Alice", "amount": "250"},
    {"user": None, "amount": "75"},           
    {"user": "Charlie", "amount": None},       
    {"user": "Bob", "amount": "free_promo"},   
    {"user": "Alice", "amount": "50"},
]

# 1. Initialize empty aggregation dictionary
user_totals = {}

# 2. Extract Values
for pay in payments:
    user = pay.get("user")
    raw_amount = pay.get("amount")

    # 3. Guard checker for missing values
    if user is None:
        print(f"Skipping record: missing required value user -> [{user}]")
        continue

    if raw_amount is None:
        print(f"Skipping [{user}]: missing amount value")
        continue

    # 4. Defensive convertion
    try:
        amount_num = int(raw_amount)
        print(f"Valid [{user}]: has an amount of [{amount_num}]")
    except ValueError:
        print(f"Skipping [{user}]: [{raw_amount}] is an invalid amount value")
        continue

    # 5 Count aggregation
    if user not in user_totals:
        user_totals[user] = amount_num
    else:
        user_totals[user] += amount_num

# 6. Print User Total Summary
print(f"\n User Total Summary:")
for user, count in user_totals.items():
    print(f"User {user:<10} -> Count {count}")
