// 注意 "两个整数之间的除法只保留整数部分" 这句话说明在num2/num1时我们使用parseInt从而达成得到的结果只保留整数部分。我们不能使用 Math.floor() 以及Math.ceil(). Math.floor()在两数均为 positive number时没问题，当结果是负数 例如 0.034时会向下降到-1，而不是要求的0
var evalRPN = function (tokens) {
    let stack = [];
    for (let char of tokens) {
        if (Number.isNaN(parseInt(char))) {
            let num1 = Number(stack.pop());
            let num2 = Number(stack.pop());
            let res;
            if (char === "+") res = num2 + num1;
            if (char === "*") res = num2 * num1;
            if (char === "-") res = num2 - num1;
            if (char === "/") res = parseInt(num2 / num1);
            stack.push(res);
            // console.log(num2, num1, char, res, stack);
        } else {
            stack.push(char);
        }
    }
    return stack.pop();
};
n = 10 * (6 / ((9 + 3) * -11)) + 17 + 5;
let tokens = [
    "10",
    "6",
    "9",
    "3",
    "+",
    "-11",
    "*",
    "/",
    "*",
    "17",
    "+",
    "5",
    "+",
];
console.log(evalRPN(tokens));
