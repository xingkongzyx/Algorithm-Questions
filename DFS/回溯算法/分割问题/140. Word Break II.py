""" 
* 将 "catsanddog" 按照 wordDict 拆分出单词。这个问题可以分解一下：
* 
* "c" 是不是 wordDict 中的单词，不是。
* "ca" 是不是 wordDict 中的单词，不是。
* "cat" 是不是 wordDict 中的单词，是，对剩余子串 "sanddog" 递归拆分。
* "cats" 是不是 wordDict 中的单词，是，对剩余子串 "anddog" 递归拆分。
* ……以此类推。用DFS回溯，考察所有的拆分可能

? https://leetcode.cn/problems/word-break-ii/solution/shou-hua-tu-jie-dan-ci-chai-fen-ii-cong-di-gui-dao/


? 递归树比较清晰: https://leetcode.cn/problems/word-break-ii/solution/shu-ju-jie-gou-he-suan-fa-hui-su-suan-fa-098z/

"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        cur = []
        total = []

        def backtracking(startIdx):
            if startIdx == len(s):
                total.append(" ".join(cur))
                return

            for i in range(startIdx, len(s)):
                # *  切出一个子串，看看是不是单词
                word = s[startIdx: i + 1]
                # * 如果是 wordDict 中的单词，对剩余子串继续划分
                if word in wordDict:
                    cur.append(word)
                    backtracking(i + 1)
                    # * 回溯
                    cur.pop()

        backtracking(0)
        return total


Solution().wordBreak(s="catsanddog", wordDict=[
    "cat", "cats", "and", "sand", "dog"])
