""" 
* 时间复杂度: (n)。由于前四个操作的时间复杂度都是 O(1), 而 popMax() 操作在最坏情况下需要将栈中的所有元素全部出栈再入栈, 时间复杂度为 O(n)。因此总的时间复杂度为 O(n)。
* 空间复杂度: (n)。

? https://leetcode.cn/problems/max-stack/solution/max-stack-by-leetcode/

"""


class MaxStack:

    def __init__(self):
        self.main = []
        self.maxStack = []

    def push(self, x: int) -> None:
        self.main.append(x)

        if len(self.maxStack) == 0:
            self.maxStack.append(x)
        else:
            curMax = max(self.maxStack[-1], x)
            self.maxStack.append(curMax)

    def pop(self) -> int:
        self.maxStack.pop()
        return self.main.pop()

    def top(self) -> int:
        return self.main[-1]

    def peekMax(self) -> int:
        return self.maxStack[-1]

    """ 
    * 对于 popMax()，由于我们知道当前栈中最大的元素值，因此可以直接将两个栈同时出栈，并存储第一个栈出栈的所有值。当某个时刻，第一个栈的出栈元素等于当前栈中最大的元素值时，就找到了最大的元素。此时我们将之前出第一个栈的所有元素重新入栈，并同步更新第二个栈，就完成了 popMax() 操作。
    """

    def popMax(self) -> int:
        curMaxVal = self.maxStack[-1]
        helperStack = []

        # * 调用已经写好的 pop 函数使得两个栈同时出栈, 同时使用 helperStack 记录出栈的元素便于之后重新 push 到 main stack 中
        while self.main[-1] != curMaxVal:
            helperStack.append(self.pop())

        self.pop()

        # * 调用已经写好的 push 函数将之前同步出 mainStack 以及 maxStack 栈的所有元素重新入栈, push 函数将为我们自动调整最大值
        while len(helperStack) > 0:
            self.push(helperStack.pop())

        return curMaxVal


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
