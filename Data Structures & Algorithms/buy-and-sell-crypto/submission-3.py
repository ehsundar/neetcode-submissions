
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buy = 0
        sell = 1
        prof = prices[sell] - prices[buy]

        for i in range(1, len(prices)):
            if prices[i] > prices[sell]:
                sell = i
            if prices[i] < prices[buy]:
                buy = i
                sell = i

            prof = max(prices[sell] - prices[buy], prof)

        return max(0, prof)

