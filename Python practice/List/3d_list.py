list1 = [
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [10,11,12],
        [13,14,15],
        [16,17,18]
    ]
]
print(list1)
city = [
    [
        ['Dhaka','Chittagong','Khulna'],
        ['Rajshahi','Barisal','Sylhet']
    ],
    [
        ['Dhaka','Chittagong','Khulna'],
        ['Rajshahi','Barisal','Sylhet']
    ]
]
for i in range(len(list1)): # Block level
    for j in range(len(list1[i])): # Row level
        for k in range(len(list1[i][j])): # Column level
            print(list1[i][j][k], end=" ")
        print()
# for i in list1:
#     for j in i:
#         for k in j:
#             print(k, end=" ")
#         print()