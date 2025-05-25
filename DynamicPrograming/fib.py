def fibonacci(num, memo = {1 : 1, 2 : 1}):
    if num in memo: return memo[num]
        
    memo[num] = fibonacci(num-1) + fibonacci(num-2)
    return memo[num]
    