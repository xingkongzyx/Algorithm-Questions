var reverse = function (x) {
    // 用于存储反转后的结果
    let result = 0;

    // 32 位有符号整数范围
    const INT_MAX = Math.pow(2, 31) - 1; //  2^31 - 1
    const INT_MIN = -Math.pow(2, 31); // -2^31

    // 当 x 不为 0 时持续处理每一位
    while (x !== 0) {
        // 取出当前数字的最后一位
        const digit = x % 10;

        /*
        在执行 result = result * 10 + digit 之前，
        需要先判断是否会产生 32 位整数溢出。

        因为如果 result > INT_MAX / 10
        那么 result * 10 一定已经超过最大范围。

        同理如果 result < INT_MIN / 10
        那么 result * 10 会小于最小范围。
        */
        if (
            result > Math.floor(INT_MAX / 10) ||
            result < Math.ceil(INT_MIN / 10)
        ) {
            return 0;
        }

        // 将当前 digit 拼接到 result 的末尾
        result = result * 10 + digit;

        // 去掉 x 的最后一位
        // Math.trunc 会去掉小数部分（向 0 取整）
        x = Math.trunc(x / 10);
    }

    // 返回最终反转后的数字
    return result;
};
