
#! 已知目标顶点（终点）的情况下，可以分别从起点和目标顶点（终点）执行广度优先遍历，直到遍历的部分有交集，这是双向广度优先遍历的思想。

""" 
更合理的做法是，每次从单词数量小的集合开始扩散；
这里 beginQueue 和 endQueue 交替使用，等价于单向 BFS 里使用队列，每次扩散都要加到总的 visited 里。

链接：https://leetcode.cn/problems/word-ladder/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you-2/
"""
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

        visited = set()
        wordSet = set(wordList)

        #* 如果wordList包含了 beginWord, 则进行去除。没有的话这个方法也不会报错
        wordSet.discard(beginWord)

        beginQueue = deque([beginWord])
        endQueue = deque([endWord])
        visited.add(beginWord)
        visited.add(endWord)
        count = 0
        while len(beginQueue) > 0 and len(endQueue) > 0:
            # print(beginQueue, endQueue)
            #* 优先选择小的queue进行扩散，考虑到的情况更少
            if len(beginQueue) > len(endQueue):
                beginQueue, endQueue = endQueue, beginQueue
            # print("after exchange", beginQueue, endQueue)
            # print("\n")
            count += 1

            #* 逻辑到这里，保证 beginQueue 是相对较小的集合
            numOfWordInCurrentLevel = len(beginQueue)

            ## 为了确保每次遍历都能考虑到上一层单词的所有转换形式，我们需要先记录 beginQueue 的初始长度，然后pop 这么多的words，因为这些words就是上一层某个单词进行替换字符得到的所有可能
            for _ in range(numOfWordInCurrentLevel):
                currentWord = beginQueue.popleft()

                #* 尝试对 currentWord 修改每一个字符，看看是不是能落在 endQueue 中，扩展得到的新的 replacedWord 添加到 beginQueue 里.
                for charIdx in range(len(currentWord)):
                    for num in range(26):
                        char = chr(ord('a') + num)
                        replacedWord = currentWord[:charIdx] + char + currentWord[charIdx + 1:]

                        #* 如果 replacedWord 在 wordSet 中说明，这个word才满足currentWord的替换要求
                        if replacedWord in wordSet:
                            #! 此时遍历的部分有交集(beginQueue中的元素的变体也出现在endQueue中，说明此时从 题目的参数的 beginWord -> endWord 变化成功)。但是因为这个 replacedWord 是在下一轮while loop 才会被处理，所以返回的是count + 1
                            if replacedWord in endQueue:
                                return count + 1

                            #* 把 currentWord 的变体放到 beginQueue 中，然后在下一轮中进行处理
                            if replacedWord not in visited:
                                visited.add(replacedWord)
                                beginQueue.append(replacedWord)
        return 0


s = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

res = s.ladderLength(beginWord, endWord, wordList)
print(res)