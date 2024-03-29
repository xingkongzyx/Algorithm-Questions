/* 
在 JavaScript 中，>> 和 >>> 是两种不同的位移运算符，它们的主要区别在于如何处理符号位（即最左边的位）。

有符号右移（>>）：这个运算符将数字的所有位向右移动指定的位数。对于正数，最左边（符号位）的0会被移入最左边的位置。对于负数，符号位是1，所以移位操作会在最左边填充1。这意味着有符号右移保留了数字的符号（正或负）。

无符号右移（>>>）：这个运算符也将数字的所有位向右移动指定的位数，但它总是在左侧填充0，不管原始数字的符号。这意味着无符号右移不保留数字的符号，总是产生一个非负结果。

举例来说：
如果你对一个正数使用 >> 或 >>>，两者的效果是相同的，因为符号位（0）被移入最左边。
如果你对一个负数使用 >>，它会保留负号，填充1。
如果你对一个负数使用 >>>，它会将负数视为一个非常大的正数（因为二进制中最左边的1现在被解释为数值的一部分，而不是符号位）。
https://leetcode.cn/problems/number-of-1-bits/solutions/1029616/tong-su-yi-dong-de-san-chong-shi-xian-fa-gceg/

*/
var hammingWeight = function (n) {
    let count = 0;
    while (n) {
        // 先判断整数二进制表示中最后边一位是不是1，
        if (n & 1) {
            count++;
        }
        // 把输入的整数右移一位，此时原来从右边数起的第二位被移到了最右边
        n = n >>> 1;
        // 不能用 n = n >> 1, 如果是输入hammingWeight(-2147483648), 就会在-1陷入死循环
        // 所以不能用 n = n >> 1;  因为题目的原话是输入是一个无符号整数（以二进制串的形式）所以这里用无符号右移 再判断是否当前位是1
    }
    // 有符号右移 a >> b 将 a 的二进制表示向右移 b (< 32) 位，丢弃被移出的位。
    // 无符号右移 a >>> b 将 a 的二进制表示向右移 b (< 32) 位，丢弃被移出的位，并使用 0 在左侧填充。
    return count;
};
