from collections import deque
class Solution(object):
    #> 每个点只需要访问一次，因为如果该点不能跳到0，那么通过其他跳法跳到该点也不能跳到0，所以每访问一个点我们就需要记录一次。也就是代码中的visited[idx] = True
    def canReach(self, arr, start):
        visited = [False for _ in range(len(arr))]

        queue = deque([])
        queue.append(start)

        while len(queue) > 0:
            #/ 弹出当前的curPos,如果arr[currentIdx]== 0说明找到了，返回true
            #/ 然后要设置下visited[currentIdx]的属性
            currentIdx = queue.popleft()

            ## 这里相当于DFS中的终止条件
            if currentIdx < 0 or currentIdx >= len(arr) or visited[currentIdx] == True:
                continue
            if arr[currentIdx] == 0:
                return True

            visited[currentIdx] = True
            
            queue.append(currentIdx + arr[currentIdx])
            queue.append(currentIdx - arr[currentIdx])

        return False

arr = [3,0,2,1,2]
start = 2
s = Solution()
res = s.canReach(arr, start)
print(res)