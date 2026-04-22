


lst = [
	[1, 2],
	[4, 5],
	[7, 8]
]


# [
# 	[1, 4, 7],
# 	[2, 5, 8]
# ]

def transpose(lst):
    columns = len(lst) #3
    rows = len(lst[0]) #2
    new_list = []
    for i in range(rows):
        new_list.append([])
        # for j in range(columns):

    print(new_list, sep= '\n')



# lst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transpose(lst)
#
# # [
# # 	[1, 4, 7],
# # 	[2, 5, 8],
# # 	[3, 6, 9]
# # ]

lst_2 = [
	[1, 2],
	[4, 5],
	[7, 8]
]
transpose(lst_2)


# [
# 	[1, 4, 7],
# 	[2, 5, 8]
# ]