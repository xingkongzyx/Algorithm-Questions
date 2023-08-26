""" 
* left_prod[i] 定义为 i 位置左边 (不包括i位置的值) 的所有数字的乘积
* right_prod[i] 定义为 i 位置右边 (不包括i位置的值) 的所有数字的乘积
* 求解 "product of all the elements of nums except nums[i]." 时就是 left_prod[i] * right_prod[i], 也就是说每个位置的结果，即为它「左边的数的乘积」，乘上它「右边的数的乘积」。

? https://leetcode.cn/problems/product-of-array-except-self/solution/gan-jue-da-bu-fen-ti-jie-du-shi-tie-dai-ma-jia-fu-/
? https://leetcode.cn/problems/product-of-array-except-self/solution/chu-zi-shen-yi-wai-shu-zu-de-cheng-ji-by-leetcode-/
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left_prod = [1 for _ in nums]
        right_prod = [1 for _ in nums]

        # 因为 left_prod[i-1] 记录的乘积是不包含 nums[i-1] 的，所以再乘上 nums[i-1] 就是 i 左边所有数字的乘积
        for i in range(1, len(nums)):
            left_prod[i] = left_prod[i - 1] * nums[i - 1]

        for j in range(len(nums) - 2, -1, -1):
            right_prod[j] = right_prod[j + 1] * nums[j + 1]

        res = [0 for _ in nums]

        for i in range(len(nums)):
            res[i] = left_prod[i] * right_prod[i]

        return res
