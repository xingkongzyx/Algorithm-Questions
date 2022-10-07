""" 
* 162 需要先自己说服自己数组中元素虽然是『无序』的, 但一定包含一个『峰顶』. 而这题是让找出山脉数组的峰顶索引, 提示的最后一条是题目数据保证 arr 是一个『山脉数组』, 也就是『山脉数组』一定是存在的, 直接使用 162 的代码找出『峰顶』就可以了

* 根据题目中的描述, 题目中的描述虽然是「任何」, 英文描述为 any, 实施上「峰顶」是唯一的；
* 在 arr[mid] < arr[mid + 1] 的时候, mid 以及 mid 的左边一定不存在山脉数组的「峰顶」, 封顶只可能存在于下标区间 [mid + 1..right] , 此时设置 left = mid + 1; 
* 使用排除法, 上述情况的反方向就是在下标区间 [left..mid] 里查找答案, 此时设置 right = mid。
? Link: https://suanfa8.com/binary-search/solutions-1/0852-peak-index-in-a-mountain-array
"""
class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
