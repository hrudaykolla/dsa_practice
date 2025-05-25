def countConstruct(target, array, memo = None):
    memo ={} if memo is None else memo
    if target in memo: return memo[target]
    if target == '': return 1
    
    
    count = 0
    for word in array:
        # print(target, word)
        if word in target and target.index(word) == 0:
            sub_target = target[len(word):]
            count += countConstruct(sub_target, array, memo)

    memo[target] = count
    return count

print(countConstruct('skateboard', ['s','ka','sk', 'ska', 'te', 'boar', 'bo', 'ard']))
print(countConstruct('skateboard', ['sk', 'ska', 'te', 'boar', 'bo', 'ar']))
print(countConstruct('hhhhhhhhhhhhhhhhhhhhhhhhhhhhkkkkkkkkkkkruday', ['h', 'hh', 'hhh', 'kkk', 'kk', 'ru','day']))