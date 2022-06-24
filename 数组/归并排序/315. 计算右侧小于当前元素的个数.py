
#* 因为计算的是 一个数后面有多少个数比他小，所以只能在合并的过程中「数出每一个数后面有多少数比它小」而不能像 剑指offer 51 那样数出「每一个数前面有多少个数比他大」
#? https://leetcode.cn/problems/count-of-smaller-numbers-after-self/solution/4chong-jie-fa-yi-wang-da-jin-pai-xu-shu-5vvds/
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #* 用于储存最后的结果
        result = [0 for _ in nums]
        
        #* 将原数组 nums 变成 (num, idx) 的形式，用于在合并排序过程中能够计算小于 nums[i] 的数量并在即使 nums 有重复的情况下将其放在正确的 result 位置上
        
        copy = [[num, idx] for idx, num in enumerate(nums)]
        tempArr = [[0,0] for _ in nums]
        self.mergeSort(0, len(copy) - 1, copy, tempArr, result)
        
        return result
    
    def mergeSort(self, leftBound, rightBound, arr, tempArr, result):
        if leftBound == rightBound:
            return 
        
        left = leftBound
        right = rightBound
        mid = left + (right - left) // 2
        # 对左子数组的内部 统计各个元素的右侧小于当前元素的个数，并进行排序操作
        self.mergeSort(left, mid, arr, tempArr, result)
        # 对右子数组的内部 统计各个元素的右侧小于当前元素的个数，并进行排序操作
        self.mergeSort(mid + 1, right, arr, tempArr, result)

        
        #* 合并阶段
        for i in range(left, right + 1):
            tempArr[i][0] = arr[i][0]
            tempArr[i][1] = arr[i][1]
            
        #* 分别指向两个子数组(我们通过 mid 达到分离两个子数组的目的)的起始元素
        i = left
        j = mid + 1
        insertPointer = left
        
        while insertPointer <= right:
            if i == mid + 1:
                arr[insertPointer][0] = tempArr[j][0]
                arr[insertPointer][1] = tempArr[j][1]
                j += 1
            elif j == right + 1:
                arr[insertPointer][0] = tempArr[i][0]
                arr[insertPointer][1] = tempArr[i][1]
                result[tempArr[i][1]] += (j - mid - 1)
                i += 1
            elif tempArr[i][0] <= tempArr[j][0]:
                arr[insertPointer][0] = tempArr[i][0]
                arr[insertPointer][1] = tempArr[i][1]
                result[tempArr[i][1]] += (j - mid - 1)
                i += 1
            else:
                arr[insertPointer][0] = tempArr[j][0]
                arr[insertPointer][1] = tempArr[j][1]
                j += 1
            insertPointer += 1

print(Solution().countSmaller(nums = [-1,-1]))
