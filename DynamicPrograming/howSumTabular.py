def howSumTabular(target, array):
    how_sum_tab = [None]*(target+1)
    how_sum_tab[0] = []  #seed
    for value in range(target):
        if how_sum_tab[value] is not None:
            for number in array:
                if value+number <= target:
                    how_sum_tab[value+number] = how_sum_tab[value].copy()
                    how_sum_tab[value+number].append(number)
    # print(how_sum_tab)
    return how_sum_tab[target]

print(howSumTabular(7, [5,4,3,7])) #True
print(howSumTabular(300, [7,14])) #False