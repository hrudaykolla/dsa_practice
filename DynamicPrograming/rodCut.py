# A recursive solution for Rod cutting problem

# Returns the best obtainable price for a rod of length n
# and price[] as prices of different pieces 
def cutRod(price_array, current_rod_size, memo = None):
	memo = {} if memo is None else memo
	if current_rod_size in memo: return memo[current_rod_size]
	if current_rod_size <= 0: return 0
	if current_rod_size == 1 : return price_array[0]
	price_comb = []
	for cut_len_index,price_per_len in enumerate(price_array):
		cut_len = cut_len_index + 1
		new_length = current_rod_size - cut_len
		if new_length >= 0:
		    price = price_per_len + cutRod(price_array[:(current_rod_size - cut_len+1)], current_rod_size - cut_len, memo)
		    price_comb.append(price)
	memo[current_rod_size] = max(price_comb)
	return max(price_comb)
		

# # Driver program to test above functions 
# arr = [3,5,8]
# size = len(arr)
# print(size)
# print("Maximum Obtainable Value is ",cutRod(arr, size))

#  Python program for above approach
 
 
def cutRodTabular(prices, n):
    mat = [[0 for i in range(n+1)]for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1:
                mat[i][j] = j*prices[i-1]
            else:
                if i > j:
                    mat[i][j] = mat[i-1][j]
                else:
                    mat[i][j] = max(prices[i-1]+mat[i][j-i], mat[i-1][j])
    return mat[n][n]
 
 
prices = [3, 5, 8, 9, 10, 17, 17, 20]
n = len(prices)
 
print("Maximum obtained value is ", cutRodTabular(prices, n))