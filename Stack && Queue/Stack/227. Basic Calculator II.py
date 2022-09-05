""" 
? 思路1: https://leetcode.cn/problems/basic-calculator-ii/solution/xian-cheng-chu-zai-jia-jian-yong-zhan-ba-hplr/
? 非常好的讲解: https://labuladong.github.io/algo/4/33/128/
"""


class Solution:
    def calculate(self, s: str) -> int:
        # * 当前遇到的数字
        curNum = 0
        # * 栈。解析过的数字入栈
        stack = []
        # * 上一个遇到的运算符
        # * 预置为 + 是为了能让第一个 curNum 顺利地入栈，因为 prevOp 为 + 才能触发 curNum 入栈
        prevOp = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                curNum = curNum * 10 + int(char)

            # # 因为算式的末尾不是运算符，是数字符号，做完最后一次运算得到的 curNum，并没有更新到栈，需要再if 判断中加入 i == len(s) - 1 的条件来触发更新
            if char in ["+", "-", "*", "/"] or i == len(s) - 1:
                if prevOp == "+":
                    stack.append(curNum)
                elif prevOp == "-":
                    stack.append(-curNum)
                elif prevOp == "*":
                    preNum = stack.pop()
                    productRes = preNum * curNum
                    stack.append(productRes)
                elif prevOp == "/":
                    preNum = stack.pop()
                    if preNum < 0:
                        stack.append(int(preNum / curNum))
                    else:
                        stack.append(preNum // curNum)

                prevOp = char
                curNum = 0
            print(
                f"curChar is {char}, curNum is {curNum}, preop is {prevOp}, stack is {stack}")
        res = 0
        for num in stack:
            res += num

        return res


Solution().calculate(s="3+2*2")
