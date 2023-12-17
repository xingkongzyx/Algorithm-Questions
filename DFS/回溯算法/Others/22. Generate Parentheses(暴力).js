// https://leetcode.cn/problems/generate-parentheses/
var generateParenthesis = function (n) {
    let current = [];
    let total = [];

    function backtracking() {
        if (current.length === 2 * n) {
            total.push(current.join(""));
            return;
        }
        // 添加左括号
        current.push("(");
        backtracking();
        current.pop();

        // 添加右括号
        current.push(")");
        backtracking();
        current.pop();
    }

    backtracking();
    return total;
};
