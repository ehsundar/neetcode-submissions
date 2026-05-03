class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        memo[m - 1][n - 1] = 1
        q = deque([(m - 1, n - 1)])

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue

                val_right = 0
                if j < n - 1:
                    val_right = memo[i][j + 1]

                val_bot = 0
                if i < m - 1:
                    val_bot = memo[i + 1][j]

                memo[i][j] = val_right + val_bot

        # while q:
        #     cur_m, cur_n = q.popleft()
        #     if memo[cur_m][cur_n] == -1:
        #         val_right = 0
        #         if cur_n < n - 1:
        #             val_right = memo[cur_m][cur_n + 1]

        #         val_bot = 0
        #         if cur_m < m - 1:
        #             val_bot = memo[cur_m + 1][cur_n]

        #         memo[cur_m][cur_n] = val_right + val_bot

        #     if cur_m > 0 and memo[cur_m - 1][cur_n] == -1:
        #         q.append((cur_m - 1, cur_n))
        #     if cur_n > 0 and memo[cur_m][cur_n - 1] == -1:
        #         q.append((cur_m, cur_n - 1))

        return memo[0][0]
