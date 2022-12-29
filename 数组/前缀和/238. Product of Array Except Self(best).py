""" 
* 我们是否真的需要创建2个数组去保存「左边积」「右边积」? 其实 「左边积」、「右边积」 的计算，都是中间计算，没有留存的必要. 可以让 answer 数组先存「左边积」，然后在计算结果值时被覆盖掉. 「右边积」用一个变量保存，在遍历中被使用，用完就更新为新的「右边积」
? https://leetcode.cn/problems/product-of-array-except-self/solution/gan-jue-da-bu-fen-ti-jie-du-shi-tie-dai-ma-jia-fu-/
? https://leetcode.cn/problems/product-of-array-except-self/solution/chu-zi-shen-yi-wai-shu-zu-de-cheng-ji-by-leetcode-/
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1 for _ in nums]

        for i in range(1, len(nums)):
            left_prod = nums[i - 1] * answer[i - 1]
            answer[i] = left_prod

        right_prod = 1
        for j in range(len(nums) - 1, -1, -1):
            answer[j] = answer[j] * right_prod
            right_prod = right_prod * nums[j]

        return answer
