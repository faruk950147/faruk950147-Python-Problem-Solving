import json

# JSON data to string (triple quote)
data = {
    "people": [
        {
            "Name": "Faruk",
            "Age": 22,
            "Gender": "Male"
        },
        {
            "Name": "Braund, Mr. Owen Harris",
            "Age": 22,
            "Gender": "Male"
        }
    ]
}



# json.dumps() Python dictionary to JSON string
json_data = json.dumps(data, indent=4)

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# json.loads() JSON string to Python dictionary 
