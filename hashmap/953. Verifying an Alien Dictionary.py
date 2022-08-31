""" 「」
* 对所有的 words 遍历, 判断相邻 word 间是否符合「外星语」的字典序。
! 只有每对相邻单词都是有序的, 那么整个 words 才是有序的
! 原因: 「有序性」是可以传递的, 例如, word1 <= word2 和 word2 <= word3 可以推出 word1 <= word3
* 相邻单词的判断方法: 
* 1. 同时遍历相邻单词, 找到出现的「第一个」不同的字母, 如果「前一个单词」的字母 order 小于「后一个单词」的字母 order, 说明这一对相邻单词符合「外星语」的字典序, 不再比较「这一对」相邻单词其余的字母, 而是比较「下一对」; 如果大于, 直接返回 False
* 2. 如果比较到相邻单词中「较短的单词」结束仍没出现不同字母, 这时要进行长度比较。如果「前一个单词」的长度比「后一个单词」的长度长, 直接返回false

? 代码借鉴: https://leetcode.cn/problems/verifying-an-alien-dictionary/solution/by-fuxuemingzhu-d81b/
? 有序性传递: https://leetcode.cn/problems/verifying-an-alien-dictionary/solution/by-nehzil-99e7/
/ 时间复杂度: O(n*m)。n为单词的个数, m 为较长单词的字母数。
/ 空间复杂度: O(1)。只有26个小写字母, 哈希表大小为常数。
"""


class Solution:
    def isAlienSorted(self, words, order) -> bool:
        charsMap = {}
        for i in range(len(order)):
            charsMap[order[i]] = i

        for i in range(len(words) - 1):
            curWord = words[i]
            nextWord = words[i + 1]
            minLen = min(len(curWord), len(nextWord))
            # * flag 代表相邻单词间每个字符是否都是相同的
            flag = True
            for j in range(minLen):
                if charsMap[curWord[j]] < charsMap[nextWord[j]]:
                    flag = False
                    break
                elif charsMap[curWord[j]] > charsMap[nextWord[j]]:
                    return False
            # * 只有相邻单词间长度不同，且较小长度的单词的所有字符与较长的单词对应的字符完全相同时，才进行前后单词长度的判断
            if flag == True and len(curWord) > len(nextWord):
                return False
        return True
