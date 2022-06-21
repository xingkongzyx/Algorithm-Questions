var restoreIpAddresses = function (s) {
    let currentPath = [];
    let totalPath = [];

    function backtracking(s, startIdx) {
        //* 本题明确要求只会分成4段，所以不能用切割线切到最后作为终止条件，而是分割的段数作为终止条件。
        if (currentPath.length === 4) {
            if (startIdx === s.length)
                totalPath.push(currentPath.join("."));
            return;
        }

        for (let i = startIdx; i < s.length; i++) {
            //* [startIndex, i] 这个区间就是截取的子串，需要判断这个子串是否合法。
            if (checkValid(s, startIdx, i)) {
                currentPath.push(s.substring(startIdx, i + 1));
            } else {
                //! 这里注意，如果截取的字串不符合要求，直接break而不是continue，因为以startIdx开始的字串都不会符合要求，例如已经以多余的0开始字串，即使i往后移动，截取的字串还是从0开始，导致不符合要求
                break;
            }

            backtracking(s, i + 1);
            currentPath.pop();
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
