
""" 
# 为什么队列中要存放「数组下标」而不是直接存储「数值」, 因为要判断队首的值是否在窗口范围内, 由「数组下标」取值很方便, 而由「数值」取「数组下标」不是很方便。
# 也可以选择加入值, 下面动画链接对应的代码就是加入值的
? python 很清晰的讲解1(必看): https://leetcode.cn/problems/sliding-window-maximum/solution/python-jian-ji-de-dan-diao-dui-lie-jie-f-q56i/
? 很清晰的讲解2: https://leetcode.cn/problems/sliding-window-maximum/solution/you-xian-dui-lie-zui-da-dui-dan-diao-dui-dbn9/

? 有动画, 但队列中储存的是值(不建议): https://leetcode.cn/problems/sliding-window-maximum/solution/zhe-hui-yi-miao-dong-bu-liao-liao-de-hua-7fy5/

/ 时间复杂度: O(n), 其中 n 是数组 nums 的长度。每一个下标恰好被放入队列一次, 并且最多被弹出队列一次, 因此时间复杂度为 O(n)。
/ 空间复杂度: O(k)。我们使用的数据结构是双向的, 因此「不断从队首弹出元素」保证了队列中最多不会有超过 k+1 个元素, 因此队列使用的空间为 O(k)。
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # * 使用双端队列, 并且存入index
        queue = collections.deque()
        res = []
        for i in range(len(nums)):
            # * 如果当前元素大于单调队列中的尾端元素的话：pop单调队列中的尾端元素
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            # * 当单调队列的第一个元素（即最大的元素）不在滑动窗口的范围 [i - k + 1, i]内, 说明该最大元素在当前的窗口之外, 则popleft单调队列中的第一个元素
            if queue[0] <= i - k:
                queue.popleft()
            # * 在当前index >= k - 1的时候（即这时候已经能够构成长度为k的窗口）把单调队列的第一个元素加入到结果中去
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res


print(Solution().maxSlidingWindow([9, 10, 9, -7, -4, -8, 2, -6], 5))
