# Question 1
# Give an algorithm to solve this problem. Determine the asymptotic time and space complexity.
# https://leetcode.com/problems/unique-paths/

class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for j in range(m)] # initialize dp m*n array with 1s

        for i in range(1, m): # iterate through the rows
            for j in range(1, n): # iterate through the columns
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] # calculate the number of unique paths to each cell using the upper and left cells

        return dp[m - 1][n - 1] # return the number of unique paths to the bottom-right cell

# Time Complexity: O(m*n)
# This is because the algorithm iterates through embedded loops the size of m and n, representing the number of
# rows and columns in the grid.
# Space Complexity: O(m*n)
# This is because the algorithm creates a 2D array of size m*n to store the number of unique paths to each cell.

# Question 2
# Give an algorithm to solve this problem. Determine the asymptotic time and space complexity.
# https://leetcode.com/problems/coin-change-ii/

class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount + 1)] # initialize dp array of size amount + 1 with 0s
        dp[0] = 1 # set the number of ways to make change for 0 to 1

        for coin in coins: # iterate through each coin
            for i in range(coin, amount + 1): # iterate through the amount for each coin
                dp[i] += dp[i - coin] # calculate the number of ways to make change for each amount using the current coin

        return dp[amount] # return the number of ways to make change for the given amount

# Time Complexity: O(amount*len(coins))
# This is because the algorithm iterates through a nested loop of size amount and len(coins) to calculate the number
# of ways to make change for each amount.
# Space Complexity: O(amount)
# This is because the algorithm creates an array of size amount to store the number of ways to make change for each
# amount.