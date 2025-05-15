/**
 * @param {number[]} cost
 * @return {number}
 */

// Approach 1: Brute Force Recursion
var minCostClimbingStairs = function (cost) {
	// Get the length of the cost array
	const n = cost.length;
	return Math.min(minCost(n - 1, cost), minCost(n - 2, cost));
};

const minCost = (i, cost) => {
	// Base Cases
	if (i < 0) return 0;
	if (i === 0 || i === 1) return cost[i];

	return cost[i] + Math.min(minCost(i - 1, cost), minCost(i - 2, cost));
};