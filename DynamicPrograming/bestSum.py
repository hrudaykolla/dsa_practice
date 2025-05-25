def bestSum(value, arr, memo=None):
    memo = {} if memo is None else memo
    # print(memo)
    if value in memo: return memo[value]
    if value == 0: return []
    if value < 0: return None
    # if value < min(arr): return None

    short_array = None
    for i in arr:
        # print(value, i)
        remainder = value - i
        how = bestSum(remainder,arr,memo)
        if how != None:
            how.append(i)
            current_array = how
            if current_array:
                if short_array is None or len(current_array) < len(short_array):
                    short_array = current_array.copy()
    memo[value] = short_array.copy()
    return short_array
            

print(bestSum(7, [1,2,3,4,5]))
print(bestSum(7, [5,4,3,2,1]))
# print(bestSum(300,[7,14]))