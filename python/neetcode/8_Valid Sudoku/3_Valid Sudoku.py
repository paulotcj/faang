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

                # let's go over the math for the squares. Consider we have squares from 0 to 8
                #  where their coordinates is 0->[0][0] to 8->[2][2]
                # rows should produce the x coordinates and rows from 0,1,2 should produce sq=0 ; 
                #  3,4,5 sqr=1 ; 6,7,8 sqr=2
                # We can see the X coordinates is basically: row // 3 = x_coord
                # And the same logic applies to the columns
                sqr_loc : tuple[int,int] = ( row_loop // 3 , col_loop // 3 )

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
        #--------------------------------------------------

    def isValidSudoku2(self, board: list[list[str]]) -> bool:
        #######################################
        board_side_len : int = 9
        num_subsquares : int = 9
        rows        : list[int] = [0] * board_side_len # 9 rows
        cols        : list[int] = [0] * board_side_len # 9 cols
        squares     : list[int] = [0] * num_subsquares # 9 subsquares

        #--------------------------------------------------
        for r in range(9):
            #--------------------------------------------------
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                val = int(val)

                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
                    return False

                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << val)
            #--------------------------------------------------
        #--------------------------------------------------
        return True

        #--------------------------------------------------

        #--------------------------------------------------


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
result = sol.isValidSudoku2(board=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
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
result = sol.isValidSudoku2(board=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')
