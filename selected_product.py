import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)

productName = input('Enter the product name: ')
if productName in data['name']: 
    print(f'The product you selected colours avaiable {data['colour']}')
else : 
    print('Not in product list')

def export_selected_product_data():
    data = {colour: data['colour'], productName: data['name']}
    return data