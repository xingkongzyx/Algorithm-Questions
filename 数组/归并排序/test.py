class Solution(object):
    def countSmaller(self, nums):
        # if len(nums) < 2:
        #     return 0
        temp = [[0, 0] for _ in nums]
        copy = [[num, idx] for idx, num in enumerate(nums)]
        print(copy)
        result = [0 for _ in nums]
        self.mergeSort(0, len(nums) - 1, copy, temp, result)
        print(result)
        return result
        
    def mergeSort(self, left, right, nums, temp, result):
        if left == right:
            return
        
        mid = (left + right) // 2
        
        self.mergeSort(left, mid, nums, temp, result)
        self.mergeSort(mid + 1, right, nums, temp, result)
        
        # 合并阶段
        for i in range(left, right + 1):
            temp[i][0] = nums[i][0]
            temp[i][1] = nums[i][1]
            
        i = left
        j = mid + 1
        insertPointer = left
        
        while insertPointer <= right:
            if i == mid + 1:
                nums[insertPointer][0] = temp[j][0]
                nums[insertPointer][1] = temp[j][1]
                j += 1
            elif j == right + 1:
                nums[insertPointer][0] = temp[i][0]
                nums[insertPointer][1] = temp[i][1]
                result[nums[insertPointer][1]] += (j - mid - 1)
                i += 1
            elif temp[i] <= temp[j]:
                nums[insertPointer][0] = temp[i][0]
                nums[insertPointer][1] = temp[i][1]
                result[nums[insertPointer][1]] += (j - mid - 1)
                i += 1
            else:
                nums[insertPointer][0] = temp[j][0]
                nums[insertPointer][1] = temp[j][1]
                j += 1
            insertPointer += 1
        # print(nums[left: mid + 1], nums[mid + 1:right + 1], result)    
        # return crossPairs + leftPairs + rightPairs

Solution().countSmaller(nums = [5,2,6,1])
