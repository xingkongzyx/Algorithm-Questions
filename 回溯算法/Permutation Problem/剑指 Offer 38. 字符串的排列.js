//* 与 47 题是一样的思路
// ? 代码随想录: https://leetcode.cn/problems/zi-fu-chuan-de-pai-lie-lcof/solution/dai-ma-sui-xiang-lu-jian-zhi-offer-38-zi-gwt6/
var permutation = function (s) {
    //! 去重一定要对元素进行排序
    s = s.split("").sort().join("");
    let current = [];
    let total = [];
    let used = new Array(s.length).fill(false);

    function backtracking(s) {
        if (current.length === s.length) {
            total.push(current.join(""));
            return;
        }
        for (let i = 0; i < s.length; i++) {
            if (i > 0 && s[i] == s[i - 1] && used[i - 1] == false) {
                continue;
            }
            if (used[i] === true) continue;
            used[i] = true;
            current.push(s[i]);
            backtracking(s);
            current.pop();
            used[i] = false;
        }
    }
    backtracking(s);
    return total;
};
