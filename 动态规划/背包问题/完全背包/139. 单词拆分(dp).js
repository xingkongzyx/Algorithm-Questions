/* 
? 为什么先遍历硬币的方式不行, 非常好的讲解:
?  https://leetcode.cn/problems/word-break/solution/by-fenjue-e8d5/
* 更具体的说: 不能先单词后背包的顺序。比如 s = "applepenapple" wordDict = ["apple","pen"] 这个案例, 若物品在外循环, 背包在内循环, 那么外循环第一次使用apple遍历到 dp[12] 也是第二个apple的结尾时, 此时尽管能匹配上但 dp[8](也就是字符 'n') 处于False 的状态, 因此 dp[12] 仍然是 False。在使用 "pen" 进行第二轮外循环时, 使用 pen 将 dp[8] 置为 true 后, 也没法再使用 "apple" 这个物品匹配 dp[12] 了。

? 标准解法: https://leetcode-cn.com/problems/word-break/solution/shou-hui-tu-jie-san-chong-fang-fa-dfs-bfs-dong-tai/

? 链接：https://leetcode.cn/problems/word-break/solution/139-dan-ci-chai-fen-bu-ke-gu-ding-dan-ci-3x74/
*/

// ! 严格按照遍历条件的标准版
var wordBreak = function (s, wordDict) {
    let bagSize = s.length;
    let dp = new Array(bagSize + 1).fill(false);
    dp[0] = true;

    for (let i = 1; i <= bagSize; i++) {
        for (let j = 0; j < wordDict.length; j++) {
            let word = wordDict[j];
            let wordLen = word.length;

            if (
                i >= wordLen &&
                word === s.substr(i - wordLen, wordLen) &&
                dp[i - wordLen] === true
            ) {
                dp[i] = true;
            }
        }
    }
    return dp[s.length];
};

const s = "leetcode",
    wordDict = ["leet", "code"];
console.log(wordBreak(s, wordDict));
