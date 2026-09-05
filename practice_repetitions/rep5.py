products = [
    {"item": "Desk", "price": "150.5"},
    {"item": "Chair", "price": "discontinued"},
    {"item": "Lamp"},
    {"item": "Mat", "price": "25.0"},
]

clean_products = []

#Safe Getter
for prod in products:
    item = prod.get("item")
    raw_price = prod.get("price")

    #Guard Check for missing value
    if raw_price is None:
        print(f"Skipping [{item}]: missing price value")
        continue

    #Defensive Conversion
    try:
        price_amount = float(raw_price)
        print(f"Verified [{item}]: item have a price of [{price_amount}]")
        #Append to Clean List
        clean_products.append({"item": item, "price": price_amount})
    except ValueError:
        print(f"Skipping [{item}]: [{raw_price}] is an invalid price value")

print(f"\nFinal Clean Products:")
print(clean_products)