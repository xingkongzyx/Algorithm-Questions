
# ? python 的相关避坑操作: https://leetcode.cn/problems/evaluate-reverse-polish-notation/solution/xiang-jie-ni-bo-lan-biao-da-shi-fu-ben-t-sfl6/
class Solution:
    def evalRPN(self, tokens):
        operators = {"+", "-", "*", "/"}
        stack = []
        for char in tokens:
            if char in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                if char == "/":
                    result = int(num2 / num1)
                elif char == "+":
                    result = num2 + num1
                elif char == "*":
                    result = num2 * num1
                elif char == "-":
                    result = num2 - num1

                stack.append(result)
            else:
                stack.append(int(char))
        return stack[-1]


print(Solution().evalRPN(
    tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
