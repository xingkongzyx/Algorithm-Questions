// https://leetcode-cn.com/problems/ones-and-zeroes/solution/pythonjie-jue-zhi-duo-wei-bei-bao-by-admin_user/

var findMaxForm = function (strs, m, n) {
    let dp = new Array(m + 1);
    for (let i = 0; i < m + 1; i++) {
        dp[i] = new Array(n + 1).fill(0);
    }

    for (let str of strs) {
        let numOfZeros = 0;
        let numOfOnes = 0;
        for (let char of str) {
            if (char === "1") numOfOnes += 1;
            if (char === "0") numOfZeros += 1;
        }
        for (let i = m; i >= numOfZeros; i--) {
            for (let j = n; j >= numOfOnes; j--) {
                dp[i][j] = Math.max(
                    dp[i][j],
                    dp[i - numOfZeros][j - numOfOnes] + 1
                );
            }
        }
    }
    return dp[m][n];
};

let strs = ["10", "0001", "111001", "1", "0"],
    m = 3,
    n = 4;
findMaxForm(strs, m, n);
