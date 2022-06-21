class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ## Step 1: 
        ## 定义需要维护的变量
        ## 本文需要对比两组字符串是否为异位词，所以用两个哈希表分别存储 p 和 s 中出现的字符频率 (abc和bac是异位词是因为他们对应的哈希表相等)。p_record 一旦建立起到的是参考作用，不会再改变！
        ## 同时我们需要找到所有合法解，所以还需要一个res数组
        s_record = {}
        p_record = {}
        p_len = len(p)
        result = []
        for char in p:
            p_record[char] = p_record.get(char, 0) + 1
        
        ## Step 2: 定义窗口的首尾端 (left, right)， 然后滑动窗口
        left = 0
        right = 0
        
        while right < len(s):
            ## Step 3: 更新需要维护的变量 (s_record), 如果 s_record == p_record, 代表找到了一个解, 加入到result
            rightChar = s[right]
            s_record[rightChar] = s_record.get(rightChar, 0) + 1
            
            if s_record == p_record:
                result.append(left)
            
            ## Step 4 
            ## 根据题意可知窗口长度固定，所以用if
            #! 滑动窗口在每次循环结束后[left, right) 代表的的都是 s 中与 p 的长度仅相差一个长度的子串，然后再进入循环后, 加上 rightChar, 滑动窗口的长度便 == p_len
            ## 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (s_record)
            if (right - left + 1) == p_len:
                leftChar = s[left]
                s_record[leftChar] -= 1
                if s_record[leftChar] == 0:
                    del s_record[leftChar]
                left += 1
                
            right += 1
            
        return result

res = Solution().findAnagrams(s = "abab", p = "ab")
print(res)
