def countConstructTabular(target, array):
    len_target = len(target)
    count_construct_tab = [0] * (len_target+1)
    count_construct_tab[0] = 1 #seed for empty string
    for i,tab in enumerate(count_construct_tab):
            if tab != 0:
                for word in array:
                    if word == target[i : i+len(word)]: 
                        count_construct_tab[i+len(word)] = count_construct_tab[i]+count_construct_tab[i+len(word)]
    return count_construct_tab[len(target)]

print(countConstructTabular('purple',['purp','p','ur','le','purpl']))
print(countConstructTabular('abcdef', ['ab','abc','cd','def', 'cdef','ef']))
print(countConstructTabular('skateboard', ['s','k','sk', 'ska', 'te', 'boar', 'bo', 'ard']))
print(countConstructTabular('skateboard', ['sk', 'ska', 'te', 'boar', 'bo', 'ar']))
print(countConstructTabular('hhhhhhhhhhhhhhhhhhhhhhhhhhhhkkkkkkkkkkkruday', ['h', 'hh', 'hhh', 'kkk', 'kk', 'ru','day']))