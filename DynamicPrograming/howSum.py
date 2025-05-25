def howSum(value, arr, memo=None):
    memo = {} if memo is None else memo
    print(memo)
    if value in memo: return memo[value]
    if value == 0: return []
    if value < 0: return None
    if value < min(arr): return None

    for i in arr:
        print(value,i)
        remainder = value - i
        how =  howSum(remainder,arr,memo)
        if how != None:
            how.append(i)
            memo[value] = how
            return how
    memo[value] = None
    return None

print(howSum(7, [1,2,3]))
# print(howSum(300,[5,3]))