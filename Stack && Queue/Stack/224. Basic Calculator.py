""" 
? https://leetcode.cn/problems/basic-calculator/solution/ru-he-xiang-dao-yong-zhan-si-lu-lai-zi-y-gpca/
"""


class Solution:
    def calculate(self, s: str) -> int:
        """ 
        * res 表示左边表达式除去栈内保存元素的计算结果;
        * sign 表示运算符, 加号(+1)或者减号(-1)
        * num 表示当前遇到的数字, 会更新到 res 中. 例如: "1 + 23" 中的1或者23
        * 用栈保存遇到「左括号」时前面计算好了的结果和运算符。
        """
        res = 0
        num = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                # *  如果当前字符是一个数字, 则用num进行记录
                # *  当前有可能是一个>9的数字, 所以需要 "num = 10 * num + int(char)"
                num = 10 * num + int(char)
            elif char == "+" or char == "-":
                # * 如果当前是操作符+或者-, 那么需要使用当前的 num 和 sign 更新计算当前整体的计算的结果 res, 并把当前数字 num 设为 0, sign 设为正负, 重新开始;
                res += num * sign
                sign = 1 if char == "+" else -1
                # * 将 num 置为0, 用来存放当前符号(+/-)之后的数字
                num = 0
            elif char == "(":
                # ! 「左括号」只会出现在 s 的第一位, 或者「操作符 + -」的后面, res这个时候已经在遇到操作符的时候被更新过结果, 无需再次更新
                # * 如果当前是 ( , 那么说明之后是「右边的表达式」(注: 我们将括号中的表达式称为「右边的表达式」, 方便与链接中的题解组合理解), 而「右边的表达式」里的内容需要优先计算, 所以要把当前「左边的表达式」的结果res 以及左右表达式之间的「操作符」 sign 进栈, 更新 res 和 sign 为新的开始; 例如当前表达式为：'123+(...)' 则将 "res=23", 入栈, 将 "sign=+1", 入栈
                stack.append(res)
                stack.append(sign)
                # * 同时 res 置为 0, 用来保存 () 中的计算结果
                res = 0
                sign = 1
            elif char == ")":
                # * 如果当前是 ) , 那么说明「右边的表达式」结束, 此时首先需要更新 res为「右边的表达式」的结果, 然后要把之前的左右表达式之间的「操作符」, 「左边的表达式的结果」出栈, 然后计算左右表达式以及中间运算符一起计算后的结果;
                res += num * sign
                num = 0
                lastSign = stack.pop()
                leftRes = stack.pop()
                res *= lastSign
                res += leftRes

        # * 最后, 当所有数字结束的时候, 需要把最后的一个 num 也更新到 res 中。例如 "1 + 2", 最后要把 num = 2, sign = 1 更新到结果 res 中
        res += num * sign
        return res
