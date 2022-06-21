var uniquePathsWithObstacles = function (obstacleGrid) {
    let rows = obstacleGrid.length;
    let cols = obstacleGrid[0].length;
    let dp = new Array(rows);
    for (let rowIdx = 0; rowIdx < rows; rowIdx++) {
        dp[rowIdx] = new Array(cols).fill(0);
    }

    for (let i = 0; i < rows; i++) {
        if (obstacleGrid[i][0] === 1) {
            dp[i][0] = 0;
            break;
        } else {
            dp[i][0] = 1;
        }
    }

    for (let j = 0; j < cols; j++) {
        if (obstacleGrid[0][j] === 1) {
            dp[0][j] = 0;
            break;
        } else {
            dp[0][j] = 1;
        }
    }

    for (let rowIdx = 1; rowIdx < rows; rowIdx++) {
        for (let colIdx = 1; colIdx < cols; colIdx++) {
            if (obstacleGrid[rowIdx][colIdx] === 1) {
                continue;
            } else {
                dp[rowIdx][colIdx] =
                    dp[rowIdx - 1][colIdx] + dp[rowIdx][colIdx - 1];
            }
        }
    }
    return dp[rows - 1][cols - 1];
};

const obstacleGrid = [
    [0, 1],
    [0, 0],
];
console.log(uniquePathsWithObstacles(obstacleGrid));
