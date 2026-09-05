users = [
    {"name": "Liam", "age": "21"},
    {"name": "Noah", "age": "unknown"},
    {"name": "Emma"},
    {"name": "Olivia", "age": "19"},
]

valid_users = []

for use in users:
    name = use.get("name")
    raw_age = use.get("age")

    # Guard Check for missing age number
    if raw_age is None:
        print(f"Skipping [{name}]: missing age")
        continue

    # Defensive Conversion to a valid users list
    try:
        age_num = int(raw_age)
        print(f"Verified [{name}]: [{age_num}] is a valid number ")
        valid_users.append({"name": name, "age": age_num})
    except ValueError:
        print(f"Skipping [{name}]: invalid age number [{raw_age}] ")

print(f"\nFinal Valid Users")
print(valid_users)
    