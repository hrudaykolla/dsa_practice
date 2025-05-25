def canConstruct(target, array, memo = None):
    memo ={} if memo is None else memo
    if target == '': return True
    if target in memo: return memo[target]
    
    for word in array:
        # print(target, word)
        if word in target:
            if target.index(word) == 0:
                sub_target = target[len(word):]
                if canConstruct(sub_target, array, memo):
                    memo[target] = True
                    return True
    memo[target] = False
    return False

print(canConstruct('skateboard', ['sk', 'ska', 'te', 'boar', 'bo', 'ard']))
print(canConstruct('skateboard', ['sk', 'ska', 'te', 'boar', 'bo', 'ar']))
print(canConstruct('hhhhhhhhhhhhhhhhhhhhhhhhhhhhkkkkkkkkkkkruday', ['h', 'hh', 'hhh', 'kkk', 'kk', 'ru','day']))