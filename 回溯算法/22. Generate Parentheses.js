//? https://leetcode.cn/problems/generate-parentheses/solution/shou-hua-tu-jie-gua-hao-sheng-cheng-hui-su-suan-fa/
var generateParenthesis = function (n) {
    let left = n;
    let right = n;
    let current = [];
    let total = [];

    function backtracking(left, right) {
        if (left === 0 && right === 0) {
            total.push(current.join(""));
            return;
        }

        //* 产生左分支的时候，只看当前是否还有左括号可以使用，也就是检查 left > 0
        if (left > 0) {
            left -= 1;
            current.push("(");
            backtracking(left, right);
            current.pop();
            left += 1;
        }
        //* 产生右分支的时候，还受到左分支的限制，右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候，才可以产生分支；
        if (right > left) {
            right -= 1;
            current.push(")");
            backtracking(left, right);
            current.pop();
            right += 1;
        }
    }
    backtracking(left, right);
    console.log(total);
    return total;
};

generateParenthesis(1);
