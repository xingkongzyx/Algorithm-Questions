""" 
/ 时间复杂度: O(n^2)，其中 n 是三角形的行数。
/ 空间复杂度: O(1)。我们在 triangle上原地进行的操作
? 链接：https://leetcode.cn/problems/triangle/solution/san-jiao-xing-zui-xiao-lu-jing-he-by-leetcode-solu/
"""
class Solution(object):
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]
        res = float('inf')
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                #* 我们在第 i 行的最左侧时，我们只能从第 i−1 行的最左侧移动过来
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                #* 我们在第 i 行的最右侧时，我们只能从第 i−1 行的最右侧移动过来(也就是左上方的位置 triangle[i-1][j-1])
                elif i == j:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] = min(triangle[i-1][j], triangle[i-1][j-1]) \
                                        + triangle[i][j]
                if i == len(triangle) - 1:
                    res = min(res, triangle[i][j])
        return res        
        

print(Solution().minimumTotal(triangle = [[-19]]))
                    