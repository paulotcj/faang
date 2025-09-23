/**
 * @param {number[]} cost
 * @return {number}
 */

// Approach 2: Recursion w/ Top-Down Memoization
var minCostClimbingStairs = function (cost) {
	// Get the length of the cost array
	const n = cost.length;
	const memo = [];
	return Math.min(minCost(n - 1, cost, memo), minCost(n - 2, cost, memo));
};

const minCost = (i, cost, memo) => {
	// Base Cases
	if (i < 0) return 0;
	if (i === 0 || i === 1) return cost[i];
	if (memo[i] !== undefined) return memo[i];
	memo[i] = cost[i] + Math.min(minCost(i - 1, cost, memo), minCost(i - 2, cost, memo));
	return memo[i];
};