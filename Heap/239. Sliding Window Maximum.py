""" 
> 优先队列: 要求的最大值必须在窗口中. 所以 如果最大值不在窗口中, 说明窗口已经 过了这个最大值所在的位置, 即最大值在窗口的左侧, 应该弹出.
? https://leetcode.cn/problems/sliding-window-maximum/solution/you-xian-dui-lie-zui-da-dui-dan-diao-dui-dbn9/
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxheap = MaxHeap()
        if len(nums) <= k:
            return [max(nums)]

        # * 初始时，我们将数组 nums 的前 kk 个元素放入 heap 中。
        for i in range(k):
            maxheap.insert((nums[i], i))

        res = [maxheap.peek()[0]]

        # * 每当我们向右移动窗口时，我们就可以把一个新的元素放入优先队列中，此时堆顶的元素就是堆中所有元素的最大值。
        for j in range(k, len(nums)):

            curNum = nums[j]
            maxheap.insert((curNum, j))

            # # 但是当前的堆顶元素可能并不属于当前的「滑动窗口」，在这种情况下，这个堆顶元素在数组 nums 中的位置出现在「滑动窗口」左边界的左侧, 而「滑动窗口」的范围是 [j-k+1, j]。所以我们要不断地从堆中移除不属于当前「滑动窗口」的堆顶的元素，直到某个堆顶元素确实出现在「滑动窗口」中。此时，这个堆顶元素就是当前「滑动窗口」中的最大值。
            while maxheap.peek()[1] < (j - k + 1):
                maxheap.remove()
            # * 将当前「滑动窗口」中的最大值加入 res
            res.append(maxheap.peek()[0])

        return res


class MaxHeap():
    def __init__(self):
        self.data = []

    def insert(self, val):
        self.data.append(val)
        self.siftUp(self.size - 1)

    @property
    def size(self):
        return len(self.data)

    def siftUp(self, curIdx):
        while curIdx > 0:
            parentIdx = (curIdx - 1) // 2
            if self.data[parentIdx][0] < self.data[curIdx][0]:
                self.swap(parentIdx, curIdx)
                curIdx = parentIdx
            else:
                break

    def remove(self):
        maxVal = self.data[0]
        self.swap(0, self.size - 1)
        self.data.pop()
        self.siftDown(0)
        return maxVal

    def siftDown(self, parIdx):
        while 2 * parIdx + 1 < self.size:
            childOneIdx = 2 * parIdx + 1
            childTwoIdx = 2 * parIdx + 2
            idxToSwap = childOneIdx
            if childTwoIdx < self.size and self.data[childOneIdx][0] < self.data[childTwoIdx][0]:
                idxToSwap = childTwoIdx

            if self.data[idxToSwap][0] > self.data[parIdx][0]:
                self.swap(idxToSwap, parIdx)
                parIdx = idxToSwap
            else:
                break

    def swap(self, idx1, idx2):
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]

    def peek(self):
        return self.data[0]


Solution().maxSlidingWindow([9, 10, 9, -7, -4, -8, 2, -6], 5)
