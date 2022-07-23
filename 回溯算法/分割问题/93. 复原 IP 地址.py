class Solution:
    def restoreIpAddresses(self, s: str):
        cur = []
        total = []
        
        def backtracking(s, startIdx):
            if len(cur) == 4:
                if startIdx == len(s):
                    total.append('.'.join(cur))
                return
            
            for i in range(startIdx, len(s)):
                strLen = i - startIdx + 1
                if strLen > 3:
                    break
                
                strSlice = s[startIdx: i + 1]
                if strLen != 1 and strSlice[0] == '0':
                    break
                strNum = int(strSlice)
                if strNum >= 0 and strNum <= 255:
                    cur.append(strSlice)
                    backtracking(s, i + 1)
                    cur.pop()
        
        backtracking(s, 0)
        # print(total)
        return total
