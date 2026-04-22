def transpose(input_list):
    columns = len(input_list)  # number of rows in original = 3
    rows = len(input_list[0])  # number of columns in original = 2
    new_list = []

    for i in range(rows):  # i = 0, 1
        new_list.append([])
        for j in range(columns):  # j = 0, 1, 2
            new_list[i].append(input_list[j][i])

    print(new_list)

list_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# [ output
# 	[1, 4, 7],
# 	[2, 5, 8],
# 	[3, 6, 9]
# ]
transpose(list_1)

list_2 = [
	[1, 2],
	[4, 5],
	[7, 8]
]
# [ output
# 	[1, 4, 7],
# 	[2, 5, 8]
# ]
transpose(list_2)
