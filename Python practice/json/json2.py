import json

# JSON data to string (triple quote)
json_data = '''
{
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
'''

# json.loads() JSON string to Python dictionary 
data = json.loads(json_data)

# print data
print(data)
