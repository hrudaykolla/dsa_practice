import copy
def allConstructTabular(target, array):
    len_target = len(target)
    all_construct_tab = [[]] * (len_target+1)
    all_construct_tab[0] = [[]] #seed for empty string
    for i,tab in enumerate(all_construct_tab):
        for word in array:
            if word == target[i : i+len(word)]:
                for list in all_construct_tab[i]:
                    temp = copy.deepcopy(list)
                    temp.append(word)
                    temp2 = copy.deepcopy(all_construct_tab[i+len(word)])
                    temp2.append(temp)
                    all_construct_tab[i+len(word)] = copy.deepcopy(temp2)
    return all_construct_tab[len(target)]

print(allConstructTabular('purple',['p','purp','ur','le','purpl']))
print(allConstructTabular('abcdef', ['ab','abc','cd','def', 'cdef','ef']))
print(allConstructTabular('skateboard', ['s','k','sk', 'ska', 'te', 'boar', 'bo', 'ard']))
print(allConstructTabular('skateboard', ['sk', 'ska', 'te', 'boar', 'bo', 'ar']))
print(allConstructTabular('hhkkruday', ['h', 'hh', 'hhh', 'kkk', 'kk', 'ru','day']))