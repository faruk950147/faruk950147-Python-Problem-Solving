# # Ternary Operator in Python 
# #ternary operator 3 part (condition, true, false)
# # variable = value_if_true if condition else value_if_false

# # a = 10
# # b = 20
# # print("a is greater than b" if a > b else "b is greater than a")

# number = 5
# result = "Even" if number % 2 == 0 else "Odd"
# print(result)
# a = 10
# b = 20
# max_value = a if a > b else b
# print(max_value)





# # Walrus Operator (:=) in Python

# # Walrus Operator Python 3.8 introduce 
# # assignment and condition check one line 
# # actual name : Assignment Expression Operator
# # name "Walrus" because it's sign := looks like Walrus (a sea animal) 😄
# # walrus operator :=
# # walrus operator is used to assign value to variable as a part of a larger expression
# # it is used in while loop

# a = 10
# while (a := a - 1) > 0:
#     print(a)
    
    
    
# mylist = [1,2,3,4,5,6,7,8,9,10]
# n = len(mylist)
# if n > 5:
#     print(f"List has {n} elements")

# if (n := len(mylist)) > 5:
#     print(f"List has {n} elements")


# #  Reading user input (without walrus):

# data = input("Enter something: ")
# while data != "quit":
#     print(f"You entered: {data}")
#     data = input("Enter something: ")
    
    
# #  Same code with Walrus Operator:

# while (data := input("Enter something: ")) != "quit":
#     print(f"You entered: {data}")


# Real-life Use Case Example:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Find first even number
for num in numbers:
    if (even := num % 2 == 0):
        print(f"First even number is: {num}")
        break