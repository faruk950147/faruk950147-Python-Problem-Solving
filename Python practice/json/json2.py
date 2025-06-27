import json 

product = {
    "product": [
        {
            "id": 1,
            "status": 200,
            "title": "Ipad M-10",
            "price": 100000,
            "description": "Ipad M-10 is a great product"
        }
    ]
}

with open('data.json', 'w') as file:
    json.dump(product, file, indent=4)