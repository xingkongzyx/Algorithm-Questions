var uniquePaths = function (m, n) {
    const dp = new Array(m);
    for (let i = 0; i < m; i++) {
        dp[i] = new Array(n).fill(0);
    }

    for (let rowIdx = 0; rowIdx < m; rowIdx++) {
        dp[rowIdx][0] = 1;
    }

    for (let colIdx = 0; colIdx < n; colIdx++) {
        dp[0][colIdx] = 1;
    }

    for (let rowIdx = 1; rowIdx < m; rowIdx++) {
        for (let colIdx = 1; colIdx < n; colIdx++) {
            dp[rowIdx][colIdx] =
                dp[rowIdx][colIdx - 1] + dp[rowIdx - 1][colIdx];
        }
    }
    // console.log(dp);
    return dp[m - 1][n - 1];
};

const m = 5;
const n = 5;

uniquePaths(5, 5);
