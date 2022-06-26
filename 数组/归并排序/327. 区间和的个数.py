
#? 整体思路很好的讲解: https://leetcode.cn/problems/count-of-range-sum/solution/fen-zhi-si-xiang-ying-yong-gui-bing-pai-xu-zuo-yi-/
#? 前缀和归并排序为什么不会影响原区间和顺序? https://leetcode.cn/problems/count-of-range-sum/solution/qian-zhui-he-shu-zu-gui-bing-pai-xu-si-lu-by-sunfl/

#> 寻找满足条件的区间和实际上只需要找到任意两个满足差值为[lower, upper]的前缀和就可以，前缀和的顺序无关紧要
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        preSum = [0 for _ in range(len(nums) + 1)]
        
        for i in range(len(nums)):
            preSum[i + 1] = preSum[i] + nums[i]
        
        temp = preSum[:]
           
        count = self.calculateCount(0, len(preSum) - 1, lower, upper, preSum, temp) 
        return count


    def calculateCount(self, leftBound, rightBound, lower, upper, preSumArr, tempArr):
        if leftBound == rightBound:
            return 0
        
        left = leftBound
        right = rightBound
        mid = (left + right) // 2
        
        leftCount = self.calculateCount(left, mid, lower, upper, preSumArr, tempArr)
        rightCount = self.calculateCount(mid + 1, right, lower, upper, preSumArr, tempArr)
        
        currentCount = 0
        
        #> 在合并两个有序数组之前计算区间和的个数
        pLeft = mid + 1
        pRight = mid + 1
        index = 0
        
        #* 这里希望找到满足差值为[lower, upper]的前缀和的个数
        #* 根据公式 "preSum[j] - preSum[i]" lies in [lower, upper], 也就是 lower <= preSum[j] - preSum[i]" <= upper. 其中的 i 是在需要合并的前后两个有序数组的前数组中, j 是在需要合并的前后两个有序数组的后数组中
        #* 将公式转换, 得到『条件1 preSum[j] >= preSum[i] + lower』and『条件2 preSum[j] <= preSum[i] + lower』, preSum[i] 指代的就是下文的 preSum[index], 而为了方便求出满足要求的 preSum[j] 的区间, 我们分别求出 j=pLeft(用于满足条件1) 以及 j=pRight(用于满足条件2), [pLeft, pRight) 区间内的元素就是能够与当前 preSum[index] 组成区间和的元素
        for index in range(left, mid + 1):
            while pLeft <= right and preSumArr[pLeft] < preSumArr[index] + lower:
                #* 希望找到一个 ｢pLeft｣ 使之是满足"preSum[index] + lower <= preSum[pLeft]" 的最小 pLeft, 在 while 循环中就是相当于在 "preSum[index] + lower > preSum[pLeft]" 的时候一直向右移动 pLeft, 直到找到了某一个 pLeft 能够使得其在 preSum 数组对应的元素大于等于 preSum[index] + lower
                pLeft += 1
            while pRight <= right and preSumArr[pRight] <= preSumArr[index] + upper:
                #* 希望找到一个 ｢pRight｣ 使之是满足 "preSum[index] + upper >= preSum[pRight]" 的最大 pRight, 如果找到了 pRight, 则 [pLeft, pRight] 之间的值都是满足要求的. 
                #* 但是在 while 循环中就是相当于在 "preSum[index] + upper >= preSum[pRight]" 的时候一直增加 pRight, 直到找到了第一个 pRight 能够大于 "preSum[index] + upper", 这个时候 pRight 左边的所有元素(不包括pRight)都是满足小于等于"preSum[index] + upper"这个要求的
                pRight += 1
            currentCount += pRight - pLeft
        
        #/ 合并数组，并将其进行排序(这一段与归并排序的代码一模一样)
        for i in range(left, right + 1):
            tempArr[i] = preSumArr[i]
        
        i = left
        j = mid + 1
        insertPointer = left
        
        while insertPointer <= right:
            if i == mid + 1:
                preSumArr[insertPointer] = tempArr[j]
                j += 1
            elif j == right + 1:
                preSumArr[insertPointer] = tempArr[i]
                i += 1
            elif tempArr[i] <= tempArr[j]:
                preSumArr[insertPointer] = tempArr[i]
                i += 1
            else:
                preSumArr[insertPointer] = tempArr[j]
                j += 1
            insertPointer += 1
        
        return leftCount + rightCount + currentCount

print(Solution().countRangeSum(nums = [-2,5,-1], lower = -2, upper = 2))
