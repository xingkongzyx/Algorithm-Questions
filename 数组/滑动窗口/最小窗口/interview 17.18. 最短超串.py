
#? 对应的代码讲解 https://leetcode.cn/problems/minimum-window-substring/solution/hua-dong-chuang-kou-ji-bai-liao-100de-javayong-hu-/
class Solution(object):
    def shortestSeq(self, big, small):
        minLen = len(big) + 1
        startIdx = 0
        small_map = {}
        for num in small:
            small_map[num] = small_map.get(num, 0) + 1
        
        big_map = {}
            
        left = 0
        right = 0
        distance = 0
        while right < len(big):
            rightNum = big[right]
            if rightNum in small_map:
                if big_map.get(rightNum, 0) < small_map[rightNum]:
                    distance += 1
                big_map[rightNum] = big_map.get(rightNum, 0) + 1
                
            while distance == len(small):
                currentLen = right - left + 1
                if currentLen < minLen:
                    minLen = currentLen
                    startIdx = left
                
                leftNum = big[left]
                if leftNum in small_map:
                    if big_map[leftNum] == small_map[leftNum]:
                        distance -= 1
                    big_map[leftNum] -= 1
                left += 1
            right += 1
            
        if minLen == len(big) + 1:
            return []
        
        return [startIdx, startIdx + minLen - 1]

print(Solution().shortestSeq(big = [1,23],
small = [4]))
