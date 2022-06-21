//? leetcode.cn/problems/longest-common-subsequence/solution/zui-chang-gong-gong-zi-xu-lie-tu-jie-dpz-6mvz/
/* 
* dp[i][j]表示字符串text1的[0, i-1]区间和字符串text2的[0, j-1]区间的最长公共子序列长度

如果两个字符串 i和j 位置的字符相等
dp[i][j] = dp[i-1][j-1] + 1
如果两个字符串 i和j 位置的字符不相等
dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1])

初始化: 把第一行和第一列都初始化为0. 空字符串与有长度的字符串的最长公共子序列长度肯定为0。
*/

https: var longestCommonSubsequence = function (text1, text2) {
    let dp = new Array(text1.length + 1);
    for (let i = 0; i < text1.length + 1; i++) {
        dp[i] = new Array(text2.length + 1).fill(0);
    }
    console.log(dp);
    for (let row = 1; row <= text1.length; row++) {
        for (let col = 1; col <= text2.length; col++) {
            if (text1[row - 1] === text2[col - 1]) {
                dp[row][col] = dp[row - 1][col - 1] + 1;
            } else {
                dp[row][col] = Math.max(
                    dp[row - 1][col],
                    dp[row][col - 1]
                );
            }
        }
    }

    return dp[text1.length][text2.length];
};
const text1 = "abcde";
const text2 = "ace";
longestCommonSubsequence(text1, text2);
