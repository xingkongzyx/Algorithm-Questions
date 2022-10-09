""" 
> 注意跟「右段尾部」比较不用考虑数组本身就是也有序的特殊情况
* 本题与 153 不同的是 - 元素的值可以相同:
* 对于处理元素相同的情况, 一般我们可以通过「递减」right 的索引或者「递加」left 的索引解决
* 例如在 81. 搜索旋转排序数组 II 中我们是通过「递加」left 的索引解决 nums[mid] == nums[left] 的情况
? https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/solution/er-fen-fa-fen-zhi-fa-python-dai-ma-by-liweiwei1419/

 
 #? 综合性讲解 https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/solution/154-find-minimum-in-rotated-sorted-array-ii-by-jyd/
 
 #/ 关于细节很好的讲解(包括为什么要与右段尾部进行比较，而不与左段头部进行比较，明明也有类似的效果？ 为什么变化时right = mid；而left = mid + 1？为什么nums[mid] == nums[right]时，直接将right--，再继续比较就可以，这样不会出现问题吗？): https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/solution/di-zi-dui-guan-fang-ti-jie-er-fen-fa-de-omkrg/
 
 #? 一般性情况的图画: https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/solution/tong-guo-hua-tu-lai-shen-ke-li-jie-er-fen-fa-by-ch/



"""


class Solution:
    def findMin(self, nums) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            print(left, mid, right)
            if nums[mid] > nums[right]:
                # [left, mid] 之间是有序的, 位于第一个递增区间内, mid 及其左边一定不是最小值
                # 下一轮搜索区间 [mid + 1, right]
                left = mid + 1
            elif nums[mid] < nums[right]:
                # [mid, right] 之间是有序的, 位于第二个递增区间内, mid 及其左边有可能是最小值
                # 下一轮搜索区间 [left, mid]
                right = mid
            else:
                """ 
                # 与153相比新增加的情况
                * 结论 3: 当中间数与右边界表示的数相等的时候，看下面两个例子: 

                * 例 5: [0, 1, 1, 1, 1, 1, 1]

                * 例 6: [1, 1, 1, 1, 0, 1, 1]

                * 目标值可能在中间数的左边，也可能在中间数的右边，那么该怎么办呢？很简单，此时你看到的是右边界，就把只右边界排除掉就好了。正是因为右边界和中间数相等，你去掉了右边界，中间数还在，就让中间数在后面的循环中被发现吧。
                # 那有没有可能 mid == right, 因为 "right -= 1" 的移动, 把结果跳过去了呢, 让我们分析下, 是否会出现 mid == right 的情况. 根据我们计算 mid 的公式是下取整, 即使数组只有两个数 [2,2], mid 将会等于 left.  right向前移动并依然能得到正确的最小值. 只有 left = right 例如 [2] 的情况下才有这种可能, 而 left == right 时依据循环结束条件循环已经结束
                """
                right -= 1
        return nums[left]


print(Solution().findMin([2, 2, 2, 0, 2]))
