""" 
* 给定一个字符串 s, 找出 至多 包含两个不同字符的最长子串 t, 并返回该子串的长度。

* 示例 1:
* 输入: "eceba"
* 输出: 3
* 解释: t 是 "ece", 长度为3。

* 示例 2:
* 输入: "ccaabbb"
* 输出: 5
* 解释: t 是 "aabbb", 长度为5。
"""
#? 题目: https://cloud.tencent.com/developer/article/1659718 

#! 每次循环结束后, 保证 s[left, right) 区间内的字符串不会包含多于两种的不同字符

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ## Step 1: 
        ## 定义需要维护的变量, 本题求最大长度, 所以需要定义 maxLen,
        ## 该题又涉及计算不重复元素个数, 因此还需要一个哈希表
        record = {}
        maxLen = 0
        
        ## Step 2: 定义窗口的首尾端 (left, right), 然后滑动窗口
        left = 0
        right = 0
        
        while right < len(s):
            ## Step 3 更新需要维护的变量 (max_len, hashmap) 首先, 把当前元素的计数加一. 一旦哈希表长度小于等于2(之多包含2个不同元素), 尝试更新最大长度

            rightChar = s[right]
            record[rightChar] = record.get(rightChar, 0) + 1
            if len(record) <= 2:
                maxLen = max(maxLen, right - left + 1)
            ## 属于Step 4 中的情况2
            ## 题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题, 窗口合法的条件就是窗口中只存在小于三个的不同字符(也就是1个或者两个不同字符)
            ## 如果当前窗口不合法时, 就是有三个不同的字符, 用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            while len(record) > 2:
                leftChar = s[left]
                record[leftChar] -= 1
                if record[leftChar] == 0:
                    del record[leftChar]
                left += 1
            
            right += 1
        
        return maxLen
                    
res = Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb")
print(res)
