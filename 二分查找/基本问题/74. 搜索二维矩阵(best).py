""" 
* 二维矩阵固定列的「从上到下」或者固定行的「从左到右」都是升序的。因此我们可以使用两次二分来定位到目标位置: 
* 
* 「第一次」二分: 从第 0 列中的「所有行」开始找, 找到合适的行 row
* 「第二次」二分: 从 row 中「所有列」开始找, 找到合适的列 col

* 时间复杂度: O(log(m)+log(n))
* 空间复杂度: O(1)
? 链接: https://leetcode.cn/problems/search-a-2d-matrix/solution/gong-shui-san-xie-yi-ti-shuang-jie-er-fe-l0pq/

! 注意 240 便无法使用这个「二分查找」. 因为这道题有一个条件是 The first integer of each row is greater than the last integer of the previous row. 相当于数组变为一维的话就是有序数组. 而 lc240  中, 假设 matrix = [[1,4,7], [2,5,8], [3,6,9]], target = 5 便无法用这个方法解决. 在这道题(74)当我们获得 targetRow 的时候, 能够确定他前面一行的的数字都比 m[targetRow][0] 小, 而这个行首又是最后一个小于等于 target 的行首, 如果target 存在的话, 一定存在于这一行。但是对于 lc240 来说, targetRow 的上一行也有元素大于行首, 可能存在等于 target 的值

"""


class Solution:
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        if target < matrix[0][0] or target > matrix[rows-1][cols-1]:
            return False

        targetRow = self.searchRow(matrix, target)
        # print("targetRow is ", targetRow)

        # * 如果这个行首等于 target, 直接返回, 因为上面的二分查找判断条件是 "找到最后一个满足 matrix[x][0] <= target 的行号" 可能出现直接等于的情况
        if matrix[targetRow][0] == target:
            return True

        targetCol = self.searchCol(matrix, target, targetRow)
        # print("targetCol is ", targetCol)

        return matrix[targetRow][targetCol] == target

    def searchRow(self, matrix, target):
        rows = len(matrix)
        # * 先找 target 的所在行, 或者说找到「最后一个」满足 matrix[x][0] <= target 的行号
        left = 0
        right = rows - 1

        while left < right:
            mid = left + (right - left + 1) // 2
            # * 使用 weiwei 提到的如果 matrix[mid][0] 大于 target, 说明mid及其之后的元素都不满足条件, 下一轮搜索区间 [left, mid - 1]
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                # * 否则下一轮搜索区间 [mid, right]
                left = mid
        return left

    def searchCol(self, matrix, target, targetRow):
        cols = len(matrix[0])
        # * 再在 targetRow 这一行找 target 的所在列, 这里使用排除法的时候, 无论 if 语句是「大于」还是「小于」, 都可以正确排除，因为「大于」「小于」都不满足要求, 其左侧或者右侧的元素都是下一轮搜索要被排除的区间
        left = 0
        right = cols - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if matrix[targetRow][mid] > target:
                right = mid - 1
            else:
                left = mid
        return left


res = Solution().searchMatrix(
    matrix=[[1, 4, 7], [2, 5, 8], [3, 6, 9]], target=5)
print(res)
