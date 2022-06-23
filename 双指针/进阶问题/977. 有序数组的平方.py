""" 
> 最关键的点就是：原数组中的元素平方最大值一定产生在原数组的最左边或者最右边。
? 进行解释的文章: https://leetcode.cn/problems/squares-of-a-sorted-array/solution/shuang-zhi-zhen-by-du-tu-9-gxo5/
"""
class Solution(object):
    def sortedSquares(self, nums):
        
        #* 创建一个新数组，存储平方值
        result = [0 for _ in nums]
        #* 左指针，指向原数组最左边
        left = 0
        #* 右指针，指向原数组最右边
        right = len(nums) - 1
        #* 得到元素值平方值，从新数组最后位置开始写
        index = len(nums) - 1
        #! 这里使用等于，只有等于符号才能让 left, right 双指针一起遍历 nums 中所有元素并且给 result array 赋值
        while left <= right:
            leftNumSquare = nums[left] ** 2
            rightNumSquare = nums[right] ** 2
            #* 如果原数组的左指针对应的平方值大于右指针，那么往新数组最后位置写入左指针对应的平方值
            if leftNumSquare > rightNumSquare:
                result[index] = leftNumSquare
                left += 1
            else:
                result[index] = rightNumSquare
                right -= 1
                
            index -= 1
        
        return result
