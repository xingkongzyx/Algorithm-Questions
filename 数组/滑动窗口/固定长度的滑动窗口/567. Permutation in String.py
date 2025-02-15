
#? 这道题 与 438 相似度百分之99 
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        ## Step 1: 
        ## 定义需要维护的变量
        ## 本文需要判断 s2 是否包含 s1 的排列，也就相当于判断 s2 是否包含 s1 的 anagram. 所以用两个哈希表分别存储 s1 和 s2 中出现的字符频率。 s1_record 一旦建立起到的是参考作用，不会再改变！
        s1_record = {}
        s2_record = {}
        s1_len = len(s1)
        for char in s1:
            s1_record[char] = s1_record.get(char, 0) + 1
        
        ## Step 2: 定义窗口的首尾端 (left, right)， 然后滑动窗口
        left = 0
        right = 0
        
        while right < len(s2):
            ## Step 3: 更新需要维护的变量 (s2_record), 如果 s2_record == s1_record, 代表 "s2 contains a permutation of s1", 直接返回 True
            rightChar = s2[right]
            s2_record[rightChar] = s2_record.get(rightChar, 0) + 1
            
            if s1_record == s2_record:
                return True
            
            ## Step 4 
            ## 根据题意可知窗口长度固定，所以用if
            #! 滑动窗口在每次循环结束后[left, right) 代表的的都是 s2 中与 s1 的长度仅相差一个长度的子串, 然后再进入循环后, 加上 rightChar, 滑动窗口的长度便  == s1_len
            ## 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (s2_record)
            #! 本题中的 map 用字典来实现的时候，需要注意：如果移除 left 元素后，若 s2_record[leftChar] == 0 那么需要从字典中删除 s2[left] 这个key。因为 {"a":0, "b":1} 和 {"b":1} 是不等的。
            if (right - left + 1) == s1_len:
                leftChar = s2[left]
                s2_record[leftChar] -= 1
                if s2_record[leftChar] == 0:
                    del s2_record[leftChar]
                left += 1
            right += 1
            
        return False

res = Solution().checkInclusion(s1 = "ab", s2 = "eidbeaooo")
print(res)
