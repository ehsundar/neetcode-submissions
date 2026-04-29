class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        current_set = set()

        for row in board:
            current_set = set()
            for v in row:
                if v == ".":
                    continue
                if v in current_set:
                    return False
                current_set.add(v)

        for j in range(len(board)):
            current_set = set()
            for i in range(len(board)):
                v = board[i][j]
                if v == ".":
                    continue
                if v in current_set:
                    return False
                current_set.add(v)

        for i in range(3):
            for j in range(3):
                current_set = set()
                for ii in range(3):
                    for jj in range(3):
                        v = board[i*3+ii][j*3+jj]
                        if v == ".":
                            continue
                        if v in current_set:
                            return False
                        current_set.add(v)

        return True
