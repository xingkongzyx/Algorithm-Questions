/* 
* word1 、word2 字符串各抽出一个前缀子字符串
* 如果末尾项不一样，最小步数的来源有三个方向
* 1. 删word1[i - 1]，最少操作次数为dp[i - 1][j] + 1. 其中的加一就是删word1[i - 1]的操作需要的次数
* 2. 删word2[j - 1]，最少操作次数为dp[i][j - 1] + 1. 其中的加一就是删word2[j - 1]的操作需要的次数
* 3. 同时删word1[i - 1]和word2[j - 1]，操作的最少次数为dp[i - 1][j - 1] + 2. 加2就是删word1[i - 1]和word2[j - 1]所需要的两步删除操作
! 因为dp[i][j]代表的含义是最小删除次数，所以最后取最小值，dp[i][j] = min({dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1, dp[i][j - 1] + 1})

? 如果末尾项一样，最小步数的来源只有一个方向, 那就是dp[i-1][j-1]. 
? 因为 word1[i - 1] == word2[j - 1] 说明这个字符是相同的，在我们想要两个字符串相同的大前提下，我们不需要删除这个字符，只需要看，前面的两个字符串若是要达到相同需要的最小删除次数
? 所以在相同时我们不需要进行任何操作，此时的最小步数和dp[i-1][j-1]之前所走的步数一样即 - dp[i][j] = dp[i-1][j-1]


*/

var minDistance = function (word1, word2) {
    let word1_len = word1.length;
    let word2_len = word2.length;
    let dp = new Array(word1_len + 1);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(word2_len + 1).fill(0);
    }
    // dp[i][j]: 以 word1[i-1]为结尾的字符串想与word2[j-1]为结尾的字符串达到相同所需要的删除的最小次数
    // 初始化
    for (let i = 0; i < word1_len + 1; i++) {
        dp[i][0] = i;
    }
    for (let j = 0; j < word2_len + 1; j++) {
        dp[0][j] = j;
    }

    for (let i = 1; i < word1_len + 1; i++) {
        for (let j = 1; j < word2_len + 1; j++) {
            if (word1[i - 1] === word2[j - 1])
                dp[i][j] = dp[i - 1][j - 1];
            else
                dp[i][j] = Math.min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + 2
                );
        }
    }
    return dp[word1_len][word2_len];
};
minDistance("sea", "eat");
