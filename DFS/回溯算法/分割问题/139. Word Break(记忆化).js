/*
 * 使用『memory 数组』保存每次计算的以startIndex起始的计算结果，如果 memory[startIndex] 里已经被赋值了，直接用memory[startIndex] 的结果。

? https://leetcode.cn/problems/word-break/solutions/587962/139-dan-ci-chai-fen-hui-su-fa-wan-quan-b-0zwf/?orderBy=most_votes
? https://leetcode.cn/problems/word-break/solutions/1466726/by-lfool-jjq9/?orderBy=most_votes
 */
var wordBreak = function (s, wordDict) {
    let wordSet = new Set(wordDict);
    let memo = new Array(s.length);
    /*
     * 使用 startIdx 使得下轮开始检查的位置不会与之前重复
     */
    function backtracking(startIdx) {
        // * 终止条件: 当 startIdx === s.length 时, 说明前面的所有字符已经与 wordSet 中的单词成功匹配, 此时返回 true
        if (startIdx === s.length) {
            return true;
        }

        // * 终止条件: 如果memory[startIndex]不是初始值了，直接使用memory[startIndex]的结果
        if (memo[startIdx] !== undefined) return memo[startIdx];
        for (let i = startIdx; i < s.length; i++) {
            let curSubStr = s.substring(startIdx, i + 1);
            // * 只有当 curSubStr 是存在于 wordSet 中的时候, 才会继续从下一个位置开始进行检查
            if (wordSet.has(curSubStr)) {
                let tempRes = backtracking(i + 1);
                if (tempRes) return true;
            }
        }

        // * 记录以startIndex开始的子串是不可以被拆分的
        memo[startIdx] = false;
        return false;
    }
    return backtracking(0);
};
