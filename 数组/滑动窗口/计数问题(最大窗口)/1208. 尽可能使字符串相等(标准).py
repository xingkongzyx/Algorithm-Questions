""" 
* 使用滑动窗口的原因: 对于区间 [i, j] ，若当前区间恰好不满足其内 ASCII 码差值和小于等于 cost ，则窗口继续向右拓展 j++ ，一样不会是合法区间。因此只能通过缩减左端点 i++ ，将区间元素删除，这样才能保证该区间 ASCII 码差值和小于等于 cost 成立。符合滑动窗口性质：向右边扩散得到和越来越大，向左边界扩散得到和越来越小。

? 链接：https://leetcode.cn/problems/get-equal-substrings-within-budget/solution/chua-dong-chuang-kou-yan-shi-by-boille-pf2z/

#> 求最大窗口，所以在窗口非法时「收缩窗口」(也就是移动左指针)，并且在「收缩窗口」的判断句外面记录最大窗口。这道题「窗口非法」就是指 currentCost 大于题目所提供的 maxCost
"""
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        ## Step 1: 定义需要维护的变量
        ## 因为是求最大长度，所以有 maxLen, 又同时涉及计算开销 (和求和一个道理)， 所以还要一个 cost
        maxLen = 0
        cost = 0
        ## Step 2: 定义窗口的首尾端 (left, right)， 然后滑动窗口
        left = 0
        right = 0
        #! 每次循环结束时窗口储存的是 s[left...right) 左闭右开区间, 这些s 区间中的字符可以转化成 t 的字符, 并且转换过程中确保现在的转换花费 cost 仍旧 <= maxCost
        while right < len(s):
            
            ## Step 3
            ## 更新需要维护的变量 (cost)
            ## 每一对字符的order差值(注意得是绝对值)就是当前时间点的开销，直接累积在cost上即可
            ## cost只要不超过最大开销，就更新max_len
            currentCharCost = abs(ord(t[right]) - ord(s[right]))
            cost += currentCharCost

            if cost <= maxCost:
                maxLen = max(maxLen, right - left + 1)
            
            ## Step 4
            ## 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            ## 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            ## 当 cost 大于最大开销时候，窗口不合法
            ## 所以需要不断移动窗口左指针直到窗口再次合法 (cost <= max_cost)
                
            while cost > maxCost:
                leftCharReturnedCost = abs(ord(t[left]) - ord(s[left]))
                cost -= leftCharReturnedCost
                left += 1
            
            right += 1
        return maxLen
Solution().equalSubstring("krrgw", "zjxss", 19)
