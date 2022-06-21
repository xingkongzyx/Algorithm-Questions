//* https://leetcode-cn.com/problems/word-break/solution/shou-hui-tu-jie-san-chong-fang-fa-dfs-bfs-dong-tai/

/* 
> 为什么内层外层的遍历顺序是重要的
排列问题：是否有 任何一种 单词排列 可以 凑成目标 s（固定死单词出现的顺序，可能无法拼出s）

本题与[凑硬币]不同的是，相同长度的单词不一定相同 => 导致了

组合问题 变 排序问题
转移方程，除来考虑单词长度 以外，还要考虑 单词是否相等 s[i-len(w):i]==w

链接：https://leetcode.cn/problems/word-break/solution/139-dan-ci-chai-fen-bu-ke-gu-ding-dan-ci-3x74/
链接: https://leetcode.cn/problems/word-break/solution/by-fenjue-e8d5/
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

// ! carl的优化版
var wordBreak_sol2 = function (s, wordDict) {
    let wordSet = new Set(wordDict);
    let dp = new Array(s.length + 1).fill(false);
    dp[0] = true;

    for (let i = 1; i <= s.length; i++) {
        for (let j = 0; j < i; j++) {
            let word = s.substring(j, i);
            if (wordSet.has(word) && dp[j] === true) dp[i] = true;
        }
    }
    return dp[s.length];
};

const s = "leetcode",
    wordDict = ["leet", "code"];
console.log(wordBreak(s, wordDict));
