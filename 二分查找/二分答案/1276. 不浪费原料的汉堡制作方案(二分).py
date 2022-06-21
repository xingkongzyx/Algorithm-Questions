class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        #* 假设最多能做的 Jumbo Burger 的数量是 [0, right] 个
        left = 0
        right = tomatoSlices // 4
        
        #* 获取使用的 tomatoSlices 恰好 [大于等于提供的 tomatoSlices] 时可以制作的Jumbo Burger数量
        while left < right:
            #* mid 代表在本轮循环中可以制作的 Jumbo Burger 的数量 
            mid = left + (right - left) // 2
            #* 根据 cheeseSlices 与两种burger之间的需求关系，可以得知在制作 mid 个 Jumbo Burger 的基础上可以制作 numOfCheese 个 cheeseBurger
            numOfCheese = cheeseSlices - mid
            neededTomatoSlices = self.neededTomatoSlices(mid, numOfCheese)
            
            #* 如果目前制作两种burger所需的 tomatoSlices 小于提供的 tomatoSlices，则说明 mid 以及 mid 左边都不是答案，下一轮搜索区间 [mid + 1, right]
            if neededTomatoSlices < tomatoSlices:
                left = mid + 1
            else:
                right = mid
        
        #* 出循环后 left 代表 "使用的 tomatoSlices 恰好大于等于提供的 tomatoSlices" 时最多能做的 Jumbo Burger的数量，因为最开始的搜索区间就是[0, tomatoSlices // 4], 所以不用检查 left < 0 的情况
        if self.neededTomatoSlices(left, cheeseSlices - left) == tomatoSlices:
            return [left, cheeseSlices - left]
        else:
            return []
        
        
    def neededTomatoSlices(self, numOfJumbo, numOfCheese):
        return 4 * numOfJumbo + 2 * numOfCheese
Solution().numOfBurgers(tomatoSlices = 16, cheeseSlices = 7)
