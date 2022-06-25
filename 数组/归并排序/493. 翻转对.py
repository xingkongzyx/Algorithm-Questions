class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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
        """ 
        > 在归并之前进行翻转对的数量统计即可。
        ? https://leetcode.cn/problems/reverse-pairs/solution/gui-bing-pai-xu-bian-xing-by-zpy___/
        ? 有动图 https://leetcode.cn/problems/reverse-pairs/solution/miao-sha-by-chefyuan-vfsn/
        问题就变成了给出A1，A2两个数组，求A1中数值大于两倍的A2中数值的总个数。
        假如这时候A1，A2都是无序的，那我们还是要暴力遍历去解决。但如果他们都是有序的，我们就可以在线性时间内解决这个问题了。（我们也可以用二分查找来解决，但是时间复杂度就是线性对数的了。）
        1. 初始化两个指针i，j分别指向A1，A2的头部
        2. 如果A1[i] > 2*A2[j],那么A1[i]及A1[i]后面的所有元素都符合要求，更新答案并后移j
        3. 否则，后移i
        4. 接下来我们需要合并A1，A2以备解决后面更大的子问题使用
        5. 返回我们的答案
        https://leetcode.cn/problems/reverse-pairs/solution/cjavapython3-gui-bing-pai-xu-by-yanghk/

        """
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if nums[i] > 2 * nums[j]:
                count += (mid - i + 1)
                j += 1
            else:
                i += 1
        
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
