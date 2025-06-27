import os


file = open("L:\Python/Python Problem Solving/Python practice/13 filleHandle/dataFile/file1.txt", "w") 
file.write("Hello, World!")
file.close()

# file = open("L:\Python/Python Problem Solving/Python practice/13 filleHandle/dataFile/file1.txt", "r")
# print(file.read())
# file.close()

# file = open("L:\Python/Python Problem Solving/Python practice/13 filleHandle/dataFile/file1.txtt", "r+")
# print(file.read())
# file.write("Hello, Python!")
# file.seek(0)
# print(file.read())
# file.close()

# with open("L:\Python/Python Problem Solving/Python practice/13 filleHandle/dataFile/file1.txt", "r+") as file:
#     print(file.read())
#     file.write("Hello, World!")
#     file.seek(0)
#     print(file.read())