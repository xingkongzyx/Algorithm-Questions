
#? 另一种完全同步的辅助栈做法: https://leetcode.cn/problems/min-stack/solution/fu-zhu-zhan-zui-xiao-zhan-by-demigodliu-wnpk/
class MinStack:
    #* 辅助栈和数据栈同步
    #* 思路简单不容易出错

    def __init__(self):
        ## 我们可以创建两个栈, 一个栈是主栈 stack, 另一个是辅助栈 helper, 用于存放对应主栈不同时期的最小值。
        self.data = []
        self.helper = []

    #! 与不同步解法的不同之处
    ## 只要往「主栈 stack」插入一个元素, 就要在「辅助栈 helper」插入当前时期主栈中所有元素的最小值, 方法就是「辅助栈 helper」栈顶元素与新插入的元素取最小值
    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        ## 因为这里 helper 与 data 元素的数量是相同的, 所以出栈时对两个栈都要操作
        if self.data:
            self.helper.pop()
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]
