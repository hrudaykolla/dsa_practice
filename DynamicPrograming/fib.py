def fibonacci(num: int, memo: dict = {1: 1, 2: 1}) -> int:
    """
    Calculate the nth Fibonacci number using memoization (top-down dynamic programming).

    The Fibonacci sequence is defined as:
        F(1) = 1
        F(2) = 1
        F(n) = F(n-1) + F(n-2) for n > 2

    Parameters:
    num (int): The position in the Fibonacci sequence to compute. Must be a positive integer.
    memo (dict, optional): A dictionary used to store previously computed Fibonacci values
                           to avoid redundant calculations. Defaults to {1: 1, 2: 1}.

    Returns:
    int: The nth Fibonacci number.

    Example:
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(13)
    233
    """
    if num in memo:
        return memo[num]
        
    memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo)
    return memo[num]

if __name__ == "__main__":
    print(f"13th Fibonacci number is: {fibonacci(13)}")

    