events = [
    {"platform": "iOS", "event": "click"},
    {"platform": "Android", "event": "view"},
    {"platform": "iOS", "event": "click"},
    {"platform": None, "event": "scroll"},       # Missing platform
    {"platform": "Android", "event": None},        # Missing event
    {"platform": "Android", "event": "purchase"},
    {"platform": "iOS", "event": "click"},
    {"platform": "Web", "event": "view"},
]

# 1. Initialize empty aggregation dictionary
platform_counts = {}


for item in events:
    platform = item.get("platform")
    event = item.get("event")

    # 2. Guard Check for missing value
    if platform is None:
        print(f"Skipping record: missing required data -> platform {[platform]}")
        continue

    if event is None:
        print(f"Skipping [{platform}]: missing event action")
        continue

    # 3. Count Aggregation
    if platform not in platform_counts:
        platform_counts[platform] = 1
    else:
        platform_counts[platform] +=1

print(f"\n Final Platform Count:")
for platform, count in platform_counts.items():
    print(f"Platform {platform:<10} -> Count: {count}")