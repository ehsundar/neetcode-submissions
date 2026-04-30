class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.exists_tracking(board, word, [])

    def exists_tracking(self, board: List[List[str]], word: str, path) -> bool:
        if len(word) == 0:
            return True

        ch = word[0]
        search_set = []

        if not path:
            for i, row in enumerate(board):
                for j, char in enumerate(row):
                    if char == ch:
                        search_set.append((i, j))
        else:
            last_i, last_j = path[-1]

            if (
                last_i - 1 >= 0
                and board[last_i - 1][last_j] == ch
                and (last_i - 1, last_j) not in path
            ):
                search_set.append((last_i - 1, last_j))
            if (
                last_i + 1 < len(board)
                and board[last_i + 1][last_j] == ch
                and (last_i + 1, last_j) not in path
            ):
                search_set.append((last_i + 1, last_j))

            if (
                last_j - 1 >= 0
                and board[last_i][last_j - 1] == ch
                and (last_i, last_j - 1) not in path
            ):
                search_set.append((last_i, last_j - 1))
            if (
                last_j + 1 < len(board[last_i])
                and board[last_i][last_j + 1] == ch
                and (last_i, last_j + 1) not in path
            ):
                search_set.append((last_i, last_j + 1))

        for s in search_set:
            if self.exists_tracking(board, word[1:], [*path, s]):
                path.append(s)
                return True

        return False
