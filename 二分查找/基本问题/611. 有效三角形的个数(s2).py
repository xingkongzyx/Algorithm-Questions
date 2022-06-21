class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        count = 0
        for side1Idx in range(0, len(nums) - 2):
            for side2Idx in range(side1Idx + 1, len(nums) - 1):
                side1 = nums[side1Idx]
                side2 = nums[side2Idx]

                sum = side1 + side2

                left = side2Idx + 1
                right = len(nums) - 1
                # 搜索最后一个小于sum的元素的下标
                while left < right:
                    mid = left + (right - left + 1) // 2
                    if nums[mid] >= sum:
                        # 使用weiwei讲解的排除法思维，如果 nums[mid] >= sum, 因为数组是有序的, 所以 mid 及其右边是不可能存在小于 sum 的值的, 搜索区间变为 [left, mid - 1]
                        right = mid - 1
                    else:
                        # 否则搜索区间为 [mid, right]
                        left = mid
                ''' 
                因为无法确定一定存在小于 sum 的值，所以需要额外的检查，这也是与"搜寻第一个大于等于sum的元素的下标"的不同之处. "搜寻第一个大于等于sum的元素的下标" 这种方法如果不存在的话退出循环时 left 为 side2Idx + 1 从这个index 开始就大于等于 sum 而在目前这种搜索条件下，如果不存在，退出循环后 left = side2Idx + 1，如果不进行判断直接加入count中，计算将有误
                '''
                if nums[left] < sum:
                    count += (left - side2Idx)

        return count
print(Solution().triangleNumber([1,1,3,4]))
