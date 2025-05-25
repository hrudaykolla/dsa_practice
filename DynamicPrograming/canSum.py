
def canSum(value, arr, memo = None):
    memo = {} if memo is None else memo
    if value in memo: return memo[value]
    if value == 0: return True
    if value < 0: return False
    if value < min(arr): return False

    for i in arr:
        remainder = value - i
        if canSum(remainder, arr, memo):
            memo[value] = True
            return True
          
    memo[value] = False
    return False

if __name__ == "__main__":
    print(canSum(7, [5,3,4,7])) #true and two ways
    print(canSum(300, [7,14])) #False