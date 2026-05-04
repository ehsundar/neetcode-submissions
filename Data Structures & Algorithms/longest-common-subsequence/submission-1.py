class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        if not m or not n:
            return 0

        tab = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    tab[i][j] = tab[i + 1][j + 1] + 1
                else:
                    tab[i][j] = max(tab[i][j + 1], tab[i + 1][j])

        return tab[0][0]

    def sol1(self, text1: str, text2: str):
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return dfs(i + 1, j + 1) + 1

            return max(dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)
