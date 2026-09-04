# 1. A sample list of transactions
data = [
    {"name": "Alice", "points": 10},
    {"name": "Bob", "points": 25},
    {"name": "Charlie", "points": 5}
]

# 2. Looker at each row one by one
for row in data:
    person = row["name"]
    score = row["points"]
    print(f"Player: {person} has {score} points")