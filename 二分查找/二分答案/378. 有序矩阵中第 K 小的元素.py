""" 
> 这道题难点在于弄明白 "为什么二分查找得到的结果一定在矩阵中"
* 我们先看 getCount 函数. getCount 函数的目的是统计矩阵里小等于 mid 的元素数目count. 再判断count 和 k的关系.因为 mid = (l + r) / 2 这种划分方法是把矩阵划分成了[left , mid] 与[mid + 1, right] 两部分. 当 count < k 时, 说明 mid 太小了, 我们应该在 [mid + 1, right] 这个范围里查找. 否则在 [left, mid] 范围里查找.
* 如果存在一个不在矩阵中的数 a 满足条件(矩阵中小于等于 mid 的数正好有 k 个), 因为 a 不在矩阵中,那 count 统计的元素肯定都是小于 a 的(因为 count 统计的是在矩阵中的元素, 而 a 不在矩阵中), ✌ 那一定存在一个比 a 小且在矩阵中的数 b 满足条件, 即从小于 a 的数变成了小于等于 b 的数. ✌ 等用题目中的例子, x = 13 和 x = 14 都满足小于等于 x 的元素数目等于 8, 对 14 来说统计的是小于它的数(因为它不在矩阵中), 而对13来说统计的都是小于等于它的数(因为13在矩阵中). 问题来了, 那为何取到的不是 14 而是 13 呢?
# 👑 因为我们取mid的取法是 mid = (left + right) / 2, 当 left < right时, mid 永远 取不到right, 想要mid取到right ,只有left == right. 但循环条件是 while(left < right), 当 left == right时循环已经终止.  所以我们得到会是一个左边界. 还是用题目中的例子, 假设left = 13, right = 14 则 mid = (13 + 14) / 2 = 13

? 来自底下JOxygen的评论: https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/

/ 或者说在 [left, right] 中符合条件 - "count(矩阵中小于等于它的数)==k" 的数可能会有多个, 这些数中, 最小的那个(设为a)一定在矩阵中(见上面说明), 对于任意整数i(i<a) , count(i)<k, 直到i等于a时, count将第一次等于k。如果先出现了 count(mid)==k 并且 mid 不在 matrix 中且大于 a, 二分搜索并不会停止而是而是缩小搜索区间为 [left, mid], 因为这里的二分搜索的目标就是找到第一个使 count==k 的位置。而第一个位置一定是 matrix 本身的一个元素 a

/ 另一个理解: 可以把这个二分法理解为 “找到矩阵中大于等于k个数的最小整数” 注意是“最小整数”，所以这个数只要小一点点都会不满足条件，意味着这个数肯定是数组内的某一个数。这样理解的原因是因为: 就算找到了刚好 count(大于等于mid) = k 的数时, right依然会向左缩, 即将mid缩小, 循环终止的条件是right缩到极限同时也满足条件, 而不是刚好找到 count(大于等于mid) = k 的数。

* 二分查找先猜一个数 a ，然后遍历整个矩阵: 
* 𝟭. 如果小于等于 a 的元素的个数严格小于(<)k 个，说明猜的这个数太小了，正确的答案比 a 大;                        🌛下一轮搜索区间 [mid + 1, right]
* 𝟮. 如果小于等于 a 的元素的个数恰好等于(=)k 个，说明猜的这个数有可能是正确的答案，但是也有可能不是。如果不是，正确答案只可能比 a 小，但是一定不会比 a 大(这一点大家可以举例说明，我们放在题解的最后说);   🌛下一轮搜索区间 [left, mid]
* 𝟯. 如果小于等于 a 的元素的个数严格大于(>)k 个，说明猜的这个数太大了，正确的答案比 a 小。                       🌛下一轮搜索区间 [left, mid - 1]
# 根据搜索区间的交集，在下面的代码中把情况二和情况三进行合并, 也就是 "大于等于" 的情况合并在一起进行判断

* 时间复杂度: O(n * log(r-l))，二分查找进行次数为 O(log(r-l))，每次操作时间复杂度为 O(n)。r 和 l 分别代表矩阵的最大值和最小值
* 空间复杂度: O(1)。
"""


class Solution:
    def kthSmallest(self, matrix, k) -> int:
        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:
            mid = left + (right - left) // 2
            print(left, right, mid)
            # * 得到matrix中小于等于 mid 的数有多少个
            count = self.getCount(matrix, mid)
            print(f"mid is {mid}, there are {count} elements <= mid")
            # * 如果 "大于 k" 则说明 mid及其右边一定不包含 kth smallest element，下一轮搜索区间是 [left, mid - 1]
            if count >= k:
                right = mid
            else:
                left = mid + 1

        return left

    # / 寻找 matrix 中 "小于等于 target" 的元素数量
    def getCount(self, matrix, value):
        # * 以行为单位找，找到每一行最后一个 <=mid 的数即知道这一行有多少个数 <=mid
        i = 0
        j = len(matrix[0]) - 1
        count = 0
        while i < len(matrix) and j >= 0:
            if matrix[i][j] <= value:
                # // 第 i 行有 j+ 1 个元素 <=mid
                count += j + 1
                i += 1
            else:
                j -= 1
        return count


print(Solution().kthSmallest(
    matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 18]], k=8))
