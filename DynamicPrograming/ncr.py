# Returns nCr % p
def nCrModp(n, r, p):
	#if r is very big we can calculate ncn-r
    if n-r < r:
        r = n-r
    # a list of C, 1row and r+1 columns
    C = [0 for i in range(r+1)]

    #make element 1 equal to 1, since nc0 is 1 for any r
    C[0] = 1

    for i in range(1,n+1):
        for j in range(min(i,r),0,-1):
            #current element = previous row current j + previous row current j-1
            C[j] = C[j]+C[j-1]
        
    return C[r]
        

def nCrModpRec(n, r, p, memo = None):
    if r > n-r:
        r = n-r
    memo = {} if memo is None else memo
    if r in memo: return memo[r]
    if r == 0: return 1
    memo[r] = nCrModpRec(n, r-1, p, memo)*((n-r+1)/r)
    return nCrModpRec(n, r-1, p, memo)*((n-r+1)/r)
    

	# return C[r]

# Driver Program
n = 100
r = 5
p = 100000000000
print('Value of nCr % p is', nCrModp(n, r, p))
print('Value of nCr % p is', nCrModpRec(n, r, p))