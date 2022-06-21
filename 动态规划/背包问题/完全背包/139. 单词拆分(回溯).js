//* https://leetcode-cn.com/problems/word-break/solution/shou-hui-tu-jie-san-chong-fang-fa-dfs-bfs-dong-tai/
var wordBreak = function (s, wordDict) {
    let set = new Set(wordDict);
    console.log(set);
    function backtracking(str, wordSet, startIdx) {
        if (startIdx === str.length) return true;

        for (let i = startIdx; i < str.length; i++) {
            let subStr = str.substring(startIdx, i + 1);
            if (
                wordSet.has(subStr) &&
                backtracking(str, wordSet, i + 1) === true
            ) {
                return true;
            }
        }
        return false;
    }

    let result = backtracking(s, set, 0);
    return result;
};
const s = "applepenapple",
    wordDict = ["apple", "pen"];
console.log(wordBreak(s, wordDict));
