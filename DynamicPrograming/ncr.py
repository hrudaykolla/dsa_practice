import time

def nCrModp(n, r, p):
    """
    Compute nCr % p using a bottom-up dynamic programming approach.

    Args:
        n (int): total number of items
        r (int): number of items to choose
        p (int): modulo value

    Returns:
        int: value of nCr % p
    """
    if r > n - r:
        r = n - r
    C = [0 for _ in range(r+1)]
    C[0] = 1  # Base case: nC0 = 1
    for i in range(1, n + 1):
        for j in range(min(i, r), 0, -1):
            C[j] = (C[j] + C[j - 1]) % p  # Apply modulo here
    return C[r]

def nCrModpRec(n, r, p, memo=None):
    """
    Compute nCr % p using memoized recursion (inefficient for large n).

    Args:
        n (int): total number of items
        r (int): number of items to choose
        p (int): modulo value
        memo (dict): memoization dictionary

    Returns:
        int: value of nCr % p
    """
    if r > n - r:
        r = n - r
    if r == 0 or n == r:
        return 1
    if memo is None:
        memo = {}
    if (n, r) in memo:
        return memo[(n, r)]

    # Use Pascal's identity: nCr = (n-1)C(r) + (n-1)C(r-1)
    memo[(n, r)] = (nCrModpRec(n - 1, r - 1, p, memo) + nCrModpRec(n - 1, r, p, memo)) % p
    return memo[(n, r)]


n = 100
r = 5
p = 10**11  # 100000000000

start = time.time()
result_dp = nCrModp(n, r, p)
end = time.time()
print(f'Value of nCr % p using DP: {result_dp} (Time: {end - start:.6f}s)')

start = time.time()
result_rec = nCrModpRec(n, r, p)
end = time.time()
print(f'Value of nCr % p using Recursion: {result_rec} (Time: {end - start:.6f}s)')
