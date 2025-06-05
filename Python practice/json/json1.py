import json
# dump is used to write json data to a file
# loads is used to read json data from a file
person = {
    "name": "Faruk",
    "age": 22,
    "gender": "Male"
}
# data = json.dumps(person)
# print(data)
# print(type(data))

# parse json from file
# with open('person.json', 'w') as file:
#     json.dump(person, file)    

with open('person.json', 'r') as file:
    data = json.load(file)
    print(data)
    print(type(data))