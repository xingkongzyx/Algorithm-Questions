
#? https://leetcode.cn/problems/min-stack/solution/min-stack-fu-zhu-stackfa-by-jin407891080/

class MinStack(object):

    def __init__(self):
        #* 有两个 stacks, 一个用于正常的栈的操作, 一个是「辅助栈」, 存放当前的最小值。
        self.stack = []
        self.helperStack = []

    #* 两种情况才会往「辅助栈」放入元素
    #* ➀ 「辅助栈」为空的时候, 必须放入新进来的数；
    #* ➁ 新来的数「小于或者等于」「辅助栈」栈顶元素的时候, 放入元素
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        #! 注意这里必须使用 <=, 否则当有多个元素的值一样且都是最小值时, 如果只加入一个, 当它被 pop 出来后, 再进行 getMin 操作将会报错
        if len(self.helperStack) == 0 or val <= self.helperStack[-1]:
            self.helperStack.append(val)

    #* 出栈的时候,「辅助栈」的栈顶元素等于「数据栈」的栈顶元素, 才出栈。
    def pop(self):
        """
        :rtype: None
        """
        poppedEle = self.stack.pop()
        if poppedEle == self.helperStack[-1]:
            self.helperStack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.helperStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
