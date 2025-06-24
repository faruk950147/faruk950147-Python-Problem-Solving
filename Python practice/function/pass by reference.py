# # no change in original list and same memory location
# pass by reference
# যখন ভ্যারিয়েবল function-এ পাঠানো হয় তার রেফারেন্স (মূল address) পাঠানো হয়।

# ফলে function এর ভেতর যা পরিবর্তন হয়, তা বাইরে মূল ভ্যারিয়েবলেও প্রভাব ফেলে।

# def pass_by_reference(x):
#     x[0] = 20
#     print("Inside function:", x, id(x))

# x = [10]  # mutable object (list)
# print("Before modification:", x, id(x))
# pass_by_reference(x)
# print("After modification:", x, id(x))

# def pass_by_reference(lst):
#     # lst[0] = lst[0] + 1
#     lst[0] += 1 # pass by reference
    
#     print("Inside function:", lst, id(lst))
#     return lst


# li = [10]
# print("Before modification:", li, id(li))
# pass_by_reference(li)
# print("After modification:", li, id(li))


def change_list(lst):
    lst.append(100)
    print("Inside function:", lst, id(lst))
    return lst

my_list = [1, 2, 3]
print("Before modification:", my_list, id(my_list))
change_list(my_list)
print("After modification:", my_list, id(my_list))  # Output: [1, 2, 3, 100]
