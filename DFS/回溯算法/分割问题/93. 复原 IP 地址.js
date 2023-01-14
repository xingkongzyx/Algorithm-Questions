//? https://leetcode.cn/problems/restore-ip-addresses/solution/java-2mstong-guo-hui-su-suan-fa-fu-shang-wq7y/
//? https://leetcode.cn/problems/restore-ip-addresses/solution/shou-hua-tu-jie-huan-yuan-dfs-hui-su-de-xi-jie-by-/
var restoreIpAddresses = function (s) {
    let currentPath = [];
    let totalPath = [];

    function backtracking(s, startIdx) {
        //* 本题明确要求只会分成 4 段, 所以不能用切割线切到最后作为终止条件, 而是「分割的段数」作为终止条件。
        /// 但是要加入「结果数组」, 在确保「分割的段数」为 4 的同时也要确保此时的「分割线的位置」在末尾
        if (currentPath.length === 4) {
            if (startIdx === s.length)
                totalPath.push(currentPath.join("."));
            return;
        }

        for (let i = startIdx; i < s.length; i++) {
            //* [startIndex, i] 这个区间就是截取的子串, 需要判断这个子串是否合法。
            if (checkValid(s, startIdx, i)) {
                currentPath.push(s.substring(startIdx, i + 1));
                backtracking(s, i + 1);
                currentPath.pop();
            } else {
                //! 这里注意, 如果截取的字串不符合要求, 直接 break 而不是 continue, 因为以 startIdx 开始的字串都不会符合要求, 例如已经以多余的 0 开始的字串, 即使 i 继续往后移动, 截取的字串还是从 0 开始, 导致不符合要求
                break;
            }
        }
    }
    backtracking(s, 0);
    return totalPath;
};

/*
 * 判断段位是否有效主要考虑到如下三点：
 *
 * 1) 段位以0为开头的数字不合法
 * 2) 段位里有非正整数字符不合法
 * 3) 段位如果大于255了不合法
 */
function checkValid(str, startIdx, endIdx) {
    let subString = str.substring(startIdx, endIdx + 1);
    if (subString.length > 1 && subString[0] === "0") return false;
    let subStringToNum = parseInt(subString);
    if (subStringToNum < 0 || subStringToNum > 255) return false;
    return true;
}
