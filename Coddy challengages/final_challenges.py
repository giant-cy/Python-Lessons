def whatToBuy(prices, quantities, restriction, names):
    if len(quantities) <= 0:
        return [[], 0]
    avg_quantity_price = (sum(quantities)/len(quantities)) * (sum(prices)/len(prices))
    construction_list = []
    removed_construction_counter = 0
    n = len(prices)
    for i in range(n):
        total_price_item  = prices[i] * quantities[i] / avg_quantity_price
        if total_price_item < restriction:
            construction_list.append(names[i])
        else:
            removed_construction_counter += 1
    return [sorted(construction_list), removed_construction_counter]


test_var = whatToBuy([5, 2, 9, 3, 1, 2, 9],
[1, 1, 1, 1, 6, 6, 6],
0.5,
['pencil', 'bottle', 'wallet', 'phone', 'toy', 'mouse', 'door'])

print(test_var)


test_var_2 = whatToBuy([],[], 0, [])
print(test_var_2)
