
# > 求最大窗口, 所以在窗口非法时「收缩窗口」(也就是移动左指针), 并且在「收缩窗口」的判断句外面记录最大窗口。这道题「窗口非法」就是指窗口内 "T" 与 "F"的数量均大于 k 的时候
class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        record = {}
        maxLen = 0

        left = 0
        right = 0
        while right < len(answerKey):
            rightChar = answerKey[right]
            record[rightChar] = record.get(rightChar, 0) + 1

            #! 与 1004 的不同之处, 只有当 "T" 与 "F"的数量均大于 k 的时候, 才无法通过修改其中一个字母来使窗口内所有字母相同, 需要移动左指针
            while record.get("T", 0) > k and record.get("F", 0) > k:
                leftChar = answerKey[left]
                record[leftChar] -= 1
                left += 1
            #! 与 1004 的不同之处, 当 "T" 与 "F" 其中一个的数量小于 k 的时候, 我们可以将那个字母全部改为另一个, 从而使窗口中的所有字母相同,
            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen
