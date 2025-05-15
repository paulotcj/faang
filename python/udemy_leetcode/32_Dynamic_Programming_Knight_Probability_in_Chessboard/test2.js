const DIRECTIONS = [
	[-2, -1],
	[-2, 1],
	[-1, -2],
	[-1, 2],
	[1, -2],
	[1, 2],
	[2, -1],
	[2, 1],
];

// Time complexity: O(8^k)
// Space Complexity: O(k)
var knightProbability = function (n, k, row, column) {
	// Init memo
	const memo = new Array(k + 1).fill(0).map(() => new Array(n).fill(0).map(() => new Array(n).fill(undefined)));

	return recurse(n, k, row, column, memo);
};

const recurse = function (n, k, row, column, memo) {
	// Determine if new directino is past row or column boundries
	if (row < 0 || row >= n || column < 0 || column >= n) return 0;
	// If no moves left
	if (k === 0) return 1;
	// Check if memoized
	if (memo[k][row][column] !== undefined) return memo[k][row][column];

	let probability = 0;

	for (let i = 0; i < DIRECTIONS.length; i++) {
		const [rowDirection, colDirection] = DIRECTIONS[i];
		const newRow = row + rowDirection;
		const newCol = column + colDirection;
		probability += knightProbability(n, k - 1, newRow, newCol) / 8;
	}
	memo[k][row][column] = probability;
	return probability;
};