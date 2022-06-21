""" 
*「二分」不是单纯指从有序数组中快速找某个数，这只是「二分」的一个应用。

*「二分」的本质是两段性，并非单调性。只要一段满足某个性质，另外一段不满足某个性质，就可以用「二分」。

* lc33 中 经过旋转的数组，显然前半段满足 >= nums[0]，而后半段不满足 >= nums[0]。我们可以以此作为依据，通过「二分」找到旋转点。

* 而 lc81 中 元素并不唯一。这意味着我们无法直接根据与 nums[0] 的大小关系，将数组划分为两段，即无法通过「二分」来找到旋转点。
* 因为「二分」的本质是二段性，并非单调性。只要一段满足某个性质，另外一段不满足某个性质，就可以用「二分」。

! 所以需要做一些预处理，使其单调性恢复
/ 更具体地说: 这道题包含了重复元素其实影响到的是，当左端点和右端点相等时，无法判断mid在左半边有序数组还是右半边有序数组，所以只需要一直pop直到左端点和右端点不相等就可以了。就加上两句话即可：
"""


class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        # ! 最关键的预处理，使得数组单调性恢复，剩下的就是33题了. 使用小于而不是小于等于是为了如果元素全部相同，至少留一个元素进入下面的循环
        while left < right and nums[left] == nums[right]:
            right -= 1
        print(f"缩减后的left, right是{left}, {right}")
        while left <= right:
            mid = left + (right - left) // 2
            # print(f"left Idx is {left}, rightIdx is {right}, mid is {mid}")
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[left]:
                # mid 处于左侧有序增区间
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                # mid 处于右侧有序增区间
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


Solution().search([2, 3, 5, 0, 0, 0, 1, 2], 3)
