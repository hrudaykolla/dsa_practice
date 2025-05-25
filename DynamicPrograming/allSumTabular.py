import copy
def allSumTabular(target, array):
    all_sum_tab = [None]*(target+1)
    all_sum_tab[0] = [[]]  #seed
    for value in range(target):
        if all_sum_tab[value] is not None:
            for number in array:
                if value+number <= target:
                    if all_sum_tab[value+number] is None:
                        temp = copy.deepcopy(all_sum_tab[value])
                        temp[0].append(number)
                        all_sum_tab[value+number] = copy.deepcopy(temp)
                    else:
                        for list in all_sum_tab[value]:
                            temp = copy.deepcopy(list)
                            temp.append(number)
                            all_sum_tab[value+number].append(temp)
    # print(all_sum_tab)
    return all_sum_tab[target]

print(allSumTabular(7, [5,4,3,7])) #True
print(allSumTabular(8, [2,3,5])) #True
# print(allSumTabular(300, [7,14])) #False