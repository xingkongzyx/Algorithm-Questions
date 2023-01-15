
""" 
* 可以使用滑动窗口的原因：如果一个连续子串已经「包含了 t 中的所有字符」, 那么左端点固定长度更长的子串一定也满足「包含了 t 中的所有字符」的要求. 但背离了找「最短覆盖子串」的要求. 所以此时选择收缩窗口, 开始考虑固定「右指针」, 向右移动「左指针」的情况了。这是在优化可行解，并让窗口长度挑战最小纪录。符合滑动窗口性质：向右边扩散得到和越来越大, 向左边界扩散得到和越来越小。
! 扩张窗口是为了纳入目标字符, 「右指针」右移, 先找到可行解 —— 当前窗口纳入了所有目标字符. 当窗口包含了所有目标字符, 此时再纳入字符, 条件依然满足, 但徒增子串长度. 此时应该优化可行解：收窄窗口, 「左指针」右移. 

> 窗口扩张或收缩取决于 —— 当前窗口是否找齐所有目标字符. 

? 对应的代码讲解 https://leetcode.cn/problems/minimum-window-substring/solution/hua-dong-chuang-kou-ji-bai-liao-100de-javayong-hu-/

? 一步步解释滑动窗口  https://leetcode.cn/problems/minimum-window-substring/solution/yi-bu-bu-xing-cheng-hua-dong-chuang-kou-si-lu-shen/
"""
class Solution(object):
    def minWindow(self, s, t):
        #* 统计滑动窗口中 s 的每个字符的出现次数(为了节省内存, 只记录窗口内能够构成目标字符串 t 的字符的出现频次)
        s_map = {}
        
        #* 用来统计 t 中每个字符出现次数
        t_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
            
        #* distance 表示滑动窗口内部已经包含的 t 中字符的个数, 窗口内单个字符的个数「等于」t 中对应字符个数的时候 distance 不再增加
        distance = 0
        left = 0
        right = 0
        beginIdx = 0
        minLen = len(s) + 1
        while right < len(s):
            rightChar = s[right]          
            #* 如果该字符 rightChar 不被目标字符串 t 需要, 也就是 rightChar 不在 t_map 中, 不做额外的判断
            if rightChar in t_map:
                #* 如果 rightChar 目前在滑动窗口中的出现次数「小于」rightChar 在 t_map 中的需要的次数, 说明这个字符被目标字符串 t 需要, 更新 distance. 如果已经「大于等于」, 则说明这个字符即使也被包含在 t 中, 但是此时的滑动窗口 s[left, right] 已包含足够多的 t 所需要 rightChar 的数量, 这个字符是多余的, 『对于构成 目标字符串 t 没有额外的贡献』, 所以 distance 不增加
                if s_map.get(rightChar, 0) < t_map[rightChar]:
                    distance += 1
                    
                #* 更新对应字符在 s_map 中的出现频次
                s_map[rightChar] = s_map.get(rightChar, 0) + 1
                
            #! 当且仅当滑动窗口 s[left, right] 已经满足了题目要求的「涵盖 t 所有字符」的要求. 此时那些字符在 s_map 中的出现频次一定是「大于或等于」他们在 t 中的出现频次的. 这个时候「缩小窗口」, 寻找『最小覆盖字串』 
            while distance == len(t):
                #* 当窗口的长度比已有的 minLen 小时, 更新 minLen , 并记录起始位置
                if right - left + 1 < minLen:
                    beginIdx = left
                    minLen = right - left + 1
                
                leftChar = s[left]
                
                #* 如果「左指针」代表的即将要移出窗口的字符 leftChar 不被 t 所需要, 说明它根本没有被记录在 s_map 中, distance 的值也不会因为它而减少, 不需要多余判断. 
                if leftChar in t_map:
                    #* 如果「左指针」代表的即将要移出窗口的字符 leftChar 被目标字符串 t 需要, 且出现的频次正好「等于」t 中的指定频次, 那么如果去掉了这个字符, 窗口就不再满足「涵盖 t 所有字符」的要求, 此时要让 distance 减一
                    if t_map[leftChar] == s_map[leftChar]:
                        distance -= 1
                    
                    #* 更新对应字符在 s_map 中的出现频次
                    s_map[leftChar] -= 1
                left += 1
            right += 1
        
        if minLen == len(s) + 1:
            return ""
        
        return s[beginIdx: beginIdx + minLen]
    
# aaabc abc {a:1, b:1, c:1}