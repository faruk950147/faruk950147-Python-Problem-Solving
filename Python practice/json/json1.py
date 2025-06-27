import json
# dumps is used to write json data to a file
# loads is used to read json data from a file
person = {
    "name": "Faruk",
    "age": 22,
    "gender": "Male"
}
# data = json.dumps(person) # json.dumps() Python dictionary to JSON string
# print(data)
# print(type(data))

# parse json from file
# with open('person.json', 'w') as file: # json.dumps() Python dictionary to JSON string
#     json.dump(person, file)  

with open('data.json', 'r') as file:# json.loads() JSON string to Python dictionary 
    data = json.loads(file.read())  
    print(data)