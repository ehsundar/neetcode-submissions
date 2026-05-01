class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = [[False for _ in s] for _ in s]
        return self.longest_palindrome(s, memo)

    def longest_palindrome(self, s, memo):
        long_i, long_j = 0, 0
        for n in range(1, len(s) + 1):
            for i in range(0, len(s) - n + 1):
                j = i + n

                if j - i <= 1:
                    memo[i][j - 1] = True
                    if memo[i][j - 1] and j - i > long_j - long_i:
                        long_i, long_j = i, j
                    continue
                if j - i == 2 or j - i == 3:
                    memo[i][j - 1] = s[i] == s[j - 1]
                    if memo[i][j - 1] and j - i > long_j - long_i:
                        long_i, long_j = i, j
                    continue

                memo[i][j - 1] = memo[i + 1][j - 2] and s[i] == s[j - 1]
                if memo[i][j - 1] and j - i > long_j - long_i:
                    long_i, long_j = i, j

        return s[long_i:long_j]
