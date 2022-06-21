/* 
? https://leetcode.cn/problems/distinct-subsequences/solution/shou-hua-tu-jie-xiang-jie-liang-chong-ji-4r2y/ 
/ 题目是求 在 s 的 "子序列" 中 t 出现的个数。
/ 翻译就是 在 s 中可以进行删除操作(也就是题目中说的 "通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串") 达到挑选相对位置不变的字符去匹配 t，计算挑选的方法数
! 抓住 “选”，s 要在自己身上挑选字符匹配 t 串。

* dp[i][j]：从开头到s[i-1]的子串中，出现『从开头到t[j-1]的子串』的 次数。
* 即：前 i 个字符的 s 子串中，出现前 j 个字符的 t 子串的次数。

/ 抓住 “选”，s 要照着 t 来挑选，对 s 逐字符考察选或不选，分别来到什么状态？
/ 举例，s 为 babgbag，t 为 bag，末尾字符相同，于是 s 有两种选择：
/   ☆ 用s[s.length-1]去匹配掉 t[t.length-1]，然后此时 dp[i][j] = dp[i-1][j-1]
/   ☆ 不这么做，但t[t.length-1]仍需被匹配，于是在babgba中继续挑，考察babgba和bag, 此时dp[i][j] = dp[i-1][j]
/   ☆ 最后将两种选择的结果数加一起 dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
! 是否用 s[s.length-1] 去匹配，是两种不同的挑选方式，各自做下去所产生的方式数，相加，是大问题的解。
/ 如果 s[i]!=t[j] 则说明 s[i] 不匹配 t[j]，唯有拿s[i]之前的子串s[0:i-1]去匹配, dp[i][j] = dp[i-1][j]

> 因为是在s中挑选字符去匹配 t, 所以删除操作只能在 s 进行, 而不能对 t 进行



*/
var numDistinct = function (s, t) {
    let s_len = s.length;
    let t_len = t.length;
    let dp = new Array(s_len + 1);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(t_len + 1);
    }

    // 初始化 以s[i-1]为结尾的字符串可以通过删除的操作，能够包含多少个空字符串呢
    for (let i = 0; i <= s_len; i++) {
        dp[i][0] = 1;
    }
    // 初始化 空字符串可以通过删除的操作，能够包含多少个以 t[j-1] 结尾的t的子序列呢
    for (let j = 0; j <= t.length; j++) {
        dp[0][j] = 0;
    }
    dp[0][0] = 1;

    for (let i = 1; i <= s_len; i++) {
        for (let j = 1; j <= t_len; j++) {
            if (s[i - 1] === t[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    return dp[s_len][t_len];
};
