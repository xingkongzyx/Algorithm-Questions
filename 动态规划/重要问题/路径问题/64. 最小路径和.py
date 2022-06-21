
## 与 62, 63 几乎是一模一样的
#? https://leetcode.cn/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-dong-tai-gui-hua-gui-fan-liu-c/ 
class Solution(object):
    def minPathSum(self, grid):
        """ 
        dp[i][j]: 每次只能向下或者向右移动一步从而到达 grid[i][j] 的最小路经总和
        dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        
        第一行，第一列需要进行初始化
        """
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, cols):
            dp[0][j] = grid[0][j] + dp[0][j-1]
            
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # print(dp)
        
        return dp[rows - 1][cols - 1]
    
grid = [[1,3,1],[1,5,1],[4,2,1]]
Solution().minPathSum(grid)
