# If a m,n size array is given, no of ways to travel from 1,1 to m,n if u can only move right and down
def gridTraveller(m,n, memo = {}):
    a = f'{m},{n}'
    b = f'{n},{m}'
    memo = {} if memo is None else memo
    if a in memo: return memo[a]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    
    memo[a] = gridTraveller(m-1,n,memo) + gridTraveller(m,n-1,memo)
    memo[b] = memo[a]
    return memo[a]

if __name__ == "__main__":
    print(gridTraveller(2,3))