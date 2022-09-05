""" 
> 基于 622 的拓展
? https://leetcode.cn/problems/design-circular-deque/solution/shu-zu-shi-xian-de-xun-huan-shuang-duan-dui-lie-by/
"""


class MyCircularDeque:

    def __init__(self, k: int):
        capacity = k + 1
        self.data = [None for _ in range(capacity)]
        """ 
        * rear 指向数组中最后一个有效位置的下一个位置, 也就是在后端下一个插入元素的位置
        * 插入时, 先放入value, 再后移
        * 删除时, 向前移动一位代表删除
        ! 注意取模
        """
        self.rear = 0
        """ 
        * front 指向数组中第一个存放元素的位置
        * 插入时, 先向前移动一位, 再放入value
        * 删除时, 向后移动一位代表删除
        ! 注意取模
        """
        self.front = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.front = (self.front - 1 + len(self.data)) % len(self.data)
        self.data[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.data[self.rear] = value
        self.rear = (self.rear + 1) % len(self.data)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.data)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + len(self.data)) % len(self.data)
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        lastEleIdx = (self.rear - 1 + len(self.data)) % len(self.data)
        return self.data[lastEleIdx]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.data) == self.front


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
