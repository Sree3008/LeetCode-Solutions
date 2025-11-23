class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            new_dp = dp[:]  # copy current state
            for r in range(3):
                new_dp[(r + num) % 3] = max(new_dp[(r + num) % 3], dp[r] + num)
            dp = new_dp
        
        return dp[0]

