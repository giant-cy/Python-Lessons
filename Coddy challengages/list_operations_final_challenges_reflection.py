def is_list_matrix(input_list):
    list_rows = len(input_list)
    list_columns = len(input_list[0])
    if list_rows != list_columns:
        return False
    for i in range(list_rows):
        for j in range(list_columns):
            if i != j and input_list[i][j] != 0:
                return False
    return True

D = [
    [5, 0, 0],
    [0, 8, 0],
    [0, 0, 3]
]
print(is_list_matrix(D))

D = [
    [5, 0, 1],
    [0, 8, 0],
    [0, 0, 3]
]
print(is_list_matrix(D))