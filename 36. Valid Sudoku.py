from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cube_set = [set() for _ in range(9)]
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    continue
                if board[i][j] in cube_set[i//3*3+j//3]:
                    return False
                else:
                    cube_set[i // 3 * 3 + j // 3].add(board[i][j])
                if board[i][j] in row_set[i]:
                    return False
                else:
                    row_set[i].add(board[i][j])
                if board[i][j] in col_set[j]:
                    return False
                else:
                    col_set[j].add(board[i][j])

        return True

arr=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
solotion=Solution()
print(solotion.isValidSudoku(arr))

