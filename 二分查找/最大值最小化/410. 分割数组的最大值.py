""" 
! 通过调整「子数组各自的和的最大值」来达到：使得它对应的「子数组的分割数」恰好等于 m 的效果
* 题目给了条件「非负整数」, 以及 n 和 m 的范围 1 ≤ n ≤ 1000 与 1 ≤ m ≤ min(50, n), 「非负整数」这个前提是很重要的。

* 很不错的问提问: 我们讨论 curNumOfSubarrays 和 m 的大小关系时, 一般不是用排除法吗, 先把不是解的情况判断一下, 这里为什么我先判断小于就不对呢, curNumOfSubarrays小于 m 的话, 对应的 mid 也一定不是解啊, 而且我也把 mid 向上取整了, 代码如下. 这样为什么不对呢? 
/        if curNumOfSubarrays < m:
/            right = mid-1;
/        else:
/            left = mid;
/        
* 答: 原因是不能够把 curNumOfSubarrays == m 划分到「大于」的区间 
? https://leetcode.cn/problems/split-array-largest-sum/solution/er-fen-cha-zhao-by-liweiwei1419-4/860146 
* 上面链接的解答中如果分成三个部分的话, 最后 left, right 可能不会重合, 返回 left 能得到正确答案, 返回 right 就不可以. example: nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], m = 20

? 带注释版 https://leetcode.cn/problems/split-array-largest-sum/solution/er-fen-cha-zhao-by-liweiwei1419-4/492820

/ 时间复杂度: O(n * log(sum - maxn)), 其中 sum 表示数组 nums 中所有元素的和, maxn 表示数组所有元素的最大值。每次二分查找时, 需要对数组进行一次遍历, 时间复杂度为 O(n), 因此总时间复杂度是 O(n* log(sum - maxn))
/ 空间复杂度: O(1)。

"""


class Solution(object):
    def splitArray(self, nums, m):
        sum = 0
        maxNum = nums[0]
        for num in nums:
            sum += num
            maxNum = max(maxNum, num)

        # * 「子数组各自的和的最大值」的下限: 就是每个元素都被当做一个子数组看待, 这样情况「子数组各自的和的最大值」的就是整个数组中最大的元素
        left = maxNum

        # * 「子数组各自的和的最大值」的上限: 就整个数组就是子数组(只有1个子数组), 也就相当于没有划分
        right = sum

        """ 
        * 二分查找逻辑: 
        * 「子数组各自的和的最大值」用 maxSubArraySum 表示, 它的取值范围是 [maxNum, sum]
        * 当 nums 分割成 len(nums) 个子数组时, maxSubArraySum == maxNum
        * 当 nums 分割成 1 个子数组时, maxSubArraySum == sum
        ! 现在把问题反过来求, 不求分割成 m 个子数组对应的 maxSubArraySum, 我们来求当 maxSubArraySum = x 时数组被分割成了多少个子数组, x 的范围就是 [maxNum, sum]
        
        * 当「子数组各自的和的最大值」== x (x是指二分搜索过程中的某个 mid) 时, 
        * ➀ 如果对应的「子数组数目」大于 m, 那就说明「当前子数组各自的和的最大值 x」的值小了, (maxSubArraySum的值越小, nums被分的越细, 子数组越多), 下一轮 x 的搜索区间为 [x+1, sum] 
        * ➁ 如果对应的「子数组数目」小于 m, 那就说明 x 的值大了(maxSubArraySum的值越大, nums被分的越粗, 子数组越少), 下一轮 x 的搜索区间 [maxNum, x-1]
        * ➂ 如果对应的「子数组数目」等于 m, 不能停止搜索, 而是应该继续查找, 使得在满足「子数组数目」等于 m 的情况下, 当前「子数组各自的和的最大值」最小化, 下一轮 x 的搜索区间 [maxNum, x]
        * 上述 ➁➂ 能够合并搜索区间, 在上面两个逻辑交替进行的过程中, 「子数组数目」 通过左右逼近的方式等于 m(这句话是我想说的重点)。

、        """

        while left < right:
            mid = left + (right - left) // 2
            curNumOfSubarrays = self.getNumOfSubarrays(mid, nums)

            # # 如果求得的子数组数目太多, 说明「分割数」太多, 说明「子数组各自的和的最大值」太小, 此时需要将「子数组各自的和的最大值」调大. 下一轮搜索的区间是 [mid + 1, right]
            if curNumOfSubarrays > m:
                left = mid + 1
            else:
                right = mid
        # print(left, right)
        return left

    def getNumOfSubarrays(self, target, nums):
        # * 「子数组数目」至少是 1
        numOfSubarrays = 1

        # * currentSum 记载当前的 subarray 中的和是多少
        currentSum = 0

        for num in nums:
            # * 如果把当前的 num 划分到同一个 subarray 中并导致此时子数组的和(也就是 currentSum) 超过了传入函数的当前的「子数组各自的和的最大值」。则要在在 num 的前面进行切割. 然后从这个元素开始划分出一个新的子数组, 所以子数组的数量增加 1, currentSum 重置用于记录这个新的子数组的和
            if currentSum + num > target:
                numOfSubarrays += 1
                currentSum = num
            else:
                currentSum += num

        return numOfSubarrays


res = Solution().splitArray([3, 2, 3, 1, 2, 4, 5, 5, 6, 7,
                             7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6], 20)
print(res)
