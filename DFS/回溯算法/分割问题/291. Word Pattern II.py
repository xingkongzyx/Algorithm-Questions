""" 
? 两个 hash https://leetcode.cn/problems/word-pattern-ii/solution/c-hui-su-zhu-shi-zai-dai-ma-zhong-by-xing-chen-da-/
? 细讲: https://leetcode.cn/problems/word-pattern-ii/solution/hui-su-hashmapbao-cun-pi-pei-hashsetbao-645u7/
? 回溯树 https://leetcode.cn/problems/word-pattern-ii/solution/by-yvhuiwang-d1fy/
/ 时间复杂度 O(状态总数 * 计算每个状态的时间) = O(MN * N) = O(M * N^2)
"""


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        pattern_to_word = dict()
        word_to_pattern = dict()
        count = 1

        def backtracking(patternIdx, strIdx, count):
            print("-------------------------------------------\n")
            print(
                f"{'  ' * count} In backtracking: {patternIdx} is patternIdx, {strIdx} is strIdx")
            # * 终止条件: patternIdx 遍历完成的同时, strIdx 也遍历完成, 说明成功 match. 否则说明 s 中有部分字符没有匹配到
            if patternIdx == len(pattern):
                if strIdx == len(s):
                    return True
                else:
                    return False

            curPattern = pattern[patternIdx]
            """
            * 匹配过程:  
            * pattern遍历到位置 patternIdx, 有两种情况：
            * 情况 1: 这个位置的模式 patter[patternIdx] 没有被匹配过(例如 pattern = "abab", patternIdx = 0, 第一次匹配 a)
            * 情况 2: 这个位置的模式 patter[patternIdx] 之前匹配过(例如 pattern = "abab", patternIdx = 2, 之前位置为 0 的 a 已经被匹配过)
            """

            if curPattern in pattern_to_word:

                # * 情况 1: 只要看看对应 s 中相同长度的「子串」跟之前匹配过的是否相等即可. 如果一样继续往后匹配，不一样就直接返回false
                mappedWord = pattern_to_word[curPattern]
                mappedWordLen = len(mappedWord)
                curWord = s[strIdx: strIdx + mappedWordLen]
                print(f"{'  ' * count} curPattern in p2w")
                print(f"{'  ' * count} curPattern is {curPattern}")
                print(f"{'  ' * count} p2w is {pattern_to_word}")
                print(
                    f"{'  ' * count} curWord is {curWord}, mappedWord is {mappedWord}, curWordIdx is {strIdx}, patterIdx is {patternIdx}")
                if curWord == mappedWord:
                    return backtracking(patternIdx + 1, strIdx + mappedWordLen, count + 1)
                else:
                    return False
            else:
                # * 情况 2: 从strIdx位置开始，尝试每一种可能的「子串」, 范围是 [strIdx, i], 然后对每一个「子串」以及 pattern 进行匹配。「」
                for i in range(strIdx, len(s)):
                    # * 当前的切割的「子串」是 s[strIdx, i]
                    curWord = s[strIdx: i + 1]

                    #! 到了这里说明, 当前的 pattern[patternIdx] 之前没有被匹配过, 但是现在切割的「子串」 curWord 已经存在于 word_to_pattern map, 说明当前的「子串」与 pattern 并不是一一对应的关系, 尝试增长「子串」进行匹配
                    if curWord in word_to_pattern:
                        print(f"{'  ' * count} !!!!can not match!!!!")
                        print(f"{'  ' * count} curPattern is {curPattern}")
                        print(f"{'  ' * count} curWord is {curWord}")
                        continue

                    pattern_to_word[curPattern] = curWord
                    word_to_pattern[curWord] = curPattern
                    print(f"{'  ' * count} curPattern not in p2w")
                    print(f"{'  ' * count} curPattern is {curPattern}")
                    print(f"{'  ' * count} curWord is {curWord}")
                    print(f"{'  ' * count} p2w is {pattern_to_word}")
                    print(f"{'  ' * count} w2p is {word_to_pattern}")
                    res = backtracking(patternIdx + 1, i + 1, count + 1)
                    if res:
                        return True
                    # * 如果不匹配，则回溯，尝试下一个 word
                    # if curPattern in pattern_to_word:
                    del pattern_to_word[curPattern]
                    # if curWord in word_to_pattern:
                    del word_to_pattern[curWord]

            return False

        return backtracking(0, 0, count)


print(print(Solution().wordPatternMatch("ab", "aa")))
