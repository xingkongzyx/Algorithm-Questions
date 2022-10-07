class Solution(object):
    def nextGreatestLetter(self, letters, target):
        #! 题目要求找严格大于 j 的第 1 个位置，因此这道题特别像第 35 题，因此搜索范围是 [0, len]，注意，不是 [0, len - 1]。
        left = 0
        right = len(letters)

        while left < right:
            mid = left + (right - left) // 2
            # * 根据排除法「小于等于」一定不是解，所以先写 letters[mid] <= target 这个分支
            if ord(letters[mid]) <= ord(target):
                # * 下一轮搜索区间是 [mid + 1, right]
                left = mid + 1
            else:
                # * 下一轮搜索区间是 [left, mid]
                right = mid

        if left == len(letters):
            return letters[0]
        else:
            return letters[left]


print(Solution().nextGreatestLetter(letters=["c", "f", "j"], target="k"))
