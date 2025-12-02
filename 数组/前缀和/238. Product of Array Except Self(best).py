""" 
* 我们是否真的需要创建2个数组去保存「左边积」「右边积」? 其实 「左边积」、「右边积」 的计算，都是中间计算，没有留存的必要. 可以让 answer 数组先存「左边积」，然后在计算结果值时被覆盖掉. 「右边积」用一个变量保存，在遍历中被使用，用完就更新为新的「右边积」

* 第一个循环使用数组ans[]来存储每个元素左侧元素乘积（从最左侧开始，每次往右乘一个数）。
* 第二个循环不使用数组存储值，直接使用一个变量temp计算右侧元素乘积（从最右侧元素开始，每次往左乘一个数）。然后直接用ans[]*temp来计算最终结果，每一轮计算出temp就计算使用掉然后下一轮更新。
* 最终就只用到两个单层循环和一个数组。

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
