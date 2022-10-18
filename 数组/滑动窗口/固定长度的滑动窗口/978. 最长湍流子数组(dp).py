
# * 状态 dp[i]表示以 arr[i] 结尾的最长湍流子数组的长度, 注意以 arr[i] 结尾是必须的。
# * 这样我们来分析状态转移方程了:
# *
# * 1）若 arr[i-2], arr[i-1], arr[i]构成一个湍流数组成立, 那么 dp[i]=dp[i-1]+1。通俗点解释就是上一个湍流子数组加上arr[i]后生成的新的湍流数组, 新的湍流数组长度也就是上一个最长湍流子数组的长度 dp[i-1] 加 1. dp[i] = dp[i-1] + 1
# * 2）若湍流数组不成立, 那么我们需要比较 arr[i-1] 与 arr[i] 是否相等来确定 dp[i] 的值。若 arr[i-1] != arr[i],则 dp[i] = 2; 若 arr[i-1] == arr[i], 则 dp[i]=1。
# ? 参考链接：https://leetcode.cn/problems/longest-turbulent-subarray/solution/liang-chong-fang-fa-hua-dong-chuang-kou-huo-dong-t/
# ? 参考链接: https://leetcode.cn/problems/longest-turbulent-subarray/solution/java-chang-gui-dpjie-fa-by-ke-xue-jia-12/

class Solution(object):
    def maxTurbulenceSize(self, arr):
        if len(arr) == 1:
            return 1

        # * 最开始都初始化为 1, 即使全部都是相同的元素, 最大的长度就是它本身
        dp = [1 for _ in range(len(arr))]

        # * 另一个需要初始化的部分, 因为在下面的代码中要判断「以 arr[i] 结尾的子数组」是否可以与前面两个元素构成湍流子数组, 所以需要跟 arr[i-1] 与 arr[i-2] 都进行比较. 相当于从数组的第三个元素进行遍历。
        if arr[0] != arr[1]:
            # * 只要数组中第一个元素不等于数组中第二个元素, 他们俩无论什么大小关系「以arr[1]结尾的最长湍流子数组」的长度都是 2. 否则如果是[9,9], 则 dp[1] 是默认值 1
            dp[1] = 2

        # * 从 arr/dp 的第三位开始进行遍历
        for i in range(2, len(dp)):
            # * 能够与前面两个元素构成湍流子数组
            if (arr[i] > arr[i-1] and arr[i-1] < arr[i-2]) or \
                    (arr[i] < arr[i-1] and arr[i-1] > arr[i-2]):
                dp[i] = dp[i - 1] + 1
            elif arr[i] != arr[i-1]:
                #! 很关键的一点: 以当前元素结尾无法与前两个元素构成更长的湍流子数组. 但如果当前元素与前一个元素不相等, 那它与前一个元素也能构成长度为 2 的 有〚不等关系〛的子数组. 为什么是 2 呢? 当 i 进行下一次遍历时(i += 1), 如果 i(i+=1 后的结果) 与 i-1 i-2 有可以构成湍流子数组, 那个时候 dp[i]=dp[i-1]+1, 我们必须保证 dp[i-1]=2, 也就是这里(下一次循环前)的 dp[i]=2
                dp[i] = 2
        # * 因为 dp 定义是以 nums[i] 结尾, 所以检查以每个元素结尾可能构成湍流子数组的最大值
        return max(dp)


print(Solution().maxTurbulenceSize(
    arr=[1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 1, 1, 1]))
