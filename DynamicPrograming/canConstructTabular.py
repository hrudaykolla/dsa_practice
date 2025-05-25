def canConstructTabular(target, array):
    len_target = len(target)
    can_construct_tab = [False] * (len_target+1)
   
    can_construct_tab[0] = True #seed for empty string

    for i,tab in enumerate(can_construct_tab):
        if tab:
            for word in array:
                if word == target[i : i+len(word)]:
                    can_construct_tab[i+len(word)] = True
    print(can_construct_tab)
    return can_construct_tab[len(target)]

print(canConstructTabular('abcdef', ['ab','abc','cd','def']))