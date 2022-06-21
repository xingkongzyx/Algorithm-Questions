""" 
/ 1. 递归参数和返回值: 返回当前向左/向右跳跃是否可以到达index 0的位置，返回 true/false
/ 2. 递归终止条件：
/    1) 当此时的跳跃起始位置已经在数组的index 范围外，返回false. 
/    2) 当目前这个index在当前这一轮的已经visit了(visited[startIdx] == True)，返回false。检查visited只有在确定index不出范围时才可以检查。
/    3) 最后，如果到达了对应元素值为 0的下标处，返回true
/ 3. 本层递归: 向左/向右 进行dfs遍历，判断哪个方向可以到达元素值为 0的下标处，有的话直接返回
"""

class Solution(object):
    #> 每个点只需要访问一次，因为如果该点不能跳到0，那么通过其他跳法跳到该点也不能跳到0，所以每访问一个点我们就需要记录一次。也就是代码中的visited[idx] = True. 并且完成左右两边跳跃后也不用进行回溯操作，因为无论什么情况再次访问它就是应该返回False。比如说向左经历了某个index不可以到0，向右再次经历了这个index，此时因为这个index已经访问过，直接返回False就可以
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        visited = [False for _ in range(len(arr))]
        def DFS(startIdx):
            if startIdx >= len(arr) or startIdx < 0 or visited[startIdx] == True:
                return False

            if arr[startIdx] == 0:
                return True

            visited[startIdx] = True

            leftRes = DFS(startIdx - arr[startIdx])
            if leftRes:
                return True
            rightRes = DFS(startIdx + arr[startIdx])
            if rightRes: 
                return True
            # ! 这里不需要将其恢复为 False, 因为如果这个位置无法到达 0, 那么即使以其他方式再次到达这个位置还是无法到达0. 所以再次到达这个位置时直接跳过就可以
            # visited[startIdx] = False

            return False

        return DFS(start)


arr = [4,2,3,0,3,1,2]
start = 0
s = Solution()
res = s.canReach(arr, start)
print(res)