 
#! 每次循环结束后, 保证 s[left, right) 区间内的字符串不会包含多于 k 种的不同字符

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        ## Step 1: 
        ## 定义需要维护的变量, 本题求最大长度, 所以需要定义 maxLen,
        ## 该题又涉及计算不同的元素个数, 因此还需要一个哈希表
        maxLen = 0
        record = {}

        ## Step 2: 定义窗口的首尾端 (left, right), 然后滑动窗口
        left = 0
        right = 0

        while right < len(s):
            ## Step 3 更新需要维护的变量 (max_len, hashmap), 把当前元素在哈希表中的计数加一. 
            rightChar = s[right]
            record[rightChar] = record.get(rightChar, 0) + 1

            ## Step 4
            ## 题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题, 窗口合法的条件就是窗口中只contains at most k distinct characters.
            ## 如果当前窗口不合法时, 就是有 k + 1 个不同的字符, 用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            while len(record) > k:
                leftChar = s[left]
                record[leftChar] -= 1
                if record[leftChar] == 0:
                    del record[leftChar]
                left += 1
            
            ## 此时缩小窗口后，窗口内的元素满足 contains at most k distinct characters 的要求，更新 maxLen
            maxLen = max((right - left + 1), maxLen)
            right += 1
        
        return maxLen
