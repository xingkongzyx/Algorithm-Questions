""" 
> 稳定的排序: 数值相同的元素在排序前后位置不变
/ 在每一层都执行了数组长度这么多次的赋值、比较、再赋值的操作, 而每一层参与比较的元素个数之和与数组的长度相等, 每一层的复杂度是 O(N). 又得出一共有 logN 层, 总体的时间复杂度是 O(N*logN)
/ 辅助数组的长度为 N, 递归使用到的栈的大小为 log(N), O(N+log(N))=O(N)
"""


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

        # * 在前面的代码运行后, [left, mid] 以及 [mid+1, right] 都是有序的, 下面需要合并这两个有序数组。合并的操作在 tempArr 的辅助下在 numsArr 上完成
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
