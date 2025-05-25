def canSumTabular(target, array):
    can_sum_tab = [False]*(target+1)
    can_sum_tab[0] = True  #seed
    for value in range(target):
        if can_sum_tab[value]:
            for number in array:
                if value+number <= target:
                    can_sum_tab[value+number] = True
    # print(can_sum_tab)
    return can_sum_tab[target]

print(canSumTabular(7, [5,4,3,7])) #True
print(canSumTabular(300, [7,14])) #False