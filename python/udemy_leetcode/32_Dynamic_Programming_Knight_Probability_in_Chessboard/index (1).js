// DIRECTIONS is a 2D array that contains all the possible moves that a knight can make.
const DIRECTIONS = [
  [-2, -1],
  [-2, 1],
  [-1, -2],
  [1, 2],
  [2, 1],
  [2, -1],
  [1, -2],
  [-1, 2],
]

/**
 * This function calculates the probability that a knight is on the chessboard after k moves starting from the cell (r, c). This is recursive approach.
 * Our solution's time complexity is O(8^k) because we have 8 possible moves that a knight can make.
 * The space complexity is O(8^k) because we have k recursive calls in the call stack.
 * @param {number} n
 * @param {number} k
 * @param {number} r
 * @param {number} c
 * @returns {number}
 */
const knightProbabilityRecursive = function (n, k, r, c) {
  if (r < 0 || r >= n || c < 0 || c >= n) {
    return 0;
  }
  if (k === 0) {
    return 1;
  }
  let res = 0;
  for (let i = 0; i < DIRECTIONS.length; i++) {
    const dir = DIRECTIONS[i];
    res += knightProbabilityRecursive(n, k - 1, r + dir[0], c + dir[1]) / 8;
  }
  return res;
}

/**
 * This function calculates the probability that a knight is on the chessboard after k moves starting from the cell (r, c). This is top-down dynamic programming approach.
 * Our solution's time complexity is O(k * n^2) because we have k * n^2 sub-problems.
 * The space complexity is O(k * n^2) because we have k * n^2 sub-problems.
 * @param {number} n
 * @param {number} k
 * @param {number} r
 * @param {number} c
 * @returns {number}
 */
const knightProbabilityDPTopDown = function (n, k, r, c) {
  const dp = new Array(k + 1).fill(0).map(() => new Array(n).fill(0).map(() => new Array(n).fill(undefined)));
  return recurse(n, k, r, c, dp);
}

const recurse = function (n, k, r, c, dp) {
  if (r < 0 || r >= n || c < 0 || c >= n) {
    return 0;
  }
  if (k === 0) {
    return 1;
  }
  if (dp[k][r][c] !== undefined) return dp[k][r][c];
  let res = 0;
  for (let i = 0; i < DIRECTIONS.length; i++) {
    const dir = DIRECTIONS[i];
    res += recurse(n, k - 1, r + dir[0], c + dir[1], dp) / 8;
  }
  dp[k][r][c] = res;
  return res;
}

/**
 * This function calculates the probability that a knight is on the chessboard after k moves starting from the cell (r, c). This is bottom-up dynamic programming approach.
 * Our solution's time complexity is O(k * n^2) because we have k * n^2 sub-problems.
 * The space complexity is O(k * n^2) because we have k * n^2 sub-problems.
 * @param {number} n
 * @param {number} k
 * @param {number} r
 * @param {number} c
 */
const knightProbabilityDPBottomUp = function (n, k, r, c) {
  const dp = new Array(k + 1).fill(0).map(() => new Array(n).map(() => new Array(n).fill(0)));
  dp[0][r][c] = 1;
  for (let step = 1; step <= k; step++) {
    for (let row = 0; row < n; row++) {
      for (let col = 0; col < n; col++) {
        for (let i = 0; i < DIRECTIONS.length; i++) {
          const dir = DIRECTIONS[i];
          const prevRow = row + dir[0];
          const prevCol = col + dir[1];
          if (prevRow >= 0 && prevRow < n && prevCol >= 0 && prevCol < n) {
            dp[step][row][col] += dp[step - 1][prevRow][prevCol] / 8;
          }
        }
      }
    }
  }
  let res = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      res += dp[k][i][j];
    }
  }
  return res;
}

const knightProbabilityDPBottomUpOptimized = function (n, k, r, c) {
  let prevDp = new Array(n).fill(0).map(() => new Array(n).fill(0));
  let currDp = new Array(n).fill(0).map(() => new Array(n).fill(0));

  prevDp[r][c] = 1;
  for (let step = 1; step <= k; step++) {
    for (let row = 0; row < n; row++) {
      for (let col = 0; col < n; col++) {
        for (let i = 0; i < DIRECTIONS.length; i++) {
          const dir = DIRECTIONS[i];
          const prevRow = row + dir[0];
          const prevCol = col + dir[1];
          if (prevRow >= 0 && prevRow < n && prevCol >= 0 && prevCol < n) {
            currDp[step][row][col] += prevDp[prevRow][prevCol] / 8;
          }
        }
      }
    }
  }
  prevDp = currDp;
  currDp = new Array(n).fill(0).map(() => new Array(n).fill(0));
  let res = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      res += prevDp[i][j];
    }
  }
  return res;
}

const n1 = 6;
const k1 = 2;
const row1 = 2;
const column1 = 2;
console.log(knightProbabilityRecursive(n1, k1, row1, column1));
console.log(knightProbabilityDPTopDown(n1, k1, row1, column1));
// console.log(knightProbabilityDPBottomUp(n1, k1, row1, column1));
console.log(knightProbabilityDPBottomUpOptimized(n1, k1, row1, column1));
const n2 = 0;
const k2 = 2;
const row2 = 1;
const column2 = 2;
console.log(knightProbabilityRecursive(n2, k2, row2, column2));
console.log(knightProbabilityDPTopDown(n2, k2, row2, column2));
// console.log(knightProbabilityDPBottomUp(n2, k2, row2, column2));
console.log(knightProbabilityDPBottomUpOptimized(n2, k2, row2, column2));
const n3 = 2;
const k3 = 3;
const row3 = 1;
const column3 = 1;
console.log(knightProbabilityRecursive(n3, k3, row3, column3));
console.log(knightProbabilityDPTopDown(n3, k3, row3, column3));
// console.log(knightProbabilityDPBottomUp(n3, k3, row3, column3));
console.log(knightProbabilityDPBottomUpOptimized(n3, k3, row3, column3));
const n4 = 2;
const k4 = 0;
const row4 = 1;
const column4 = 1;
console.log(knightProbabilityRecursive(n4, k4, row4, column4));
console.log(knightProbabilityDPTopDown(n4, k4, row4, column4));
// console.log(knightProbabilityDPBottomUp(n4, k4, row4, column4));
console.log(knightProbabilityDPBottomUpOptimized(n4, k4, row4, column4));