# Question 1
# Give an algorithm to solve this problem. Determine the asymptotic time and space complexity.
# https://leetcode.com/problems/unique-paths/

class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for j in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

# Question 2
# Give an algorithm to solve this problem. Determine the asymptotic time and space complexity.
# https://leetcode.com/problems/coin-change-ii/

class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount+1)]
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]

        return dp[amount]

# Time Complexity: O(amount*len(coins))
# Space Complexity: O(amount)