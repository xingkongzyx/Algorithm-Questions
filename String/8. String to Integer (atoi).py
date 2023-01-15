""" 
? https://leetcode.cn/problems/string-to-integer-atoi/solution/pythonqing-xi-yi-dong-de-zi-fu-chuan-zhuan-zheng-s/
? https://leetcode.cn/problems/string-to-integer-atoi/solution/jin-liang-bu-shi-yong-ku-han-shu-nai-xin-diao-shi-/
"""


class Solution:
    def myAtoi(self, str: str) -> int:
        length = len(str)
        self.INT_MIN, self.INT_MAX = -2**31, 2**31-1
        # // 1、去除前导空格
        index = 0
        while (index < length and str[index] == ' '):
            index += 1

        # // 2、如果已经遍历完成（针对极端用例 "      "）
        if (index == length):
            return 0

        # // 3、如果出现符号字符，仅第 1 个有效，并记录正负
        sign = 1
        firstChar = str[index]
        if (firstChar == '+'):
            index += 1
        elif (firstChar == '-'):
            index += 1
            sign = -1

        # // 4、将后续出现的数字字符进行转换
        res = 0
        while index < length:
            currChar = str[index]
            # // 4.1 先判断不合法的情况
            if currChar > '9' or currChar < '0':
                break

            # 先处理越界，并取10整除，因为先判断越界再做后面运算，所以要判断是否超过最大值的整除10的数
            # res > self.INT_MAX // 10 对应最小边界
            # res == self.INT_MAX // 10 and (ord(str[i]) - ord('0') > 7) 对应最大边界, 这里7是因为(2**31 - 1) % 10 = 7
            if res > self.INT_MAX // 10 or (res == self.INT_MAX // 10 and (ord(str[index]) - ord('0') > 7)):
                if sign == 1:
                    return self.INT_MAX
                else:
                    return self.INT_MIN
            res = res * 10 + ord(str[index]) - ord('0')

            index += 1
        # print(res)
        return res * sign


Solution().myAtoi("42")
