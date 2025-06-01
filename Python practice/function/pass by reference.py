# no change in original list and same memory location
def pass_by_reference(lst):
    lst[0] = lst[0] + 1 # pass by reference
    return lst


a = [10]
print(pass_by_reference(a))
print(a)

def change_list(lst):
    lst.append(100)

my_list = [1, 2, 3]
change_list(my_list)
print(my_list)  # Output: [1, 2, 3, 100]
