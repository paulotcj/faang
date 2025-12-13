from collections import defaultdict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        cols    : defaultdict[set[str]] = defaultdict(set)
        rows    : defaultdict[set[str]] = defaultdict(set)
        squares : defaultdict[set[str]] = defaultdict(set)

        board_side_len : int = 9

        #--------------------------------------------------
        for row_loop in range(board_side_len) :
            #----
            for col_loop in range(board_side_len) :
                curr_val : str = board[row_loop][col_loop]
                if curr_val == "." : continue

                # let's go over the math for the squares. Consider we have squares from 0 to 8
                #  where their coordinates is 0->[0][0] to 8->[2][2]
                # rows should produce the x coordinates and rows from 0,1,2 should produce sq=0 ; 
                #  3,4,5 sqr=1 ; 6,7,8 sqr=2
                # We can see the X coordinates is basically: row // 3 = x_coord
                # And the same logic applies to the columns
                sqr_loc : tuple[int,int] = ( row_loop // 3 , col_loop // 3 )

                #----
                if ( curr_val in rows[row_loop] or
                     curr_val in cols[col_loop] or
                     curr_val in squares[sqr_loc] 
                ) : 
                    return False
                #----

                rows[row_loop].add( curr_val )
                cols[col_loop].add( curr_val )
                squares[ sqr_loc ].add( curr_val )
            #----
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
