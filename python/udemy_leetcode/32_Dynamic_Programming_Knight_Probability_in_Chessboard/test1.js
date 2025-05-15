
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
	// Determine if new directino is past row or column boundries
	if (row < 0 || row >= n || column < 0 || column >= n) return 0;
	// If no moves left
	if (k === 0) return 1;

	let res = 0;

	for (let i = 0; i < DIRECTIONS.length; i++) {
		const [rowDirection, colDirection] = DIRECTIONS[i];
		const newRow = row + rowDirection;
		const newCol = column + colDirection;
		res += knightProbability(n, k - 1, newRow, newCol) / 8;
	}

	return res;
};
