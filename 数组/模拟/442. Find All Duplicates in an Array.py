""" 
* 我们知道一个数组有「下标」和「值」两个概念, 根据下标获取到值。
* 本题中, 数组中数字的取值范围 [1, n], 正好与下标的范围 [0, n - 1] 对应。
* 因此, 就有一个思路, 对于遍历到的当前数字 nums[i], 我们将其与下标为"nums[i] - 1" 的位置的数字进行映射（还要能映射回去）。有 "-1" 的原因是因为下标的范围比数组的取值范围小 1, 所以要 "-1" 确保不会越界. 映射方法采用「取反」
! 由于数组的下标范围是 [0, n-1], 我们需要将数 i 放在数组中下标为 i-1 的位置。
「」
 * 上述做法的原理如下: 
 * ➀ 初始时数组 nums 中的整数都是「正数」, 表示尚未被访问；
 * ➁ 当一个整数被访问时, 如果「该整数对应的下标处的元素」是正数, 则该整数尚未被访问, 因此将「该整数对应的下标处的元素」改成其相反数, 相反数是负数, 表示被访问了一次；
 * ➂ 当一个整数被访问时, 如果「该整数对应的下标处的元素」是负数, 则该整数已经被访问, 因此说明该整数是被「第二次」访问, 即该整数是出现两次的整数。


? https://leetcode.cn/problems/find-all-duplicates-in-an-array/solution/by-stormsunshine-ojmz/
? https://leetcode.cn/problems/find-all-duplicates-in-an-array/solution/by-fuxuemingzhu-dko5/
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for i in range(len(nums)):
            # * 有可能 nums[i] 在之前的遍历过程中已经是负数, 所以这里要用绝对值
            mappedIdx = abs(nums[i]) - 1
            # * 若发现下标为 mappedIdx 的数字已经是「负数」, 说明 nums[i] 之前已经出现过, nums[i] 就是题目要求找到的「the integer that appears twice」
            if nums[mappedIdx] < 0:
                res.append(abs(nums[i]))
            else:
                nums[mappedIdx] = -nums[mappedIdx]

        return res
