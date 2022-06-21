""" 
* 时间复杂度: O((m + n)*log(mn)) 每一次矩阵搜索至多为O(m+n)\，如动图中例子所示，整个二分搜索过程为log(m*n)
* 空间复杂度: O(1)
? 讲解了为什么左上和右下的点不能作为 "搜索乘法表中小于等于mid的元素的数量" 的计算的起点: 从这两个点出发无论是向哪个方向增长性都是单调的，以左上为例，从这个点向下或是向右都是单调递增，每次遍历无法排除其中的一个方向。比如说某个值大于左上的起点，我们无法确定此时是应该向右走还是向下前进，因为它们都满足要求，无法达到快速舍弃一方数据的目的。
? https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/solution/dong-tu-yan-shi-by-xiaohu9527-3k7s/ 
"""
## 这道题在二分搜索方面是与 378 同样的思路，在获取乘法表中小于等于某个数的个数中时，并不需要重新搭建matrix，而是根据每一行每一列都在递增的规律采取与 378 同样的从左下角或者右上角使用 O(n + m) 得到乘法表中小于等于的某个元素的数量
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        left = 1
        right = m * n
        
        while left < right:
            mid = left + (right - left) // 2
            
            count = self.getCount(m, n, mid)
            # print(f"left is {left} mid is {mid} right is {right}, there are {count} elements <= mid")
            if count >= k:
                right = mid
            else:
                left = mid + 1
                
        return left
    def getCount(self, m, n, target):
        i = m
        j = 1
        count = 0
        while i > 0 and j <= n:
            if i * j <= target:
                count += i
                j += 1
            else:
                i -= 1
        return count
        
        
res = Solution().findKthNumber(3,3,5)
print(res)
