import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
def sort_by_discounted_price():
    sorted_products = []
    for color in data["colour"]:
        color_key = f"{color}-tshirt" if f"{color}-tshirt" in data else color
        if color_key in data:
            product_info = data[color_key]
            sorted_products.append({
                "color": color,
                "discountedPrice": product_info["discountedPrice"],
                "originalPrice": product_info["originalPrice"]
            })

    # Sorting by discounted price
    sorted_products.sort(key=lambda x: x["discountedPrice"])
    return sorted_products

if __name__ == "__main__":
    sorted_products = sort_by_discounted_price()
    print("Products sorted by discounted price:", sorted_products)