
#* 可以使用滑动窗口的原因：如果一个子串包含重复字符，那么与它有相同左端点的、长度更长的字符串一定也包含重复字符；又由于题目只要求我们找最长不重复子串的长度，如果已经找到了一个长度为 n 的子串，那么小于等于长度 n 的子串就没有必要再枚举了. 符合滑动窗口性质：向右边扩散得到和越来越大，向左边界扩散得到和越来越小。
#> 求最大窗口，所以在窗口非法时「收缩窗口」(也就是移动左指针)，并且在「收缩窗口」的判断句外面记录最大窗口。这道题「窗口非法」就是指窗口存在重复字符，此时需要移动左窗口
#? https://leetcode.cn/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
#? https://leetcode.cn/problems/longest-substring-without-repeating-characters/solution/zen-yao-yong-hua-dong-chuang-kou-wei-he-35418/

#! 保证这两个指针对应的子串中没有重复的字符. 每次循环结束后 [left, right) 之间的字符串没有重复字符
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ## Step 1: 定义需要维护的变量, 本题求最大长度，所以需要定义max_len, 该题又涉及去重，因此还需要一个哈希表
        maxLen = 0
        record = {}
        
        ## Step 2: 定义窗口的首尾端 (left, right)， 然后滑动窗口
        left = 0
        right = 0
        
        while right < len(s):
            ## Step 3
            ## 更新需要维护的变量 (hashmap)
            ## i.e. 把窗口末端元素加入哈希表，使其频率加1
            rightChar = s[right]
            record[rightChar] = record.get(rightChar, 0) + 1
            
            
            ## Step 4: 
            ## 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            ## 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            ## 当窗口长度大于哈希表长度时候 (说明存在重复元素)，窗口不合法
            ## 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (record)

            while record[rightChar] > 1:
                leftChar = s[left]
                record[leftChar] -= 1
                if record[leftChar] == 0:
                    del record[leftChar]
                    
                left += 1
                
            #* 经历过上面的缩小窗口后(也可能本来就符合要求不需要缩小)，此时的 [left, right] 窗口是合法的
            maxLen = max(maxLen, right - left + 1)
            
            right += 1
        
        return maxLen

res = Solution().lengthOfLongestSubstring("abcabcbb")
print(res)
