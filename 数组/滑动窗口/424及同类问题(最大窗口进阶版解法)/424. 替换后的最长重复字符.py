"""
> 这道题 不用保证窗口内的字符串是合法的 
? 关于 maxFrequency: https://leetcode.cn/problems/longest-repeating-character-replacement/solution/tong-guo-ci-ti-liao-jie-yi-xia-shi-yao-shi-hua-don/956007

* 核心要点: 
* 1. map记录的是「窗口里的」字符出现的次数, 是「窗口里的」!「窗口里的」! 所以左窗口右移后, 记得将移出去的元素个数 -1
* 2. 我们的目的就是让窗口尽可能扩张, 有K个字符的容错机会, 容错机会肯定要用给map中「出现次数最多的字符」以外的字符才有机会让窗口扩张, 也就是让 k 个「出现次数最多的字符以外的字符」变成 「出现次数最多的那个字符」
! 3. 就算某一刻你发现窗口里元素都不一样, 但不要怀疑, ⭐因为它曾经辉煌过⭐,它会一直呈现它窗口最大时候的状态
* 现在我是这样: aaab【cdef】, 是因为曾经我: 【aaab】cdef (容错次数 K=1)

# maxFrequency 并不是当前窗口内出现次数最多字母的次数, 而是历史窗口中出现次数最多字母的次数。为什么在窗口平移的时候不用更新？因为曾经有一个窗口满足过条件。滑动窗口的长度只有在 maxFrequency 变大的时候才增加, 由于不需要对滑动窗口减小, 因此没有对 maxFrequency 进行减小操作, 如果减小了反而可能出现错误。感觉这题的核心思路就是通过滑动窗口的方式寻找窗口内相同字符出现最多的次数, 并且使用的是历史最长保证窗口长度不会减小。

# 因为我们要找的是「最长」那一个符合条件的子串, 而子串长度是由 maxFrequency + k 来决定的, 所以我们只在其有机会变得更大时将其更新。什么时候变得更大呢？ 只有当其超出「历史最大值」时。在这里我们不关心当前窗口的各个字符重复次数最大值, 只关心这个最大值有没有超出历史最大值。
? https://leetcode.cn/problems/longest-repeating-character-replacement/solution/tan-xin-de-hua-dong-chuang-kou-si-lu-qing-xi-dai-m/
"""


class Solution(object):
    def characterReplacement(self, s, k):
        map = [0] * 26
        maxLen = 0
        #! 滑动窗口历史上在一个窗口内出现次数最多的字母的次数（仅限在当时的窗口内出现）
        maxFrequency = 0
        left = 0
        right = 0
        while right < len(s):
            # * 右边界先移动找到一个满足题意的可以替换 k 个字符以后, 所有字符都变成一样的当前看来最长的子串, 直到右边界纳入一个字符以后, 不能满足的时候停下；
            rightChar = s[right]
            rightCharIdx = ord(rightChar) - ord('A')
            map[rightCharIdx] += 1
            # print("move right边界")
            if map[rightCharIdx] > maxFrequency:
                maxFrequency = map[rightCharIdx]

            if right - left + 1 <= maxFrequency + k:
                maxLen = max(maxLen, right - left + 1)
            # print(
            #     f'left is {left}, right is {right}, {s[left: right + 1]}, maxFrequency is {maxFrequency}')
            """ 
            * 说明此时 k 不够用, 把其它不是最多出现的字符替换以后, 都不能填满这个滑动的窗口, 这个时候须要考虑左边界向右移动
            * 移出滑动窗口的时候, 频数数组须要相应地做减法
            ! 这里做的是窗口的平移操作, 而不是缩小窗口
            """
            if maxFrequency + k < right - left + 1:
                # print("****move 左边界*****")
                leftChar = s[left]
                leftCharIdx = ord(leftChar) - ord('A')
                map[leftCharIdx] -= 1
                left += 1
            # print(f'left is {left}, right is {right}, {s}, \n')
            right += 1

        return maxLen


s = Solution().characterReplacement(s="AABCABBB", k=2)
print(s)
