""" 
> 与「三路快排」的代码思路一模一样, 代码对应视频讲解的第一种方法
 *[0, zeroPointer] 区间内的元素都是 0, zeroPointer 是这个区间的最后一个元素
 *(zeroPointer, i) 区间内的元素都是 1, zeroPointer + 1 是这个区间的第一个元素
 *[twoPointer, len(nums - 1)] 区间内的元素都是 2, twoPointer 是这个区间的第一个元素


/ 时间复杂度: O(N)，这里 N 是输入数组的长度；
/ 空间复杂度: O(1)。
? 文字: https://leetcode.cn/problems/sort-colors/solution/kuai-su-pai-xu-partition-guo-cheng-she-ji-xun-huan/
? 视频 https://leetcode.cn/problems/sort-colors/solution/yan-se-fen-lei-by-leetcode-solution/
"""


class Solution(object):
    def sortColors(self, nums):
        # * 为了保证初始化的时候 [0, zeroPointer] 为空, 设置 zeroPointer = -1,
        # * 所以下面遍历到 0 的时候, 先加, 再交换
        zeroPointer = -1

        # * 为了保证初始化的时候 [twoPointer, len - 1] 为空, 设置 twoPointer = len
        # * 所以下面遍历到 2 的时候, 先减, 再交换
        twoPointer = len(nums)

        i = 0

        # 当 i == two 上面的三个子区间正好覆盖了全部数组, 循环终止条件是 i == twoPointer, 那么循环可以继续的条件是 i < twoPointer

        while i < twoPointer:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                # 当 i 位置上的数字是 0 时, 需要将其与第二个区间(1区间)的第一个位置进行交换, 这样确保了第一个区间(0区间)增加了一个位置
                zeroPointer += 1
                nums[zeroPointer], nums[i] = nums[i], nums[zeroPointer]
                i += 1
            elif nums[i] == 2:
                # 当 i 位置上的数字是 2 时, 需要将其与第二个区间(1区间)的最后一个位置进行交换, 这样确保了第三个区间(2区间)增加了一个位置
                twoPointer -= 1
                nums[twoPointer], nums[i] = nums[i], nums[twoPointer]
                # ! 但是这里不能够更新 i, 因为不能确定交换来的元素是等于0的
        return nums
