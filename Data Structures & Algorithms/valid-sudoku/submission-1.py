class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {} # Map: board num -> set
        rows = {}
        cols = {}
        for i in range(9):
            seen[i] = set()
            rows[i] = set()
            cols[i] = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(i, j)
                if board[i][j] != ".":
                    if board[i][j] in rows[i] or board[i][j] in cols[j]:
                        return False
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    if i < 3:
                        if j < 3:
                            if board[i][j] in seen[0]:
                                return False
                            seen[0].add(board[i][j])
                        elif j < 6:
                            if board[i][j] in seen[1]:
                                return False
                            seen[1].add(board[i][j])
                        else:
                            if board[i][j] in seen[2]:
                                return False
                            seen[2].add(board[i][j])
                    elif i < 6:
                        if j < 3:
                            if board[i][j] in seen[3]:
                                return False
                            seen[3].add(board[i][j])
                        elif j < 6:
                            if board[i][j] in seen[4]:
                                return False
                            seen[4].add(board[i][j])
                        else:
                            if board[i][j] in seen[5]:
                                return False
                            seen[5].add(board[i][j])
                    else:
                        if j < 3:
                            if board[i][j] in seen[6]:
                                return False
                            seen[6].add(board[i][j])
                        elif j < 6:
                            if board[i][j] in seen[7]:
                                return False
                            seen[7].add(board[i][j])
                        else:
                            if board[i][j] in seen[8]:
                                return False
                            seen[8].add(board[i][j])

        return True