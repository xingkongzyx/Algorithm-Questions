""" 
> 这道题与 797 一起看, 797 是「有向无环」图, 因此从起始顶点开始, 按照某条路径遍历下去『不可能』回到某个已经遍历过的节点, 不用怕进入死循环。而这道题是「有向有环」图, 从起始顶点开始, 按照某条路径遍历下去『有可能』回到某个已经遍历过的节点, 造成死循环, 所以需要 visited 数组

? 代码随想录: https://leetcode.cn/problems/keys-and-rooms/solution/dai-ma-sui-xiang-lu-841-yao-chi-he-fang-8mlei/
? 使用 set 的解法: https://leetcode.cn/problems/keys-and-rooms/solution/shou-hua-tu-jie-you-xiang-tu-de-bian-li-yi-jing-ge/

/ 时间复杂度: O(n+m), 其中 n 是房间的数量, m 是所有房间中的钥匙数量的总数。
/ 空间复杂度: O(n), 其中 n 是房间的数量。主要为栈空间的开销。

? 来源: https://leetcode.cn/problems/keys-and-rooms/solution/yao-chi-he-fang-jian-by-leetcode-solution/

"""


class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        # # count 单纯是用于输出的
        def DFS(curRoom, count):
            # * 递归终止条件: 如果当前房间已访问过, 直接返回, 避免「死循环」
            if visited[curRoom] == True:
                return
            # * 单层处理逻辑: 标记当前房间为「已访问」状态, 总的访问房间数加1。然后对当前房间能够解锁的其余房间继续进行 DFS 遍历。
            visited[curRoom] = True
            nonlocal numOfVisitedRooms
            numOfVisitedRooms += 1

            print(
                f"{'  ' * count} visiting {curRoom}, total visit {numOfVisitedRooms} rooms")

            #! 这里不需要进行 visited[unlockedRoom] 的判断, 因为我们在终止条件中再进行判断
            for unlockedRoom in rooms[curRoom]:
                DFS(unlockedRoom, count + 1)

        numOfVisitedRooms = 0
        visited = [False for _ in rooms]
        DFS(0, 0)
        if numOfVisitedRooms == len(rooms):
            return True

        return False
