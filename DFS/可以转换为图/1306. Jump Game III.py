""" 
> 与 841 很像，同样需要一个 visited 数组避免死循环，最坏的情况需要遍历整个数组
# 每个点只需要访问一次, 因为如果从该点不能跳到 0, 那么通过其他跳法跳到该点也不能跳到 0, 所以每访问一个点我们标记这个点的 visited[index] 为 True。也就是代码中的visited[idx] = True. 并且完成左右两边跳跃后也不用进行撤回标记(回溯)操作, 因为无论什么情况再次访问它就是应该返回False。比如说向左经历了某个 index 不可以到0, 向右再次到达这个 index, 此时因为这个 index 已经访问过, 直接返回 False 就可以
? 递归树: https://leetcode.cn/problems/jump-game-iii/solution/java-bfs-dfs-qian-xian-yi-dong-fu-shang-mqn6p/
"""


class Solution(object):

    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        visited = [False for _ in range(len(arr))]

        def DFS(curIdx):
            """ 
            * 递归终止条件: 
            * ➀ 当前 curIdx 越界了, 也就是不在 [0,len-1] 范围内
            * ➁ 当前 curIdx 的访问过
            * ➂ 当 arr[curIdx]==0时, 表示找到了
            """
            if curIdx >= len(arr) or curIdx < 0 or visited[curIdx] == True:
                return False

            if arr[curIdx] == 0:
                return True

            visited[curIdx] = True

            leftRes = DFS(curIdx - arr[curIdx])
            if leftRes:
                return True
            rightRes = DFS(curIdx + arr[curIdx])
            if rightRes:
                return True
            # ! 这里不需要将其恢复为 False, 因为如果这个位置无法到达 0, 那么即使以其他方式再次到达这个位置还是无法到达0. 所以再次到达这个位置时直接跳过就可以
            # visited[curIdx] = False

            return False

        return DFS(start)
