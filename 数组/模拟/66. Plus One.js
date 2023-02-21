/* 
* ➀ 末位无进位, 则末位加一即可, 因为末位无进位, 前面也不可能产生进位, 比如 45 => 46, 此时直接返回
* ➁ 末位有进位, 在中间位置进位停止, 则需要找到进位的典型标志, 即为当前位 +1 后为 10, 则继续循环, 前一位加 1, 直到不为 0 为止, 比如 499 => 500
* ➂ 末位有进位, 并且一直进位到最前方导致结果多出一位, 对于这种情况, 需要在第 2 种情况遍历结束的基础上, 进行单独处理, 比如 999 => 1000
? 思路: https://leetcode.cn/problems/plus-one/solutions/9236/hua-jie-suan-fa-66-jia-yi-by-guanpengchn/
? 代码: https://leetcode.cn/problems/plus-one/solutions/97972/c-z-by-zrita/?orderBy=most_votes
*/
var plusOne = function (digits) {
    for (let i = digits.length - 1; i >= 0; i--) {
        digits[i] += 1;

        if (digits[i] === 10) {
            digits[i] = 0;
        } else {
            return digits;
        }
    }

    digits.unshift(1);
    return digits;
};
function calcSquare(num) {
    let res = 0;
    while (num > 0) {
        let curDigit = num % 10;
        res += curDigit * curDigit;
        num = Math.floor(num / 10);
    }
    return res;
}

console.log(calcSquare(12));
