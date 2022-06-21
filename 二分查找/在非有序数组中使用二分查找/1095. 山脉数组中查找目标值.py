class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        mountainIdx = self.findMountainIdx(mountain_arr)
        # print("mountain idx is ", mountainIdx)
        firstPartRes = self.findFirstPart(mountain_arr, mountainIdx, target)
        # print("first part res is ", firstPartRes)
        if firstPartRes != -1:
            return firstPartRes
        
        secondPartRes = self.findSecondPart(mountain_arr, mountainIdx + 1, target)
        # print("second part res is ", secondPartRes)
        return secondPartRes

    def findMountainIdx(self, mountain_arr):
        left = 0
        right = mountain_arr.length() - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                # 下一轮搜索区间 [mid + 1, right]
                left = mid + 1
            else:
                # 下一轮搜索区间 [left, mid]
                right = mid
        return left

    def findFirstPart(self, mountain_arr, rightIdx, target):
        left = 0
        right = rightIdx
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < target:
                # 因为 [left, right] 是递增区间, 说明 [left, mid] 一定不包含 target, 下一轮搜索区间 [mid + 1, right]
                left = mid + 1
            else:
                right = mid
        val = mountain_arr.get(left)
        return -1 if val != target else left

    def findSecondPart(self, mountain_arr, leftIdx, target):
        left = leftIdx
        right = mountain_arr.length() - 1
        
        # [left, right] 是递减区间
        while left < right:
            mid = (left + right + 1) // 2
            if mountain_arr.get(mid) < target:
                # 因为 [left, right] 是递减区间, 说明 [mid, right] 一定不包含 target, 下一轮搜索区间 [left, mid - 1]
                right = mid - 1
            else:
                # 下一轮搜索区间 [mid, right]
                left = mid
                
        val = mountain_arr.get(left)
        return -1 if val != target else left
