def transpose(input_list):
    columns = len(input_list)
    rows = len(input_list[0])
    new_list = []

    for i in range(rows):
        new_list.append([])
        for j in range(columns):
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


# first list
# [ output
# 	[1, 4, 7],
# 	[2, 5, 8],
# 	[3, 6, 9]
# ]

# first column
# [ output
# 	[1, 4, 7],
# 	[2, 5, 8],
# 	[3, 6, 9]
# ]