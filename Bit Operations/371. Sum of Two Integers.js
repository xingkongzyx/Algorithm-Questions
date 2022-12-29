/* 
总结一下：
➀ a + b 的问题拆分为 (a 和 b 的无进位结果) + (a 和 b 的进位结果)
➁ 「无进位结果」使用「异或」运算计算得出
➂ 进位结果使用「&运算」和「移位运算」计算得出
➃ 此时 "a + b" 的问题被转换为 "a + b = (a ^ b) + ((a & b) << 1)", 我们对转换后的值继续进行 ➀➁➂ 的步骤, 由于 "(a & b)<<1" 会不断左移， 所以 carry 最后一定会变成0， 此时计算就完成了。

? https://leetcode.cn/problems/sum-of-two-integers/solution/li-yong-wei-cao-zuo-shi-xian-liang-shu-qiu-he-by-p/
? js代码: https://leetcode.cn/problems/sum-of-two-integers/solution/by-iimt-ty09/
/ 时间复杂度: O(1), 最多循环32次, 因为需要左移32位。
/ 空间复杂度: O(1)
*/
var getSum = function (a, b) {
    while (b !== 0) {
        carry = (a & b) << 1;
        no_carry_sum = a ^ b;
        a = no_carry_sum;
        b = carry;
    }
    return a;
};
