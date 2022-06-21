""" 
? https://leetcode.cn/problems/search-a-2d-matrix-ii/solution/sou-suo-er-wei-ju-zhen-ii-cong-you-shang-e0vj/

* 以右上角的元素举例，在它下面的元素的值都比他大，在它左边的元素的值都比它小
* 所以 从最右上角的元素开始找, 如果这个元素比target大(这个元素的下边元素会更大), 则说明找更小的, 往左走; 如果这个元素比target小(这个元素的左边元素会更小), 则说明应该找更大的, 往下走。


* 每一步会排除一行或者一列, 矩阵一共有 n 行, m 列, 所以最多会进行 n+m 步。所以时间复杂度是 O(n+m)。


! 与 74. 搜索二维矩阵 不同，本题没有确保「每行的第一个整数大于前一行的最后一个整数」，因此我们无法采取「两次二分」的做法。只能退而求之，遍历行/列，然后再对列/行进行二分。
* 时间复杂度：O(m∗logn) 或 O(n∗logm)
"""
class Solution:
    def searchMatrix(self, matrix, target):
        i = 0
        j = len(matrix[0]) - 1
        
        while i < len(matrix) and j >= 0:
            value = matrix[i][j]
            
            if value == target:
                return True
            elif value >target:
                j -= 1
            elif value < target:
                i += 1
        return False
        
    
res = Solution().searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 1000)
print(res)
