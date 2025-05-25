def countSumTabular(target, array):
    count_sum_tab = [None]*(target+1)
    count_sum_tab[0] = 0  #seed
    for value in range(target):
        if count_sum_tab[value] is not None:
            for number in array:
                if value+number <= target:
                    if count_sum_tab[value+number] is None: count_sum_tab[value+number] = 1
                    else: count_sum_tab[value+number] += 1
    print(count_sum_tab)
    return count_sum_tab[target]

print(countSumTabular(7, [5,4,3,7])) #True
print(countSumTabular(8, [2,3,5])) #True
# print(countSumTabular(300, [7,14])) #False