/* 
> 问题等价转换在t中找到和s相同的子序列，并且它的长度==s的大小
! 这道题与1143几乎是一样的，所以定义方法也可以变成 "长度为i的子串 s[0:i-1]" 和 "长度为j的子串 t[0:j-1]" 的最长公共子序列的长度。最后看这个长度是否等于s的长度
* dp[i][j] ：长度为i，末尾项为s[i-1]的子字符串，与长度为j，末尾项为t[j-1]的子字符串，二者的相同子序列长度。
* 如果 s[i-1] == t[j-1] 则 dp[i][j] = dp[i-1][j-1] + 1
* 如果不等于，则删除 t[j-1]，看dp table中以t[j-2]结尾和s[i-1]结尾的相同子序列的长度是多少，也就是 dp[i][j-1]. 
# 为什么呢，因为要判断 s 是否为 t 的子序列。所以当s[i-1] 和 t[j-1] 不同的时候，我们要删除t中的这个元素，看前面的 t 的子串与 s 的相同子序列的长度。

*/
var isSubsequence = function (s, t) {
    let dp = new Array(s.length + 1);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(t.length + 1).fill(0);
    }

    for (let i = 1; i < s.length + 1; i++) {
        for (let j = 1; j < t.length + 1; j++) {
            if (s[i - 1] === t[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else dp[i][j] = dp[i][j - 1];
        }
    }
    return dp[s.length][t.length] === s.length;
};
