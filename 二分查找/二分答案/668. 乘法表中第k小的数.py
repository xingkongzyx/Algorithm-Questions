""" 
! 这道题在二分搜索方面是与 378 同样的思路, 在获取乘法表中小于等于某个数的个数中时, 并不需要重新搭建matrix, 而是根据每一行每一列都在递增的规律采取与 378 同样的从左下角或者右上角使用 O(n + m) 得到乘法表中小于等于的某个元素的数量
? 讲解了为什么左上和右下的点不能作为 "搜索乘法表中小于等于mid的元素的数量" 的计算的起点: 从这两个点出发无论是向哪个方向增长性都是单调的, 以左上为例, 从这个点向下或是向右都是单调递增, 每次遍历无法排除其中的一个方向。比如说某个值大于左上的起点, 我们无法确定此时是应该向右走还是向下前进, 因为它们都满足要求, 无法达到快速舍弃一方数据的目的。
? 外网证明: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/discuss/1580357/C%2B%2BPython-Clean-and-Simple-Solution-w-Detailed-Explanation-or-Binary-Search-with-Proof

? https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/solution/by-fuxuemingzhu-8eq4/

/ 时间复杂度: Time Complexity : O((m+n) * log(m*n)), where m and n are the given input dimensions of multiplication table. We are doing binary search over [1, m*n] which requires O(log(m*n)) and each iteration of binary search takes O(m+n) time for the count function.
/ 空间复杂度: O(1)

"""


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

            """ 
            * 为什么 getCount(m, n, mid)>k时, 是 right=mid, 而不是right=mid-1。 例如当输入 m = 11, n = 13, k = 57时, 正确答案是24(写法是right=mid), 但其实通过计算发现, 在一张11*13的乘法表里面, 小于或等于24的数一共有59个, 与57个对不起来。 那为啥正确答案是24呢? 因为有5种乘法是等于24的, 2*12, 3*8, 4*6, 6*4, 8*3。然后从这 5 种里面删除 2 种, 小于或等于 24 的数就只有 57 个了。然后此时 24 仍然是第 57 小的数。(前一个22是第54小的数). 因此, 当 getCount(m, n, mid)>k 时, 右边界仍然可能是正确答案。因此, 只能用 right=mid, 靠左边界慢慢提升得到最终答案, 而不是 right=mid-1
            """
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


res = Solution().findKthNumber(3, 3, 5)
print(res)
