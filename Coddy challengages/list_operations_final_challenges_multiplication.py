def list_multiplication(list1, list2):
    row_list_1 = len(list1)
    column_list_1 = len(list1[0])
    row_list_2 = len(list2)
    columns_list_2 = len(list2[0])
    result = []

    if column_list_1 != row_list_2:
        print("Matrix multiplication not possible")
        return result

    for i in range(row_list_1):
        result.append([])
        for j in range(columns_list_2):
            total = 0
            for k in range(column_list_1):
                total += list1[i][k] * list2[k][j]
            result[i].append(total)
    return result

list_1 = [
    [1 , 2],
    [3,4]
]

list_2 = [
    [5 , 6],
    [7,8]
]
print(list_multiplication(list_1,list_2))

list_1 = [
    [1, 2, 3],
    [4, 5, 6]
]
list_2 = [
    [7,  8],
    [9, 10],
    [11, 12]
]
print(list_multiplication(list_1,list_2))
