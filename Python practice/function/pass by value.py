# change in original list and same memory location
def pass_by_value(x):
    x = x + 1 # pass by value
    return x    


a = 10
print(pass_by_value(a))
print(a)