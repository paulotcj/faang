# problem: https://leetcode.com/problems/jump-game-ii/description/
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def jump(self, nums: list[int]) -> int:
        """
        Uses DFS with memoization to find the minimum number of jumps to reach the last index.
        Args:
            nums (List[int]): List of maximum jump lengths at each index.
        Returns:
            int: Minimum number of jumps to reach the last index.
        """
        len_array: int = len(nums)
        memo: dict[int, int] = {}

        #-------------------------------------------------------------------------
        def dfs(position: int) -> int:
            # If we've reached the last index, no more jumps needed
            if position >= len_array - 1: return 0

            # If already computed, return cached result
            if position in memo: return memo[position]

            min_jumps: int = float('inf')

            # Try all possible jumps from current position
            furthest_jump: int = min(position + nums[position], len_array - 1)

            #----------------------------------------
            for next_pos in range(position + 1, furthest_jump + 1):
                jumps: int = 1 + dfs(next_pos)
                if jumps < min_jumps:
                    min_jumps = jumps
            #----------------------------------------
            
            memo[position] = min_jumps
            return min_jumps
        #-------------------------------------------------------------------------

        return dfs(0)
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()
input = [2,3,1,1,4]
expected_result = 2
result = sol.jump(nums = input)
print(f'result: {result} - expected: {expected_result} - is the result expected?: {result==expected_result}')
print('-----')




