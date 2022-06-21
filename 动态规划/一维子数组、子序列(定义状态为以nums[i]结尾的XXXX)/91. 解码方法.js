/* 
* 状态表示：dp[i] 定义为 以 s[i - 1] 结尾的前缀子串有多少种解法方法；
* 那么，dp[s.length]就表示以 s[s.length - 1] 结尾的前缀子串一共有多少种不同的解码方式，即为答案。

? https://leetcode.cn/problems/decode-ways/solution/jie-ma-fang-fa-tu-jie-dp-zui-qing-xi-yi-97hng/

*/

var numDecodings = function (s) {
    if (s[0] == "0") return 0;
    let dp = new Array(s.length + 1).fill(0);
    dp[0] = 1;

    for (let i = 1; i < dp.length; i++) {
        /// 如果s[i-1] 不为0，说明这个数字可以单独解码，所以 dp[i] = dp[i-1]
        if (s[i - 1] != "0") {
            dp[i] += dp[i - 1];
        }
        /// i >= 2 是因为 s 中的单独的第一个数字也就是s[0](在dp数组中的index是1)是无法与它前面的数字进行组合的
        /// 如果 >= 2, 就能将 s[i-1] 与前面的数字 s[i-2] 组合成两位数，看它是否在 [10,26] 之间，如果在的话，这就是第二种解码方式，dp[i] += dp[i-2]
        if (i >= 2) {
            let num = parseInt(s[i - 2]) * 10 + parseInt(s[i - 1]);
            if (num >= 10 && num <= 26) {
                dp[i] += dp[i - 2];
            }
        }
        //! 如果 s[i-1] == '0' 的话我们就会看它是否能与 s[i-2] 组成 [10,26] 之间的数字，如果能则说明能够解码，否则 例如 s="30", 当遍历到 '0' 的时候上面两个if statement 都无法进入，最后 dp[i] 就还会是默认值 - 0
    }
    console.log(dp);
    return dp[s.length];
};

console.log(numDecodings("2301"));
