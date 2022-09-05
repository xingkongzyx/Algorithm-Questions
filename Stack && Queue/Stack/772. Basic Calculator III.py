""" 
? 注释明确: https://leetcode.cn/problems/basic-calculator/solution/chai-jie-fu-za-wen-ti-shi-xian-yi-ge-wan-zheng-j-2/1569323
"""
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        s = deque(s)

        def helper(sQueue):
            stack = []
            preOperator = '+'
            curNum = 0

            while len(sQueue) > 0:
                char = sQueue.popleft()
                if char.isdigit():
                    curNum = 10 * curNum + int(char)
                # * 遇到左括号开始递归计算 num
                if char == '(':
                    curNum = helper(sQueue)

                # # 第一种情况, 如果不为数字和空格, 也就是遇到 '+' , '-' , '*' , '/', ')'
                # # 或者是遇到第二种情况, 也急速遇到字符串的尾部 (尾部可能是一个数字, 可能是 ')' , 也可能是' ' , 所以这两种情况之间有重叠)
                # ! 则将前一个操作符和数压入堆栈
                if (char in ["+", "-", "*", "/", ")"]) or len(sQueue) == 0:
                    if preOperator == '+':
                        stack.append(curNum)
                    elif preOperator == '-':
                        stack.append(-curNum)
                    elif preOperator == '*':
                        stack.append(stack.pop() * curNum)
                    elif preOperator == '/':
                        stack.append(int(stack.pop() / curNum))
                    curNum = 0
                    # * 记录当前符号。若当前 char 为右括号或最后一个字符则为无效记录，但不影响结果计算。
                    preOperator = char

                # * 只有递归过程才会遇到 ')', 上面运算完了需要额外进行 break
                if char == ')':
                    break
            return sum(stack)

        return helper(s)
