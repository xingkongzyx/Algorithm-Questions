class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def parseIdxToNum(num):
            numStr = str(num)
            sum = 0
            for numChar in numStr:
                sum += int(numChar)
            return sum
        
        queue = [(0, 0)]
        visited = set()
        while len(queue) > 0:
            currentX, currentY = queue.pop(0)
            if currentX >= m or \
            currentY >= n or \
            parseIdxToNum(currentX) + parseIdxToNum(currentY) > k or \
            (currentX, currentY) in visited:
                continue

            visited.add((currentX, currentY))
            queue.append((currentX + 1, currentY))
            queue.append((currentX, currentY + 1))
        return len(visited)

s = Solution()
m = 2 
n = 3
k = 100
print(s.movingCount(m, n, k))