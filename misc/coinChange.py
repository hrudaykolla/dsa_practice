import copy
class Solution:
    def allSum(self, coins, N, Sum, memo = None):
        memo = {} if memo is None else memo
        if Sum in memo: return memo[Sum]
        if Sum == 0:
            return [[]]
        elif Sum < 0:
            return None
        
        all_sum = []
        for coin in coins:
            how = self.allSum(coins, N, Sum-coin, memo)
            if how is not None:
                for h in how:
                    k = copy.deepcopy(h)
                    k.append(coin)
                    k.sort()
                    if k not in all_sum:
                        all_sum.append(k)
                
        memo[Sum] = all_sum
        # print(memo)
        return all_sum
        
    def count(self, coins, N, Sum):
        all_sum_list = self.allSum(coins, N, Sum, memo = None)
        if all_sum_list is not None: return len(all_sum_list)
        else: return 0

    def countTabular(self, coins, N, sum):
        # Creating a table with dimensions (sum+1) x (N)
        table = [[0 for x in range(N)] for x in range(sum+1)]
    
        # Initializing the first column of the table with 1's
        for i in range(N):
            table[0][i] = 1
    
        # Filling up the table with number of combinations
        for i in range(1, sum+1):
            for j in range(N):
                # Checking if using the current coin is possible
                x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0
                # Checking if not using the current coin is possible
                y = table[i][j-1] if j >= 1 else 0
                # Adding the number of combinations to the table
                table[i][j] = x + y
    
        # Returning the number of combinations for the given sum and coins
        return table[sum][N-1]
    
    
    def countRecursive(self, coins, N, sum, dp = None):
        if dp is None:
            dp = [[-1 for i in range(sum+1)] for j in range(N+1)]
        else:
            dp = dp
        # Base Case
        if (sum == 0):
            dp[N][sum] = 1
            return dp[N][sum]
    
        # If number of coins is 0 or sum is less than 0 then there is no way to make the sum.
        if (N == 0 or sum < 0):
            return 0
    
        # If the subproblem is previously calculated then simply return the result
        if (dp[N][sum] != -1):
            return dp[N][sum]
    
        # Two options for the current coin
        dp[N][sum] = self.countRecursive(coins,  N, sum - coins[N - 1], dp) + \
            self.countRecursive(coins, N - 1, sum, dp)
    
        return dp[N][sum]

x = Solution()
print(x.countRecursive([1,2,3], 3 , 4))