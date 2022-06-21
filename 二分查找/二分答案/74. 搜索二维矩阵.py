""" 
! 用 240. 的写法也能AC, 时间复杂度是 O(N + M)

"""
class Solution:
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = rows * cols - 1
        
        while left < right:
            mid = left + (right - left + 1) // 2
            
            basedRow = mid // cols
            basedCol = mid % cols
            # print(f"mid is {mid} row is {basedRow}, col is {basedCol}, val is {matrix[basedRow][basedCol]} ")
            if matrix[basedRow][basedCol] > target:
                # 下一轮搜索区间[left, mid - 1]
                right = mid - 1
            else:
                left = mid
        
        return matrix[left // cols][left % cols] == target
            
res = Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 300)
print(res)
