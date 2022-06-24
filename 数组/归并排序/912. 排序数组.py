class Solution(object):
    def sortArray(self, nums):
        temp = [0 for _ in nums]
        
        self.mergeSort(0, len(nums) - 1, temp, nums)
        
        return nums
    
    """ 
 * 递归调用的函数的定义是：对 numsArr 在 [left..right] 这个区间范围内使用归并排序
 * 特别注意：区间的边界 left 和 right 都是可以取到的
    """
    def mergeSort(self, leftBound, rightBound, tempArr, numsArr):
        if leftBound == rightBound:
            return
        left = leftBound
        right = rightBound
        mid = (left + right) // 2
        self.mergeSort(left, mid, tempArr, numsArr)
        self.mergeSort(mid + 1, right, tempArr, numsArr)
        
        #* 在前面的代码运行后目前 [left, mid] 以及 [mid+1, right] 都是有序的，下面需要合并有序数组。合并的操作在 tempArr 的辅助下在 numsArr 上完成
        for i in range(left, right + 1):
            tempArr[i] = numsArr[i]
            
        j = left
        k = mid + 1
        insertPointer = left
        
        while insertPointer <= right:
            if j == mid + 1:
                numsArr[insertPointer] = tempArr[k]
                k += 1
            elif k == right + 1:
                numsArr[insertPointer] = tempArr[j]
                j += 1
            elif tempArr[j] <= tempArr[k]:
                numsArr[insertPointer] = tempArr[j]
                j += 1
            else:
                numsArr[insertPointer] = tempArr[k]
                k += 1
            insertPointer += 1
