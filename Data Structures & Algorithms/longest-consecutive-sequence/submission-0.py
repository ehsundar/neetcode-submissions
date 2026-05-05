class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return longest_consecutive(nums)


def longest_consecutive(nums: List[int]) -> int:
    freq = {}
    for n in nums:
        freq[n] = 1

    memo = {}

    def dfs(n):
        if n not in freq:
            return 0

        if n in memo:
            return memo[n]
        else:
            val = dfs(n + 1) + 1
            memo[n] = val
            return val

    mx = 0
    for n in nums:
        mx = max(mx, dfs(n))

    return mx
