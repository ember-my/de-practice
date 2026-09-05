employees = [ 
    {"name": "Mark", "badge_id": "1042"},
    {"name": "Sarah"},
    {"name": "John", "badge_id": "invalid"},
    {"name": "Ella", "badge_id": "2055"}
]

for emp in employees:
    name = emp.get("name")
    raw_badge = emp.get("badge_id")

    if raw_badge is None:
        print(f"Skipping {name}: missing badge ID")
        continue

    try:
        badge_num = int(raw_badge)
        print(f"Verified {name}: Badge #{badge_num}")
    except ValueError:
        print(f"Skipping {name}: Badge ID '{raw_badge}' is not a valid number")

        