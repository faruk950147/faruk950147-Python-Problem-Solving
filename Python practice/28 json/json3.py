import json 

products = {
    "products": [
        {
            "id": 1,
            "status": 200,
            "title": "Ipad M-10",
            "price": 100000,
            "description": "Ipad M-10 is a great product"
        },
        {
            "id": 2,
            "status": 200,
            "title": "Ipad M-10",
            "price": 100000,
            "description": "Ipad M-10 is a great product"
        }
    ]
}


with open('L:/Python/Python Problem Solving/Python practice/json/file/products.json', 'w') as file:    # json.dump() Python dictionary to JSON string
    json.dump(products, file, indent=4)
    print("Data written to file successfully")

with open('L:/Python/Python Problem Solving/Python practice/json/file/products.json', 'r') as file:    # json.load() JSON string to Python dictionary 
    products = json.load(file)
    print(f"Data read from file successfully: {products}")