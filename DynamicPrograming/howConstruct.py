
def howConstruct(target, array, memo = None):
    memo ={} if memo is None else memo
    if target in memo: return memo[target]
    if target == '': return []

    for word in array:
        # print(target, word)
        if word in target and target.index(word) == 0:
            sub_target = target[len(word):]
            list = howConstruct(sub_target, array, memo)
            if list != None:
                memo[target] = [word,*list]
                return [word,*list]
    
    memo[target] = None
    return None

print(howConstruct('skateboard', ['ska', 'te', 'board']))
print(howConstruct('skateboard', ['sk', 'ska', 'te', 'boar', 'bo', 'ar']))
print(howConstruct('hhhhhhhhhhhhhhhhhhhhhhhhhhhhkkkkkkkkkkkruday', ['h', 'hh', 'hhh', 'kkk', 'kk', 'ru','day']))