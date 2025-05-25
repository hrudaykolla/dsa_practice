def lcs(X: str, Y: str, m: int, n: int) -> int:
    """
    Compute the length of the Longest Common Subsequence (LCS) between two strings.

    Parameters:
    X (str): First input string.
    Y (str): Second input string.
    m (int): Length of string X.
    n (int): Length of string Y.

    Returns:
    int: Length of the longest common subsequence between X and Y.

    A subsequence is a sequence that appears in the same relative order,
    but not necessarily contiguous. For example, "GTAB" is a subsequence
    of "AGGTAB".

    Example:
    >>> lcs("AGGTAB", "GXTXAYB", 6, 7)
    4
    """
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))

if __name__ == '__main__':
    S1 = "AGGTAB"
    S2 = "GXTXAYB"
    print(f"String 1: {S1}")
    print(f"String 2: {S2}")
    print("Length of LCS is", lcs(S1, S2, len(S1), len(S2)))

