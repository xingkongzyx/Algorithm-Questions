'''
# > 这道题目不是回溯，没有撤销选择这一步骤，这是因为这道题不是说要找到一条路径，所以说当寻找第二条路时原来第一条找过的点可以撤销，重新使用；这道题是要让我们找到所有可达解，所以只要走过的点，就永远不能再走了。

# ? https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/


时间复杂度 O(MN) ： 最差情况下，机器人遍历矩阵所有单元格，此时时间复杂度为 O(MN) 。
空间复杂度 O(MN) ： 最差情况下，Set visited 内存储矩阵所有单元格的索引，使用 O(MN) 的额外空间。

链接：https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/

'''
class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        self.visited = set()

        def helper(currentX, currentY):

            #/ 递归终止条件1：机器人走出界了
            #/ 递归终止条件2：机器人走到一个之前访问过的（因为已经访问过了，所以对于结果‘能够到达多少格子’不能再算一次了）
            #/ 递归终止条件3：数位之和>k了
            if currentX >= m or currentY >= n \
                or parseIdxToNum(currentX) + parseIdxToNum(currentY) > k \
                or (currentX, currentY) in self.visited:
                return 0

            #/ 没有在终止条件返回说明这个cell是有效的，每次的有效情形都需要把坐标记录到已访问数组内
            self.visited.add((currentX, currentY))

            #/ 递归计算这个cell下方和右侧有几个cell可以被返回
            bottomMoves = helper(currentX + 1, currentY)
            rightMoves = helper(currentX, currentY + 1)
            #/ 最后加上这个current cell 一起返回
            #! 至于为什么只向右和向下扩张是因为不用回溯已走过的路径，扩张的路径只会向下或者向右
            return 1 + bottomMoves + rightMoves

        def parseIdxToNum(num):
            numStr = str(num)
            sum = 0
            for numChar in numStr:
                sum += int(numChar)
            return sum
        helper(0, 0)
        return self.visited

s = Solution()
m = 2 
n = 3
k = 100
print(s.movingCount(m, n, k))