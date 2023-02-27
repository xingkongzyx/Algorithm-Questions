/* 
> 与回溯算法中的 131. 分割回文串 是非常类似的
* "leetcode"能否 break, 可以拆分为：
*  ✧ "l"是否是单词表的单词, 剩余子串能否 break。
*  ✧ "le"是否是单词表的单词, 剩余子串能否 break。
*  ✧ "lee"...以此类推
* 用 DFS 回溯, 考察所有的拆分可能, 指针从左往右扫描：
*  ✧ 如果指针的左侧部分是单词, 则对剩余子串递归考察。
*  ✧ 如果指针的左侧部分不是单词, 不用看了, 回溯, 考察别的分支。

? https://leetcode.cn/problems/word-break/solutions/302779/shou-hui-tu-jie-san-chong-fang-fa-dfs-bfs-dong-tai/

*/

var wordBreak = function (s, wordDict) {
    let wordSet = new Set(wordDict);
    /*
     * 使用 startIdx 使得下轮开始检查的位置不会与之前重复
     */
    function backtracking(startIdx) {
        // * 终止条件: 当 startIdx === s.length 时说明前面的所有字符已经与 wordSet 中的单词成功匹配
        if (startIdx === s.length) {
            return true;
        }

        for (let i = startIdx; i < s.length; i++) {
            // * s[i, startIdx] 就是当前要检查的 substring
            let curSubStr = s.substring(startIdx, i + 1);
            // * 只有当 curSubStr 是存在于 wordSet 中的时候, 才会继续从下一个位置开始进行检查
            if (wordSet.has(curSubStr)) {
                let tempRes = backtracking(i + 1);
                if (tempRes) return true;
            }
        }
        return false;
    }
    return backtracking(0);
};
