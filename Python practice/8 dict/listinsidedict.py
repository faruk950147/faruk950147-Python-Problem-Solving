from typing import List, Dict

products: List[Dict[str, int]] = [
    {"id": 1, "price": 100},
    {"id": 2, "price": 150},
]

print(products)
print(products[1])
print(products[1]['price'])
print(type(products))
print(type(products[1]))
print(type(products[1]['price']))