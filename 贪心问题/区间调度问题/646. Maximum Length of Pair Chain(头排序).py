from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()  # Sort in increasing order by starting point

        ans = 1
        lastEnd = pairs[0][1]
        for start, end in pairs:
            if start > lastEnd:
                ans += 1
                lastEnd = end
            else:
                lastEnd = min(lastEnd, end)
        return ans
