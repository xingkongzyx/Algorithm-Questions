
# * 可以使用滑动窗口的原因：如果一个子串已经「包含了 t 中的所有字符」，那么左端点固定长度更长的子串一定也满足「包含了 t 中的所有字符」的要求 ，但是题目要求找最短覆盖子串，此时左端点需要右移。符合滑动窗口性质：向右边扩散得到和越来越大，向左边界扩散得到和越来越小。
# https://leetcode.cn/problems/minimum-window-substring/solution/leetcode-76-zui-xiao-fu-gai-zi-chuan-cja-lmqz/
class Solution(object):
    def minWindow(self, s, t):
        s_map = {}
        t_map = {}
        #* distance 表示滑动窗口内部包含了 t 中字符的个数, 窗口内单个字符个数等于T中对应字符个数的时候 distance 不再增加
        distance = 0
        
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        left = 0
        right = 0
        beginIdx = 0
        minLen = len(s) + 1
        while right < len(s):
            rightChar = s[right]
            
            #* 如果该字符不被目标字符串 t 需要，也就是 rightChar 不在 t_map 中，不做额外的判断
            if rightChar in t_map:
                #* 更新对应字符在 s_map 中的出现频次
                s_map[rightChar] = s_map.get(rightChar, 0) + 1
                #* 如果更新后的值小于等于 rightChar 在 t_map 中的出现次数，说明这个字符被目标字符串 t 需要，更新 distance. 如果大于，则说明这个字符即使也被包含在 t 中，但是此时的 s[left, right] 已包含足够多的 t 所需要的这个字符 rightChar 的数量，这个字符是多余的
                if s_map[rightChar] <= t_map[rightChar]:
                    distance += 1
            
            
            #* 当且仅当已有字符串已经包含了所有目标字符串的字符，且出现频次一定大于或等于指定频次    
            while distance == len(t):
                #* 挡窗口的长度比已有的最短值小时，更改最小值，并记录起始位置
                if distance == len(t):
                    if right - left + 1 < minLen:
                        beginIdx = left
                        minLen = right - left + 1
                
                leftChar = s[left]
                #* 如果左边即将要去掉的字符不被目标字符串需要，那么不需要多余判断，也就是 leftChar 不在 t_map 中
                if leftChar in t_map:
                    #* 如果左边即将要去掉的字符被目标字符串 t 需要，且出现的频次正好等于指定频次，那么如果去掉了这个字符，
                    #* 就不满足覆盖子串的条件，此时要破坏循环条件跳出循环，即控制目标字符串指定字符的出现总频次 distance -= 1
                    if t_map[leftChar] == s_map[leftChar]:
                        distance -= 1
                    
                    #* //已有字符串中目标字符出现的次数-1
                    s_map[leftChar] -= 1
                left += 1
                # print("after: ", s[left:right+1])
                # print("\n")
            right += 1
        
        if minLen == len(s) + 1:
            return ""
        
        return s[beginIdx: beginIdx + minLen]
    

r = Solution().minWindow("ewcwaefgcf", "cae")
print(r)
