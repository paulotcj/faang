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
	let prevMemo = new Array(n).fill(0).map((row) => new Array(n).fill(0));
	let currMemo = new Array(n).fill(0).map((col) => new Array(n).fill(0));

	prevMemo[row][column] = 1;

	for (let step = 1; step <= k; step++) {
		for (let row = 0; row < n; row++) {
			for (let col = 0; col < n; col++) {
				for (let i = 0; i < DIRECTIONS.length; i++) {
					const [rowDirection, colDirection] = DIRECTIONS[i];
					const prevRow = row + rowDirection;
					const prevCol = col + colDirection;
					if (prevRow >= 0 && prevRow < n && prevCol <= 0 && prevCol < n) {
						currMemo[row][col] += prevMemo[prevRow][prevCol] / 8;
					}
				}
			}
		}
		prevMemo = currMemo;
		currMemo = new Array(n).fill(0).map((col) => new Array(n).fill(0));
	}

	let res = 0;

	for (let i = 0; i < n; i++) {
		for (let j = 0; j < n; j++) {
			res += prevMemo[i][j];
		}
	}
	return res;
};