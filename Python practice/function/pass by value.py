# change in original list and same memory location
# যখন কোনো ভ্যারিয়েবল function-এ পাঠানো হয় তার কপি (copy) পাঠানো হয়।
# মূল ভ্যারিয়েবল এর উপর কোনো প্রভাব পড়ে না।

def pass_by_value(x):
    print("before memory location:", x, id(x))
    # x = x + 1 # pass by value
    x += 1 # pass by value   
    print("Inside function:", x)
    print("after memory location:", x, id(x))
    return x    


a = 10
print("Before modification:", a, id(a))
pass_by_value(a)
print("After modification:", a, id(a))

# def change_value(x):
#     x = x + 10
    
#     print("Inside function:", x)
#     return x

# a = 5
# print("Before modification:", a, id(a))
# change_value(a)
# print("After modification:", a, id(a))
