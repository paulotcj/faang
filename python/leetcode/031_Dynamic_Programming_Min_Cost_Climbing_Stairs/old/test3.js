/**
 * @param {number[]} cost
 * @return {number}
 */

// Approach 2: Iteration w/ Bottom Up Approach
var minCostClimbingStairs = function (cost) {
	// Get the length of the cost array
	const n = cost.length;
	const memo = [];

	for (let i = 0; i < n; i++) {
		if (i < 2) {
			memo[i] = cost[i];
		} else {
			memo[i] = cost[i] + Math.min(memo[i - 1], memo[i - 2]);
		}
	}

	return Math.min(memo[n - 1], memo[n - 2]);
};