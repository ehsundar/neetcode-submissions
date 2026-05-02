class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        return self.coin_change(coins, amount, memo)

    def coin_change(self, coins, amount, memo):
        if amount in memo:
            return memo[amount]
        if amount < 0:
            memo[amount] = -1
            return -1
        if amount == 0:
            memo[amount] = 0
            return 0
        if amount in coins:
            memo[amount] = 1
            return 1

        nums = []
        for c in coins:
            n = self.coin_change(coins, amount - c, memo)
            if n >= 0:
                nums.append(n + 1)

        if nums:
            memo[amount] = min(nums)
        else:
            memo[amount] = -1

        return memo[amount]
