import json

# Path to your JSON file
json_file_path = 'data.json'

# Load data from JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)
productName = input('Enter product name: ')
colour = input(f"please select colour of {productName} : ")
# for colour in data:

#     print(f"Selected colous is {data.colour}")
# if colour in data[productName]['colour'] for future expansion
if colour in data['colour']:
    print(f"The colour {colour} is available for {productName}.")
else:
    print(f"The colour {colour} is not available for {productName}.")
    