
#* 可以使用滑动窗口的原因：如果一个连续子串已经包含了「大于两个」的不同字符，那么左端点固定, 且长度更长的子串一定也包含「大于两个」的不同字符, 此时的虽然「长度更长」, 但是背离了「至多包含两个不同字符」的要求。 所以此时选择收缩窗口, 开始考虑固定「右指针」, 向右移动「左指针」的情况了。这是在找到满足「至多包含两个不同字符」的可行解，找到后记录最大的可行子串的长度。符合滑动窗口性质：向右边扩散得到和越来越大, 向左边界扩散得到和越来越小。
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
            ## Step 3 更新需要维护的变量 (max_len, hashmap), 把当前元素在哈希表中的计数加一. 
            rightChar = s[right]
            record[rightChar] = record.get(rightChar, 0) + 1
            
            ## Step 4
            ## 题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题, 窗口合法的条件就是窗口中只存在小于三个的不同字符(也就是一个或者两个不同字符)
            ## 如果当前窗口不合法时, 就是有三个不同的字符, 用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            while len(record) > 2:
                leftChar = s[left]
                record[leftChar] -= 1
                if record[leftChar] == 0:
                    del record[leftChar]
                left += 1
            
            ## 此时缩小窗口后，窗口内的元素满足 contains at most 2 distinct characters 的要求，更新 maxLen
            maxLen = max(maxLen, right - left + 1)
            right += 1
        
        return maxLen
                    
res = Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb")
print(res)
