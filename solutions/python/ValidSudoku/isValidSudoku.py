class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:[] for i in range(len(board))}
        cols = {i:[] for i in range(len(board))}
        boxes = {i:[] for i in range(len(board))}
        # # Use an array to record the status
        # rows = [[0] * N for _ in range(N)]
        # cols = [[0] * N for _ in range(N)]
        # boxes = [[0] * N for _ in range(N)]
        # # Use hash set to record the status
        # rows = [set() for _ in range(N)]
        # cols = [set() for _ in range(N)]
        # boxes = [set() for _ in range(N)]
        # # Use binary number to check previous occurrence
        # rows = [0] * N
        # cols = [0] * N
        # boxes = [0] * N
        
        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]
                if val == '.':
                    continue
                # check row
                if val in rows[i]:
                    return False
                rows[i].append(val)
                # check col
                if val in cols[j]:
                    return False
                cols[j].append(val)
                # check box
                k = (i//3) * 3 + j//3
                if val in boxes[k]:
                    return False
                boxes[k].append(val)
        return True

