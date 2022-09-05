""" 
> 这道题的本质在于找到数组中的「每一个数」作为「最小值」的「子数组范围」
* 因此只要我们向左找到第一个比 arr[i] 小的数 arr[left] 以及向右找到第一个比 arr[i] 小的数 arr[right], 左右范围内(exclusive)的所有 subarray 都是以 arr[i] 作为最小值的。然后用数学方法算出这个范围内所有经过 arr[i] 的 subarray 的个数, 公式是 ((right - i) * (i - left))。 在一个数组中找左右两边第一个大于、小于、等于的数这种问题可以使用单调栈来解决。
* 维护一个单调递增栈 stack; 当当前数 nums[i] <= nums[stack.top()], 触发计算; 此时形成i和stack[-2]两个小的数字夹住stack[-1]这一个大数字的情况. 因为此时的栈顶元素比栈里的第二个元素大, nums[i] 又是比栈顶元素大 , 那么栈顶元素就是在这两个数之间作为最小值的一个范围

? 必看讲解详细: https://leetcode.cn/problems/sum-of-subarray-minimums/solution/xiao-bai-lang-dong-hua-xiang-jie-bao-zhe-489q/


* 正向思维：
* 1、找到所有的子数组; 
* 2、求出所有子数组的最小值; 
* 3、求出这些最小值的总和; 
*
* 逆向思维：
* 1、找到所有的最小值; 
* 2、找到每个最小值所在的数组的个数
* 3、min * n 之和就是目标
*
* 问题是：
* 如何找到所有的最小值 => 数组中的每个数字都可能是最小值; 
* 那么对于每个最小值 min, 我们要找到这样的数组：a1 > a2 ...> min < an-1 < an (min 是最小的哪一个)
* 这样: 左边有 n 个数, 右边有 m 个数, 那么组合起来就是 n * m;

? https://leetcode.cn/problems/sum-of-subarray-minimums/solution/neng-xiang-dao-de-zui-jian-da-de-zuo-fa-9xl7l/

* 为什么在算 left 的时候是 arr[stack[-1]] >= arr[i], 而在算 right 的时候是 arr[stack[-1]] > arr[i] 呢?
? 答案: https://leetcode.cn/problems/sum-of-subarray-minimums/solution/dan-diao-zhan-python3-by-smoon1989/119581
"""


class Solution:
    def sumSubarrayMins(self, arr) -> int:

        stack = []
        # * 如果当前元素在其右侧没有 next smaller element，为了计算方便将其右边界设定为 len(arr), 这样在以当前元素为最小元素的子数组中右边界的选择个数直接表示为 right[i] - i, 不用苦恼于加一减一的问题
        right = [len(arr) for _ in arr]

        # ! 在计算左边界或者右边界时将一侧设置为求解「大于等于」arr[i] 的元素, 目的是为了解决当一个子数组中有两个一样的最小值元素时(比如[3,1,2,4,1]中有两个1), 不重复且不遗漏地统计每一个子数组。
        # # 向右遍历寻找 arr[i]右边「第一个」比 arr[i] 小于等于的数
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                # 此时 arr[stack[-1]] 元素对应的右边第一个比他小的元素就是 arr[i]
                basedIdx = stack.pop()
                right[basedIdx] = i

            stack.append(i)

        # print(f"right side: ", right)

        # * 如果当前元素在其左侧没有 prev smaller element，为了计算方便将其左边界设定为 -1, 这样在以当前元素为最小元素的子数组中左边界的选择个数直接表示为 i - left[i], 像 arr 中 arr[i] 的对应左边界是 -1, 其子数组左边界选择范围就是 0-(-1) = 1 种, 只有一种选择
        left = [-1 for _ in arr]
        # # 向左遍历寻找 arr[i] 左边「第一个」比 arr[i] 小的数
        stack = []
        for j in range(len(arr) - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[j]:
                basedIdx = stack.pop()
                left[basedIdx] = j
            stack.append(j)
        # print(f"left side: ", left)

        res = 0
        for k in range(len(arr)):
            # * 此处 left[k] 和 right[k] 实际上记录的是「左边界-1」和「右边界+1」, 和上面思路中有些区别, 便于计算
            subArrSum = (k - left[k]) * (right[k] - k) * arr[k]
            res += subArrSum

        return res % 1000000007
