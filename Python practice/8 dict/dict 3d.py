products_3d = {
    "electronics": {
        1: {
            "status": 200,
            "title": "Ipad M-10",
            "price": 100000,
            "description": "Ipad M-10 is a great product"
        },
        2: {
            "status": 200,
            "title": "Ipad M-11",
            "price": 200000,
            "description": "Ipad M-11 is a great product"
        },
        3: {
            "status": 200,
            "title": "Ipad M-12",
            "price": 300000,
            "description": "Ipad M-12 is a great product"
        }
    }
}
print(products_3d)
print(products_3d['electronics'])
print(products_3d['electronics'][1])
print(products_3d['electronics'][1]['title'])
print(products_3d['electronics'][1]['price'])
print(products_3d['electronics'][1]['description'])
print(products_3d['electronics'][1]['status'])
print(type(products_3d))
print(type(products_3d['electronics']))
print(type(products_3d['electronics'][1]))
print(type(products_3d['electronics'][1]['price']))
print(type(products_3d['electronics'][1]['description']))
print(type(products_3d['electronics'][1]['status']))

products_3d['electronics'][1]['price'] = 150000
print(products_3d['electronics'][1]['price'])

products_3d['electronics'][1]['description'] = "Ipad M-11 is a great product"
print(products_3d['electronics'][1]['description'])

products_3d['electronics'][1]['status'] = 404
print(products_3d['electronics'][1]['status'])

products_3d['electronics'][1]['title'] = "Ipad M-11"
print(products_3d['electronics'][1]['title'])

products_3d['electronics'][1]['price'] = 250000
print(products_3d['electronics'][1]['price'])

products_3d['electronics'][1]['description'] = "Ipad M-11 is a great product"
print(products_3d['electronics'][1]['description'])

products_3d['electronics'][1]['status'] = 404
print(products_3d['electronics'][1]['status'])

