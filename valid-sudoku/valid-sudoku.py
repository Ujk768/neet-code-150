from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check cols keep a set to track of numbers seen in the columns
        for col in range(9):
            col_set = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in col_set :
                    return False
                col_set.add(board[i][col])  
        # check rows keep a set to keep track of numbers seen in rows
        for row in range(9):
            hm = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in hm :
                    return False
                hm.add(board[row][i])
        
        # check squares
        for square in range(9):
            square_set = set()
            # Calculate the top-left corner of the current 3x3 square
            start_row = (square // 3) * 3
            start_col = (square % 3) * 3
            
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    val = board[r][c]
                    
                    if val == ".":
                        continue
                    
                    if val in square_set:
                        return False
                    
                    square_set.add(val)
                
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))
        



            
        