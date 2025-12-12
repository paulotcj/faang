#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        board_side_len : int = 9
        num_subsquares : int = 9
        subsquare_side_len : int = 3
        
        # logic: let's check every row for repeated values
        #--------------------------------------------------
        for loop_row in range(board_side_len): # for every row...
            seen : set[str] = set() # create a set so we can track values
            for loop_col in range(board_side_len): # and now we check all the values in this specific row
                curr_val : str = board[loop_row][loop_col]
                if curr_val == "." : continue # nothing to do here

                if curr_val in seen: return False # if they are repeated, return false

                seen.add( curr_val ) # add value for tracking - keep looping
        #--------------------------------------------------

        # now we do this but from the column's perspective
        #--------------------------------------------------
        for loop_col in range(board_side_len):
            seen : set[str] = set()
            for loop_row in range(board_side_len):
                curr_val : str = board[loop_row][loop_col]
                if curr_val == "." : continue # nothing to do here

                if curr_val in seen : return False

                seen.add(curr_val)
        #--------------------------------------------------

        # somewhat the same logic now, but this time we loop for 9 sub-squares and then 
        #   for 3 rows and and 3 columns. We check for uniqueness under the same sub-square
        # but we will need to do some math for the sub-square row/col coordinates
        # if you are at square 0, your rows are: 0,1,2 ; and your cols: 0,1,2
        # if you are at square 1, your rows are: 0,1,2 ; and your cols: 3,4,5
        # if you are at square 2, your rows are: 0,1,2 ; and your cols: 6,7,8
        # if you are at square 3, your rows are: 3,4,5 ; and your cols: 0,1,2
        # if you are at square 5, your rows are: 3,4,5 ; and your cols: 6,7,8
        # now we can see the general formula for a row is: (square number // 3)*3 + row
        # and the col is: (square number % 3)*3 + col 
        #--------------------------------------------------
        for loop_subsquare in range(num_subsquares):
            seen : set[str] = set()
            for loop_subsqr_row in range(subsquare_side_len):
                for loop_subsqr_col in range(subsquare_side_len) :
                    actual_row : int = (loop_subsquare // 3) * 3 + loop_subsqr_row
                    actual_col : int = (loop_subsquare %  3) * 3 + loop_subsqr_col
                    curr_val : str = board[actual_row][actual_col]

                    if curr_val == "." : continue
                    if curr_val in seen : return False
                    seen.add(curr_val)
        #--------------------------------------------------
        
        # if at this point you didn't return false, then you looped through all the possible
        #  combinations and nothing was flagged as duplicated, then return True
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
result = sol.isValidSudoku(board=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')
