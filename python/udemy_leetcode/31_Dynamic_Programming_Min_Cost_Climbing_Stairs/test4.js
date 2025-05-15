/**
 * @param {number[]} cost
 * @return {number}
 */

// Approach 2: Optimized Iteration w/ Bottom Up Approach
var minCostClimbingStairs = function (cost) {
	const n = cost.length;
	if (n === 0) return 0;
	if (n === 1) return cost[0];

	const dp = [cost[0], cost[1]];

	for (let i = 2; i < n; i++) {
		let current = cost[i] + Math.min(dp[0], dp[1]);
		dp[0] = dp[1];
		dp[1] = current;
	}

	return Math.min(dp[0], dp[1]);
};