import json

# JSON data to string (triple quote)
data = [
    {
        "name": "Faruk",
        "age": 22,
        "gender": "Male"
    },
    {
        "name": "Braund, Mr. Owen Harris",
        "age": 22,
        "gender": "Male"
    }
]


# json.dumps() Python dictionary to JSON string

with open('L:/Python/Python Problem Solving/Python practice/json/file/data.json', 'w') as file:
    json.dump(data, file, indent=4)
    print("Data written to file successfully")

# json.loads() JSON string to Python dictionary 
# with open('L:/Python/Python Problem Solving/Python practice/json/file/data.json', 'r') as file:
#     data = json.load(file)
#     print(data)
