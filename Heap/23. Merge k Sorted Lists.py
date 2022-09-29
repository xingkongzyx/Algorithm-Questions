""" 
* 思路分析：
* 1、由于是 k 个排序链表, 那么这 k 个排序的链表头结点中 val 最小的结点就是合并以后的链表中最小的结点；
* 2、然后最小结点所在的链表的头结点就要更新了, 更新成最小结点的下一个结点（如果有的话）, 此时还是这 k 个链表, 这 k 个排序的链表头结点中 val 最小的结点就是合并以后的链表中第 2 小的结点。

? https://leetcode.cn/problems/merge-k-sorted-lists/solution/tan-xin-suan-fa-you-xian-dui-lie-fen-zhi-fa-python/

/时间复杂度: 假设 k 是链表个数, 考虑优先队列中的元素不超过 k 个, 那么插入和删除的时间代价为 O(logk), 假设链表中所有中元素的个数为 n 个, 对于每个点都被插入删除各一次, 故总的时间代价即渐进时间复杂度为 O(n*logk)。
/ 空间复杂度：这里用了优先队列, 优先队列中的元素不超过 k 个, 故渐进空间复杂度为 O(k)。

"""
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        dummyHead = ListNode(0)
        k = len(lists)

        if k == 0:
            return dummyHead.next

        minHeap = MinHeap()

        #! minHeap 中记录的是一个tuple, 其中包含(arrIdx, 对应链表lists[arrIdx]中的元素位置, 对应链表lists[arrIdx]中的元素位置的value: elementVal)
        # * 他的初始值是 arrs 中的每个 array 中的 first element(index 0)
        for i in range(k):
            # > 这个判断用于通过 "lists = [[]]" 的测试
            if lists[i] != None:
                minHeap.insert((i, lists[i], lists[i].val))

        current = dummyHead

        while minHeap.size > 0:
            smallestItem = minHeap.remove()
            arrIdx, linkedListNode, _ = smallestItem
            current.next = linkedListNode
            current = current.next

            # * 同样不要忘记判断到链表末尾结点的时候就不能再将其放入 heap 中
            if linkedListNode.next != None:
                # * 刚刚出列的那个链表的下一个结点成为新的链表头结点加入优先队列
                linkedListNode = linkedListNode.next
                minHeap.insert((arrIdx, linkedListNode, linkedListNode.val))
            else:
                continue

        # finalHead = dummyHead.next
        # while finalHead != None:
        #     print(finalHead.val)
        #     finalHead = finalHead.next
        return dummyHead.next


class MinHeap:
    def __init__(self):
        self.heap = []

    @property
    def size(self):
        return len(self.heap)

    def insert(self, val):
        self.heap.append(val)
        self.siftUp(self.size - 1)

    def siftUp(self, currentIdx):
        while currentIdx > 0:
            parentIdx = (currentIdx - 1) // 2
            if self.heap[currentIdx][2] < self.heap[parentIdx][2]:
                self.swap(currentIdx, parentIdx)
                currentIdx = parentIdx
            else:
                break

    def remove(self):
        removedItem = self.heap[0]
        self.swap(0, self.size - 1)
        self.heap.pop()
        self.siftDown(0)
        return removedItem

    def siftDown(self, currentIdx):
        endIdx = self.size - 1
        while currentIdx * 2 + 1 <= endIdx:
            childOneIdx = currentIdx * 2 + 1
            childTwoIdx = currentIdx * 2 + 2
            childIdxToSwap = childOneIdx

            if childTwoIdx <= endIdx and self.heap[childOneIdx][2] > self.heap[childTwoIdx][2]:
                childIdxToSwap = childTwoIdx

            if self.heap[childIdxToSwap][2] < self.heap[currentIdx][2]:
                self.swap(childIdxToSwap, currentIdx)
                currentIdx = childIdxToSwap
            else:
                break

    def peek(self):
        return self.heap[0]

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(5)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

head3 = ListNode(2)
head3.next = ListNode(6)
Solution().mergeKLists(lists=[head1, head2, head3])
