// https://leetcode.cn/problems/longest-palindromic-subsequence/solution/516-zui-chang-hui-wen-zi-xu-lie-by-ming-zhi-shan-y/
/* 
* dp[i][j]表示字符串s[i⋯j]的最长回文子序列的长度。
* 当s[i] == s[j]，也就是说两头的字符是一样的，他们可以和中间的最长回文子序列构成一个更长的回文子序列.那么就说明在原先的基础上又增加了回文子序列的长度，
* dp[i][j] = dp[i+1][j-1] + 2
* 当s[i] != s[j]，那么那么说明s[i]、s[j]至少有一个不在回文子序列中。
* 表明这时的dp[i][j]只需取两者之间的最大值即可。即dp[i][j]=max(dp[i][j−1],dp[i+1][j])。

*/

var longestPalindromeSubseq = function (s) {
    // dp[i][j], 字符串 s 在 [i, j] 范围内的最长回文子序列的长度
    let dp = new Array(s.length);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(s.length).fill(0);
    }

    for (let i = 0; i < dp.length; i++) {
        dp[i][i] = 1;
    }

    for (let i = dp.length - 1; i >= 0; i--) {
        for (let j = i + 1; j < dp.length; j++) {
            if (s[i] == s[j]) dp[i][j] = dp[i + 1][j - 1] + 2;
            else {
                dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[0][dp.length - 1];
};
longestPalindromeSubseq("bbbab");
