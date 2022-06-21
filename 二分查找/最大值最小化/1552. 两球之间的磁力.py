""" 
* 一般来说, 查找对象就是题目要求的值, 这里为「任意两球间最小磁力」
* 题中的单调性是「任意两球间最小磁力」越大, 最多能放置的球的个数越少；「任意两球间最小磁力」越小, 最多能放置的球的个数越多, 
* 
* 至于为什么是最多能放置的球的个数, 因为我们要找的是一种可能性, 在某个最小磁力下, 能不能放下 m 个球, 能放下说明最小磁力还能再大, 不能放下则说明最小磁力应该缩小, 这里能不能放下, 就应该用最多能放置的球的个数来判断了。
 """
 
class Solution:
    def maxDistance(self, position, m):
        position.sort()
        #* 「任意两球间最小磁力」的可能值：最小为 1, 最大为最后一个位置与第一个位置的距离的差（这时最多就能放俩球了, 不可能再大了）
        minVal = 1
        maxVal = position[-1] - position[0]

        left = minVal
        right = maxVal
        
        while left < right:
            mid = left + (right - left + 1) // 2
            
            ballsNum = self.calculateBalls(mid, position)
            # print(f"left is {left}, right is {right}, mid is {mid}, balls are {ballsNum}")
            #* 因为题目求的是「最小磁力」最大化的值，所以若当前计算出的「最小磁力」满足条件(正好可以放置 m 个球)，我们要"尝试"将左边界右移，去判断稍大一点「最小磁力」是否满足条件，下一轮搜索区间是 [mid, right]；注意的点是要将当前的「最小磁力」也包含在下一轮的搜索区间，因为它有可能就是所求
            #* 若当前计算出的「最小磁力」下可以放置的球多于 m 个，说明当前的「最小磁力」过小，需要增大「最小磁力」，下一轮搜索区间 [mid + 1, right] 
            #* 为了保证退出循环时 left == right, 将这两个分支合并，得到的下一轮搜索区间是 [mid, right]
            if ballsNum >= m:
                left = mid
            #* 若当前计算出的最小磁力使得可以放置的球个数少于 m 个，说明当前的「最小磁力」过大，需要减少「最小磁力」，下一轮搜索区间 [left, mid - 1] 
            else:
                right = mid - 1
                
        return left
    
    #* 在传入的「任意两球间最小磁力」magForce 下能够放入多少个小球，用 count 表示 
    def calculateBalls(self, magForce, positionArr):
        count = 1
        i = 0
        #* 验证过程使用贪心算法，遍历数组，从最左侧开始，每间隔传入的「任意两球间最小磁力」开始放球，或者说若找到两位置之间的「最小磁力」大于等于传入的 magForce，则可放置的球的数量加 1
        for j in range(1, len(positionArr)):
            currentMagForce = abs(positionArr[j] - positionArr[i])
            if currentMagForce >= magForce:
                count += 1
                i = j
        return count

res = Solution().maxDistance([5,4,3,2,1,1000000000], 2)
print(res)
