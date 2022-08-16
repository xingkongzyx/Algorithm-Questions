""" 
* 在本题中, 我们需要判断「pattern中的字符」与「s分割后的单词」之间是否恰好一一对应。即任意一个「字符」都对应着唯一的「单词」, 任意一个「单词」也只被唯一的一个「字符」对应。在集合论中, 这种关系被称为「双射」。

* 思路：创建两个 map   
* 第一步 key为pattern, value为words, 遍历pattern, 检查同一个patten是否对应相同的word
* 第二步 key为words, value为pattern, 遍历words, 检查同一个word是否对应相同的patter
* 为什么定义两个 map 呢?
* 为何定义两个呢？ 防止[aaaa]与[cat dog dog cat]、[abba]与[cat cat cat cat]时输出true
? https://leetcode.cn/problems/word-pattern/solution/dan-ci-gui-lu-by-leetcode-solution-6vqv/
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        pattern_to_word = dict()
        word_to_pattern = dict()

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            curPattern = pattern[i]
            curWord = words[i]

            if curPattern in pattern_to_word and curWord != pattern_to_word[curPattern]:
                return False

            if curWord in word_to_pattern and curPattern != word_to_pattern[curWord]:
                return False

            pattern_to_word[curPattern] = curWord
            word_to_pattern[curWord] = curPattern

        return True
