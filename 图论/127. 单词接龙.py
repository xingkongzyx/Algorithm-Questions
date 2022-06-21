# https://leetcode.cn/problems/word-ladder/solution/shou-hua-tu-jie-127-dan-ci-jie-long-bfsde-dian-x-2/
# ? 求起点和终点的最短路径长度，对于无向图求最短路径，广搜(BFS)最为合适，广搜只要搜到了终点，那么一定是最短的路径。因为广搜就是以起点中心向四周扩散的搜索。
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import deque

        #* 处理edge case
        if not wordList or endWord not in wordList:
            return 0

        #> 不变为set的话运行时间会无导致法通过测试
        wordSet = set(wordList)

        queue = deque([beginWord])
        count = 0
        while len(queue) > 0:
            count += 1
            #! 这里相当于层序遍历，上一层单词的替换词可能有多个，在这一层中我们要对上一层可能出现的替换词中的每个单词进行检查。所以说在某次遍历中从queue中会popleft 出多个单词。
            #! 如果没有这个变量，我们把一个单词的多个替换词当成了多次替换，而其实这些变换词都属于一次替换得到的结果
            numOfWordInCurrentLevel = len(queue)
            for _ in range(numOfWordInCurrentLevel):
                currentWord = queue.popleft()
                if currentWord == endWord:
                    return count
                for charIdx in range(len(currentWord)):
                    for i in range(26):
                        char = chr(ord('a') + i)
                        replacedWord = currentWord[:charIdx] + char + currentWord[charIdx+1:]

                        if replacedWord in wordSet:
                            queue.append(replacedWord)
                            wordSet.remove(replacedWord)
        return 0
s = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

res = s.ladderLength(beginWord, endWord, wordList)
print(res)