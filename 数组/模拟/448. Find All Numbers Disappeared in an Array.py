"""
* 根据题目特点, 可以把数组中的「元素」与「索引」建立一一对应的关系。因为「索引」是确定的, 范围是[0, n-1], 一个也不缺, 而数组的「元素」是不确定的, 少了哪个也不知道。
* 既然两者是一一对应的关系, 那么我们在第一次遍历过程中对数组中的每个「元素」对应的「索引」做个标记；"当前元素对应的索引 = 当前元素的值 - 1", 然后把「当前元素对应的索引」这个位置的值变为负数, 代表其对应的「元素值」已经被访问过。

* 然后再对数组进行一次遍历, 如果所有的元素值都是负数, 说明原数组已经包含了 [1, n] 范围内的所有数字, 所以每个数字对应的「索引位置」的「值」都被改成了负数。
* 如果某个元素值不是负数, 说明这个「位置」或者说「索引」没有被访问过,
! 注意这里并不是说当前遍历到的元素是缺失的数字。而是用于映射这个「索引」的「元素值」没有被遍历到, 这个「元素值」就是题目求的『缺失的数字』, 根据公式, 当前元素的值 = 当前元素对应的索引 + 1。
* 相反, 
? https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/solution/yi-zhang-dong-tu-bang-zhu-li-jie-yuan-di-uign/
? https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/solution/bu-xu-yao-e-wai-kong-jian-si-lu-chao-ji-qing-xi-bu/
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        res = []
        # * 遍历下数组的元素, 对对应的索引位置的元素作标记
        for i in range(len(nums)):
            # * 由于数组的元素有可能被 "*-1", 所以取绝对值
            mappedIdx = abs(nums[i]) - 1
            if nums[mappedIdx] > 0:
                nums[mappedIdx] *= -1

        # * 寻找没有标记的索引位置
        for j in range(len(nums)):
            if nums[j] > 0:
                # *将索引转化为对应的元素并加入结果数组
                res.append(j + 1)

        return res
