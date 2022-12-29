""" 
? https://leetcode.cn/problems/longest-repeating-character-replacement/solution/xiao-ying-wu-424-python-hua-dong-chuang-lumqd/
内部使用while的原因: Consider an example:- AAEBAE with k=2, when end is at the last position, start gets incremented from 0 to 2 by 2 steps and not only one step to get a new valid window.

/ Time Complexity: O(26 |s|) = O(|s|)
/ Space Complexity: O(26) = O(1)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        map = {}
        maxLen = 0

        while right < len(s):
            rightChar = s[right]
            map[rightChar] = map.get(rightChar, 0) + 1
            # # 需要替换的字符数目 + 数量最多的字符数目 = 窗口字符数目, 如果需要替换的字符数目超过给定的 k, 则移动左边界
            while right - left + 1 > max(map.values()) + k:
                leftChar = s[left]
                map[leftChar] = map.get(leftChar, 0) - 1
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen
