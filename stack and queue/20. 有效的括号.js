/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    let stack = [];
    for (let char of s) {
        if (char === "(" || char === "{" || char === "[")
            stack.push(char);
        else {
            //# 第一种情况，括号没有多余，但是 括号的类型没有匹配上。
            //# 第二种情况，字符串里右方向的括号多余了，所以不匹配。
            let parentheses = stack.pop();
            if (char === "]" && parentheses !== "[") return false;
            if (char === "}" && parentheses !== "{") return false;
            if (char === ")" && parentheses !== "(") return false;
        }
    }
    //# 第三种情况 考虑字符串里左方向的括号多余的情况
    return !(stack.length > 0);
};
