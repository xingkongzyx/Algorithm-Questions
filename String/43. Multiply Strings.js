/* 
? https://leetcode.cn/problems/multiply-strings/solutions/29100/you-hua-ban-shu-shi-da-bai-994-by-breezean/
*/

/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function (num1, num2) {
    // 乘数中有 0，直接返回 "0"
    if (num1 === "0" || num2 === "0") return "0";

    let sum = "0";
    // 遍历 num1 的每一位，从最低位开始
    for (let i = num1.length - 1; i >= 0; i--) {
        let curNum = num1[i]; // 当前位的数值
        let res = [];
        let carry = 0; // 进位

        // 遍历 num2 的每一位，从最低位开始
        for (let j = num2.length - 1; j >= 0; j--) {
            let digit = parseInt(num2[j]) * parseInt(curNum) + carry;
            res.push(digit % 10); // 取个位部分存入数组
            carry = Math.floor(digit / 10); // 更新进位
        }

        // 若计算结束后仍有进位，则加入结果数组
        if (carry > 0) res.push(carry);
        res.reverse(); // 反转数组，以符合正常的数字排列

        // 在末尾补充对应的 0（低位补 0）
        let tailZeros = num1.length - 1 - i;
        while (tailZeros > 0) {
            res.push("0");
            tailZeros--;
        }

        // 将当前乘法结果与累加和相加
        sum = addStrings(sum, res.join(""));
    }
    return sum;
};

/**
 * 字符串加法（大整数加法）
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
function addStrings(num1, num2) {
    let maxLength = Math.max(num1.length, num2.length);

    // 用 0 补齐较短的数字，使它们长度相等
    num1 = num1.padStart(maxLength, 0);
    num2 = num2.padStart(maxLength, 0);

    let carry = 0; // 进位
    let sumResultStr = "";

    // 从个位数开始遍历两个字符串
    for (let i = maxLength - 1; i >= 0; i--) {
        let curDigit = parseInt(num1[i]) + parseInt(num2[i]) + carry;
        carry = Math.floor(curDigit / 10); // 计算新的进位
        sumResultStr = (curDigit % 10) + sumResultStr; // 取当前位的个位数
    }

    // 若最后仍有进位，则需要在前面补 1
    if (carry === 1) {
        sumResultStr = "1" + sumResultStr;
    }
    return sumResultStr;
}
