/* 
https://leetcode.cn/problems/palindrome-number/solutions/657549/tu-jie-guan-fang-tui-jian-ti-jie-hui-wen-pqvq/
*/
var isPalindrome = function (x) {
    // 1. 负数一定不是回文数
    // 例如 -121 反转后是 121-，不相同
    if (x < 0) {
        return false;
    }

    // 2. 如果数字最后一位是 0，但数字本身不是 0
    // 例如 10 -> 01，不可能是回文
    if (x !== 0 && x % 10 === 0) {
        return false;
    }

    // 用来保存原始数字
    let original = x;

    // 用于存储反转后的数字
    let reversed = 0;

    // 3. 逐位反转数字
    while (x !== 0) {
        // 取出最后一位
        let digit = x % 10;

        // 构建反转后的数字
        reversed = reversed * 10 + digit;

        // 去掉最后一位
        x = Math.trunc(x / 10);
    }

    // 4. 判断反转后的数字是否等于原数字
    return reversed === original;
};
