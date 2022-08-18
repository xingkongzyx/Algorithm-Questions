
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        numRows = len(maze)
        numCols = len(maze[0])

        def inArea(rowIdx, colIdx):
            return 0 <= rowIdx < numRows and 0 <= colIdx < numCols

        visited = [[False for _ in range(numCols)] for _ in range(numRows)]
        dir_x = [0, 0, 1, -1]
        dir_y = [1, -1, 0, 0]
        minLen = float("inf")
        curPath = []

        def DFS(rowIdx, colIdx, curLen):
            if rowIdx == destination[0] and colIdx == destination[1]:
                # print(curPath, curLen)
                nonlocal minLen
                minLen = min(minLen, curLen)
                return

            for i in range(4):
                newRow = rowIdx
                newCol = colIdx
                dirLen = 0
                while inArea(newRow, newCol) and maze[newRow][newCol] == 0:
                    newRow += dir_x[i]
                    newCol += dir_y[i]
                    dirLen += 1

                newRow -= dir_x[i]
                newCol -= dir_y[i]
                dirLen -= 1
                if visited[newRow][newCol] == False:
                    # curPath.append((newRow, newCol))
                    visited[newRow][newCol] = True
                    DFS(newRow, newCol, curLen + dirLen)
                    # curPath.pop()
                    visited[newRow][newCol] = False

        visited[start[0]][start[1]] = True
        DFS(start[0], start[1], 0)
        return minLen if minLen != float("inf") else -1
