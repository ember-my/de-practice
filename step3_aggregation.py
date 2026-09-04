logs = [
    {"service": "auth", "status": 200},
    {"service": "payment", "status": 500},
    {"service": "auth", "status": 404},
    {"service": "auth", "status": "200"},
    {"service": "payment", "status": "failed"},   # Corrupt status
    {"service": "search"},                        # Missing status key entirely
    {"service": "payment", "status": 200},
    {"service": "payment", "status": 500},
]

service_error_counts = {}

for entry in logs:
    service = entry.get("service")
    raw_status = entry.get("status")

    # 1. Skipping services or status that has missing keys
    if service is None or raw_status is None:
        continue

    # 2. Converting status to integers only
    try:
        status_code = int(raw_status)
    except ValueError:
        # skips strings or values aside the asigned
        continue

    # 3. Checks if the status code gives an error (>= 400)
    if status_code >= 400:
        if service not in service_error_counts:
            service_error_counts[service] = 1
        else:
            service_error_counts[service] += 1

# 4 Displays output
print("--- Error Summary by Service ---")
for service, count in service_error_counts.items():
    print(f"Service: {service} -> {count} errors" )



