from typing import List, Optional

def bestSum(value: int, arr: List[int], memo: Optional[dict] = None) -> Optional[List[int]]:
    """
    Finds the shortest combination of numbers from `arr` that add up to exactly `value`.

    This function uses memoization to optimize recursive calls by storing intermediate results.

    Parameters:
    value (int): The target sum we want to achieve.
    arr (List[int]): A list of positive integers that can be used to sum to the target.
    memo (dict, optional): A dictionary to store previously computed results for specific values.
                           Defaults to None, which initializes an empty memo dict.

    Returns:
    Optional[List[int]]: The shortest combination of elements that add up to `value`, or
                         None if no combination exists.

    Example:
    >>> bestSum(7, [5, 3, 4, 7])
    [7]
    >>> bestSum(8, [2, 3, 5])
    [3, 5]
    >>> bestSum(7, [2, 4])
    None
    """
    memo = {} if memo is None else memo

    if value in memo:
        return memo[value]
    if value == 0:
        return []
    if value < 0:
        return None

    shortest_combination = None

    for num in arr:
        remainder = value - num
        remainder_result = bestSum(remainder, arr, memo)

        if remainder_result is not None:
            combination = remainder_result + [num]

            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    memo[value] = shortest_combination
    return shortest_combination


# Example usage
if __name__ == "__main__":
    print(bestSum(11, [1, 2, 3, 4, 5]))  
    print(bestSum(7, [5, 4, 3, 2, 1]))  # Output may vary: [2, 5], etc.
    # print(bestSum(300, [7, 14]))      # Will return None (efficiently due to memoization)
