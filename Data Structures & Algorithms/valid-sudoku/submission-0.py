class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set=set()
        for row in board:
            for value in row:
                if value == ".":
                    continue
                if value in row_set:
                    return False
                row_set.add(value)
                
            row_set.clear()
            
        col_set=set()
        for col in range(9):
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in col_set:
                    return False
                col_set.add(board[row][col])
            col_set.clear()
        
        square_set=set()
        for square_starting_row in range(0,9,3):
            for square_starting_col in range(0,9,3):
                
                for row_offset in range(3):
                    for col_offset in range(3):
                        if board[square_starting_row+row_offset][square_starting_col+col_offset] == ".":
                            continue
                        if board[square_starting_row+row_offset][square_starting_col+col_offset] in square_set:
                            return False
                        square_set.add(board[square_starting_row+row_offset][square_starting_col+col_offset])
                square_set.clear()

        return True       
            