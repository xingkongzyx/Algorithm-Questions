
# ? 必看: 参考了剑指offer 29 的解法, 代码能够统一 https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/mian-shi-ti-29-shun-shi-zhen-da-yin-ju-zhen-she-di/
class Solution(object):
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        top, left = 0, 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        result = []
        while True:
            """ 
            * 从左往右
            * 列在变，列为循环值
            * 从左往右的下一步是往下走，上边界内缩，故 top += 1
            """
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            if top > bottom:
                break
            
            """ 
            * 从上往下，行在变
            * 从上往下的下一步是从右往左，右边界收缩，故 right -= 1
            """
            for j in range(top, bottom + 1):
                result.append(matrix[j][right])
            right -= 1
            
            if left > right:
                break
            """ 
            * 从右向左，列在变
            * 从右往左的下一步是从下往上，下边界收缩，故 bottom -= 1
            """
            for m in range(right, left - 1, -1):
                result.append(matrix[bottom][m])
            bottom -= 1
            
            if top > bottom:
                break
            """ 
            * 从下到上，行在变
            * 从下到上的下一步是从左到右，左边界收缩，故 left += 1
            """
            for n in range(bottom, top - 1, -1):
                result.append(matrix[n][left])
            left += 1
            
            if left > right:
                break
        return result
