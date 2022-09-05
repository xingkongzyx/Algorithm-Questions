""" 
! 必看, 通过 data 数组扩大或者说有意浪费一位从而避免「队列为空」和「队列为满」的判别条件冲突
? https://leetcode.cn/problems/design-circular-queue/solution/shu-zu-shi-xian-de-xun-huan-dui-lie-by-liweiwei141/

"""


class MyCircularQueue(object):

    def __init__(self, k):
        # * front：指向队列头部第 1 个有效数据的位置
        self.front = 0
        # * rear：指向「新来元素」待插入的位置(或者说是从队尾入队的位置)
        self.rear = 0
        # * 创建一个长度为 k + 1 的 circular array
        self.arr = [None] * (k + 1)

    # *  Inserts an element into the circular queue. Return true if the operation is successful.

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        # * 「rear指针」指向的就是待插入元素应在的位置
        self.arr[self.rear] = value
        # * 在这之后更新「rear指针」，要通过取模解决越界的问题
        self.rear = (self.rear + 1) % len(self.arr)
        return True

    # * Deletes an element from the circular queue. Return true if the operation is successful.
    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False

        # * 这里的 deque 并不是使用 pop 方法，而是通过移动「front指针」从而更新「第 1 个有效数据」的位置。同样要注意越界的问题。
        self.front = (self.front + 1) % len(self.arr)

        return True

    # * Gets the front item from the queue. If the queue is empty, return -1.
    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    # * Gets the last item from the queue. If the queue is empty, return -1.
    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        # * last item 在的位置是「rear指针」的前一个位置，要通过「取模」避免 rear 已经「等于0」的情况
        rearEleIdx = ((self.rear - 1) + len(self.arr)) % len(self.arr)
        return self.arr[rearEleIdx]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.front == self.rear

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.rear + 1) % len(self.arr) == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
