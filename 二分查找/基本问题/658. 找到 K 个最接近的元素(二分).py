"""
# 二分法，把 K 个元素当成数组上面一个能够左右滑动的窗口. 因为 x 的值是给定了的, 不管 x 在不在数组里面, x 在数组里面的位置其实是固定的(如果按大小排序的话).
* 那么也就是说,我们需要确定这个窗口的起点 start,使得 [start, start+k-1] 这几个元素对于x满足题意. 那么我们可以用二分查找来算这个起点 start.
? 写的非常好: https://leetcode.cn/problems/find-k-closest-elements/solution/by-iamysw-bid6/
? 视频: https://www.youtube.com/watch?v=o-YDQzHoaKM
"""


class Solution(object):
    def findClosestElements(self, arr, k, x):
        # * 窗口最小的起点为 0
        left = 0
        # * 窗口最大的起点为 len(arr) - k，这样才能保证从这个起点选取长度为 k 的窗口
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left: left + k]
