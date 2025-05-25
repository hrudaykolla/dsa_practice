def bestSumTabular(target, array):
    best_sum_tab = [None]*(target+1)
    best_sum_tab[0] = []  #seed
    for value in range(target):
        if best_sum_tab[value] is not None:
            for number in array:
                if value+number <= target:
                    if best_sum_tab[value+number] is None:
                        best_sum_tab[value+number] = best_sum_tab[value].copy()
                        best_sum_tab[value+number].append(number)
                    else:
                        temp = best_sum_tab[value].copy()
                        temp.append(number)
                        if len(temp) < len(best_sum_tab[value+number]):
                            best_sum_tab[value+number] = temp.cpoy()

    print(best_sum_tab)
    return best_sum_tab[target]

print(bestSumTabular(7, [5,4,3,7])) #True
print(bestSumTabular(8, [2,3,5])) #True
# print(bestSumTabular(300, [7,14])) #False