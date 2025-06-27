import json 

products = [
    {
        "id": 1,
        "status": 200,
        "title": "Ipad M-10",
        "price": 100000,
        "description": "Ipad M-10 is a great product"
    }
]

with open('data.json', 'w') as file:    # json.dump() Python dictionary to JSON string
    json.dump(products, file, indent=4)

# with open('data.json', 'r') as file:    # json.load() JSON string to Python dictionary 
#     data = json.load(file)
#     print(data)