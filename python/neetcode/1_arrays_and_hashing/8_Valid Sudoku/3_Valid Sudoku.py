from collections import defaultdict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        board_side_len : int = 9
        num_subsquares : int = 9
        rows        : list[int] = [0] * board_side_len # 9 rows
        cols        : list[int] = [0] * board_side_len # 9 cols
        squares     : list[int] = [0] * num_subsquares # 9 subsquares

        #--------------------------------------------------
        for row_loop in range(board_side_len) :
            for col_loop in range(board_side_len) :
                curr_val : str = board[row_loop][col_loop]
                if curr_val == "." : continue

                curr_val : int = int(curr_val)


                sqr_loc : int = (( row_loop // 3 ) * 3) + (col_loop // 3 )

                #now the bit masking is a 'bit' confusing. But when we do this: 
                # 1 << num  we are shifting the number 1 by 'num' bits. 
                # For instance: 1 << 0 = 1 (no shift has happened) ; 1 << 1 = 2 (10 in binary) ; 
                #  1 << 2 = 4 (0b100) ; 1 << 3 = 8 (0b1000)
                # So effectively we are using the binary value as an array, and we are asking:
                #  consider an array of length of 32 bits, I want to know if in this array the
                #  flag for the number 6 has been flagged. We would do 1 << 6 = 64 (0b1000000)
                #  meaning, in the sixth position, is there a number 1 set?
                #  And to answer this question we do (1 << 6 ) & rows[r]
                bit_mask = (1<<curr_val)
                #-----
                if ( bit_mask & rows[row_loop] or 
                     bit_mask & cols[col_loop] or
                     bit_mask & squares[ sqr_loc ]
                ) :
                    return False
                #-----

                # | -> is the bit 'or' operator. It will set the flag for the number being
                # investigated by the bit_mask
                rows[row_loop] = rows[row_loop] | bit_mask
                cols[col_loop] = cols[col_loop] | bit_mask
                squares[sqr_loc] = squares[sqr_loc] | bit_mask
        #--------------------------------------------------

        # if we looped through all and we didn't find a reason to return False, then at this
        #  point we must return True
        return True
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('------------------------------------')
input = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
 ]
expected = True

sol = Solution()
result = sol.isValidSudoku(board=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
 ]
expected = False

sol = Solution()
result = sol.isValidSudoku(board=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')
