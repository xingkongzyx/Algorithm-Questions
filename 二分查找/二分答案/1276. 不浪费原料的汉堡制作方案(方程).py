class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """ 
*        解二元一次的方程
*        设 Jumbo Burger 数量为x
*        设 Small Burger 数量为y
*        4x + 2y = tomatoSlices
*        x + y = cheeseSlices
*        
*        x = tomatoSlices // 2 - cheeseSlices
*        y = cheeseSlices - x
        """
        #! 解这个方程最关键的一点就是 tomatoSlices % 2 得是0，确保了这点就能保证后面的x和y都是整数，再检查x和y是否大于等于0，如果有小于0的情况，说明是无法制作的
        if tomatoSlices % 2 == 0:
            x = tomatoSlices // 2 - cheeseSlices
            y = cheeseSlices - x
            
            if x < 0 or y < 0:
                return []
            return [x, y]
        
        return []
