/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function (num1, num2) {
    // num1 is the multiply
    for (let i = num1.length - 1; i >= 0; i--) {
        let curNum = num1[i];
        let res = [];
        let carry = 0;
        for (let j = num2.length - 1; j >= 0; j--) {
            let digit = parseInt(num2[j]) * parseInt(curNum) + carry;
            res.push(digit % 10);
            carry = Math.floor(digit / 10);
        }

        res.reverse();
        if (carry > 0) res.push(carry);
        console.log(res);
    }
};
multiply("12", "12");
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
function addStrings(num1, num2) {
    //取两个数字中最大长度， b 比 a 长，maxLength 就是 b 的 length
    let maxLength = Math.max(num1.length, num2.length);

    //padStart(targetLength,padString)
    //targetLength 即补齐后的目标长度，padString 即填充字符串
    //用 0 去补齐长度
    num1 = num1.padStart(maxLength, 0); //结果 "0009007199254740991"
    num2 = num2.padStart(maxLength, 0); //结果 "1234567899999999999"

    //声明加法过程中需要用到的变量
    let curDigit = 0;
    let carry = 0; //"进位"
    let sumResultStr = ""; // sum 声明为空字符串

    // 从个位数开始遍历数字
    for (let i = maxLength - 1; i >= 0; i--) {
        curDigit = parseInt(num1[i]) + parseInt(num2[i]) + carry;

        // 取地板数，比如 9/10 取 0， 11/10 取 1
        carry = Math.floor(curDigit / 10);

        // 取模，个位数与 10 取模为它本身，即余数
        // 因为 sum 声明为空字符串，所以数字会被转换成字符串
        // 比如 8 + "9" 输出为字符串 "89"
        sumResultStr = (curDigit % 10) + sumResultStr;
    }

    //最后得到的 sum 时， f 为 1 即在前加 1
    //假设此时 sum 为 "xxx", f 为 1，则返回"1xxx"
    if (carry == 1) {
        sumResultStr = "1" + sumResultStr;
    }
    return sumResultStr;
}
