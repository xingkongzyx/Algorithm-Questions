
# ? https://leetcode.cn/problems/reverse-pairs/solution/gui-bing-pai-xu-bian-xing-by-zpy___/
# ? 有动图理解合并过程中计算「翻转对」的方法 https://leetcode.cn/problems/reverse-pairs/solution/miao-sha-by-chefyuan-vfsn/
""" 
/ 思路就是: 将整个数组通过归并的思路不断划分为小的片段, 依次进行合并, 合并的过程中我们保持了左右片段的顺序, 但是无需考虑一个片段内部的元素顺序(即使前后两个子数组内部完成了排序, 但是前后两组的元素相对顺序是不变的，前一组元素一定在先). 而前后两组在前面的合并过程中产生的「翻转对」已经计算完成, 就是下面的leftPairs 和 rightPairs. 我们现在需要做的就是在前后两个有序数组进行合并排序的过程中去统计这两个片段中 a[i] > 2 * b[j] 的个数
"""
class Solution(object):
    def reversePairs(self, nums):
        temp = [0 for _ in nums]
        
        res = self.calculatePairs(0, len(nums) - 1, nums, temp)
        return res
    
    def calculatePairs(self, leftBound, rightBound, nums, tempArr):
        if leftBound == rightBound:
            return 0
        
        left = leftBound
        right = rightBound
        mid = (left + right) // 2
        
        leftPairs = self.calculatePairs(left, mid, nums, tempArr)
        rightPairs = self.calculatePairs(mid + 1, right, nums, tempArr)
        
        count = 0
       
        #> 统计翻转对的时机就是在〖得到左右有序序列〗之后，〖合并左右有序序列〗之前。
        #* 此时左右数组都是升序的，要在合并之前统计「翻转对」
        
        #* i 指向左序列的开头
        i = left
        #* j 指向右序列的开头
        j = mid + 1
        while i <= mid and j <= right:
            #* 如果当前的 nums[i] 能和 nums[j] 构成「翻转对」, 因为此时 nums[i...mid] 是有序的, 说明 nums[i...mid] 这之间所有的元素都可以与 nums[j] 构成「翻转对」, 数量是［mid - i + 1］. 此时需要移动 j 看更大的 nums[j] 还能否与 nums[i...mid] 构成「翻转对」
            if nums[i] > 2 * nums[j]:
                count += (mid - i + 1)
                j += 1
            else:
                #* 当前 nums[i] 不满足「大于 2 * nums[j]」的条件，考察下一个 i 
                i += 1
        
        #* 下面就是合并两个有序数组的操作, 两个有序数组分别是 nums[left:mid] 以及 nums[mid+1, right]
        for i in range(left, right + 1):
            tempArr[i] = nums[i]
        
        i = left
        j = mid + 1
        insertPointer = left
        
        while insertPointer <= right:
            if i == mid + 1:
                nums[insertPointer] = tempArr[j]
                j += 1
            elif j == right + 1:
                nums[insertPointer] = tempArr[i]
                i += 1
            elif tempArr[i] <= tempArr[j]:
                nums[insertPointer] = tempArr[i]
                i += 1
            else:
                nums[insertPointer] = tempArr[j]
                j += 1
            insertPointer += 1
        
        return count + leftPairs + rightPairs

print(Solution().reversePairs([2,4,3,5,1]))
