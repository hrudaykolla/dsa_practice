def allConstruct(target, array, memo=None):
    """
    allConstruct(target, array)
    -------------------------------------
    Task:
    Given a target string and an array of strings (word bank), return **all possible combinations**
    of elements from the array that can be concatenated to form the target string.
    Each element of the word bank can be used as many times as needed.

    This function uses recursion with memoization (top-down dynamic programming)
    to avoid redundant computations of the same sub-targets.

    Parameters:
    - target (str): The target string to construct.
    - array (List[str]): A list of words (strings) that can be used to build the target.
    - memo (dict): A dictionary to cache results of sub-targets (default is None).

    Returns:
    - List[List[str]]: A list of lists, where each inner list is a valid combination of words
      from the array that constructs the target.
    """
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == '':
        return [[]]  # Base case: one way to construct the empty string

    all_ways = []

    for word in array:
        # Check if the word is a prefix of the target
        if target.startswith(word):
            suffix = target[len(word):]
            # Recursively get all ways to construct the suffix
            suffix_ways = allConstruct(suffix, array, memo)
            # Prepend the current word to each combination from the suffix
            target_ways = [[word, *way] for way in suffix_ways]
            all_ways.extend(target_ways)

    # Store the result in memo before returning
    memo[target] = all_ways
    return all_ways


# Example test cases
print(allConstruct('abac', ['ab', 'a', 'b', 'c', 'ac']))
print(allConstruct('skateboard', ['sk', 'ska', 'te', 'boar', 'bo', 'ar']))
