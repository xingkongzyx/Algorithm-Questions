/* 
! 本题与 17 非常相似，每一个字符(非数字)的两个选择「大写形式」或者「小写形式」代表的是「不同集合」，也就是求「不同集合」之间的组合
* 枚举每个位置所取字符的情况，若为数字，则在 cur 中添加该数字；若为字符，枚举大小写字符两种情况即可；然后继续进行递归。
* 具体思路: 
* ➀ 先判断当前字符是否是数字，是数字直接跳过数字不处理，继续递归。
* ➁ 已经明确该字符一定是字母，那就按当前字母建立第一分支。（选择1）
* ➂ 切换字母大小写并建立第二个分支。（选择2）
* ➃ if (s.size() == idx) 说明当前选择的“路”已经走到底。
? 链接：https://leetcode.cn/problems/letter-case-permutation/solution/3chong-hui-su-jie-fa-by-fengziluo-oirf/

* 为什么「当前字符」是「数字字符」也要有回溯操作呢? 正如图中所示，参数 s = "a1b2" 是先进入「小写 a」的分支将其产生的两个结果 ["a1b2","a1B2"] 加入结果数组，然后进行回溯，再进入「大写 A」的分支，这个回溯的过程，遇到的「数字字符」也得从 cur 中排除，重新在「大写 A」的分支重新加入
? 递归树: https://leetcode.cn/problems/letter-case-permutation/solution/shen-du-you-xian-bian-li-hui-su-suan-fa-python-dai/

? 代码来源: https://leetcode.cn/problems/letter-case-permutation/solution/cbao-sou-dai-ma-jian-ji-yi-ji-zi-fu-wei-d4qsk/1371435
*/
function isDigit(c) {
    return c >= "0" && c <= "9";
}

var letterCasePermutation = function (s) {
    const cur = [];
    const total = [];
    function backtracking(s, charIdx) {
        if (charIdx === s.length) {
            total.push(cur.join(""));
            return;
        }

        if (isDigit(s[charIdx]) === true) {
            //* 如果是数字，则直接添加进入 cur, 别忘了之后还有进行回溯
            cur.push(s[charIdx]);
            backtracking(s, charIdx + 1);
            cur.pop();
        } else {
            //* 如果是字母，则分别将大小写字符这两种可能性添加进入 cur, 别忘了之后还有进行回溯
            cur.push(s[charIdx].toLowerCase());
            backtracking(s, charIdx + 1);
            cur.pop();

            cur.push(s[charIdx].toUpperCase());
            backtracking(s, charIdx + 1);
            cur.pop();
        }
    }
    backtracking(s, 0);
    return total;
};
