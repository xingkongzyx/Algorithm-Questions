//* https://leetcode-cn.com/problems/integer-break/solution/bao-li-sou-suo-ji-yi-hua-sou-suo-dong-tai-gui-hua-/
/* 
* 1. 确定dp数组（dp table）以及下标的含义
* dp[i]: 分拆数字i, 得到的最大乘积是dp[i]
* 2. 递推公式
* 对于数字i, 设定一个辅助数字j从1遍历到 i-1, 此时 dp[i] 只会是 j * dp[i-j] 和j * (i - j) 这两种情况的最大值:
*   dp[i] = max(j * dp[i-j], j * (i - j), dp[i])
* 3. 初始化
* dp[0] = 0 dp[1] = 0 

* 4. 遍历: left -> right from 1

*/
var integerBreak = function (n) {
    let dp = new Array(n + 1).fill(0);
    dp[2] = 1;

    for (let i = 3; i <= n; i++) {
        for (let j = 1; j <= i - 1; j++) {
            //* j * (i - j) 是单纯的把整数拆分为两个数相乘，而j * dp[i - j]是拆分成两个以及两个以上的个数相乘。
            dp[i] = Math.max(dp[i], j * (i - j), j * dp[i - j]);
        }
    }

    return dp[n];
};

let n = 10;
console.log(integerBreak(n));
