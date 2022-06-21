/* 
* dp[i][j]：word1 的前[0...i-1] 转换成 word2 的前 [0...j-1] 字符最少需要操作的次数
> 因为状态的定义是将 word1 转换成 word2的方法数，所以下方 word1[i-1] != word2[j-1]时删除、替换、插入的操作是在word1上完成的

/ 情况 1：如果 word1[i - 1] == word2[j - 1]，即当前考虑的两个字符串的最后一个字符相等，此时它们的编辑距离就等于它们去掉了最后一个字符以后的编辑距离，dp[i][j] = dp[i - 1][j - 1]；

/ 情况 2：如果 word1[i - 1] != word2[j - 1]，此时编辑距离是以下三种情况的最小者(替换字符操作, 删除字符操作, 插入字符操作)
/ 情况 2.1：在当前 word1 后面加上与当前 word2 最后一个字符相等的字符（操作次数 + 1），此时编辑距离 dp[i][j] = dp[i][j - 1] + 1；在 word1[i-1] 后面的一个位置加上了与 word2[j-1] 位置相同的字符串。相当于此时 word[i] === word2[j-1]，好似又回到了情况一，我们要考虑将 word1[0:i-1] 变成 word2[0:j-2]  最少的操作次数，也就是dp[i][j-1] 的值
/ 情况 2.2 ：去掉当前 word1 后面最后一个字符（操作次数 + 1），此时编辑距离 dp[i][j] = dp[i - 1][j] + 1；
/ 情况 2.3：将当前 word1 后面最后一个字符替换成当前 word2最后一个字符（操作次数 + 1），此时编辑距离 dp[i][j] = dp[i - 1][j - 1] + 1。

? https://leetcode.cn/problems/edit-distance/solution/dong-tai-gui-hua-java-by-liweiwei1419/
*/
var minDistance = function (word1, word2) {
    let word1_len = word1.length;
    let word2_len = word2.length;
    let dp = new Array(word1_len + 1);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(word2_len + 1).fill(0);
    }

    for (let i = 0; i < dp.length; i++) {
        dp[i][0] = i;
    }

    for (let j = 0; j < dp[0].length; j++) {
        dp[0][j] = j;
    }

    for (let i = 1; i < word1_len + 1; i++) {
        for (let j = 1; j < word2_len + 1; j++) {
            if (word1[i - 1] === word2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] =
                    Math.min(
                        dp[i - 1][j - 1],
                        dp[i][j - 1],
                        dp[i - 1][j]
                    ) + 1;
            }
        }
    }

    return dp[word1_len][word2_len];
};
