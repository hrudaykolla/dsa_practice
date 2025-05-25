
def allConstruct(target, array, memo = None):
    memo ={} if memo is None else memo
    if target == '': return [[]]
    
    all = []
    for word in array:
        # print(target, word)
        if word in target and target.index(word) == 0:
            sub_target = target[len(word):]
            list = allConstruct(sub_target, array, memo)
            if list != None:
                list = [[word,*sub_list] for sub_list in list]
                all =[*all,*list]
    memo[target] = all
    return all

print(allConstruct('abac', ['ab','a', 'b','c','ac']))
print(allConstruct('skateboard', ['sk', 'ska', 'te', 'boar', 'bo', 'ar']))
print(allConstruct('hhhhhhhkkkkkkkkkkkruday', ['h', 'hh','k' ,'kkk', 'ru','day']))