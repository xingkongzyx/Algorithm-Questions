""" 
? 为什么使用 BFS: https://leetcode.cn/problems/word-ladder/solution/127-dan-ci-jie-long-wei-shi-yao-yao-yong-yan-sou-x/
* 本题可以看成是「无向图」。对于「无向图」求起点和终点的『最短路径』长度, BFS 最为合适, 广搜只要搜到了终点, 那么一定是最短的路径。因为广搜就是以起点中心向四周扩散的搜索。
! 本题有一个注意点：本题是一个「无向图」, 需要用标记位, 标记着节点是否走过, 否则就会死循环！代码中采取的标记的写法是将访问过的单词从 wordSet 中移除
? 无向图图片来自: https://leetcode.cn/problems/word-ladder/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you-2/
? https://leetcode.cn/problems/word-ladder/solution/shou-hua-tu-jie-127-dan-ci-jie-long-bfsde-dian-x-2/
"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        from collections import deque

        # * 处理edge case
        if not wordList or endWord not in wordList:
            return 0

        # / 不变为set的话运行时间会无导致法通过测试
        wordSet = set(wordList)

        queue = deque([beginWord])
        count = 0
        while len(queue) > 0:
            count += 1
            #! 这里相当于层序遍历, 上一层单词的替换词可能有多个, 在这一层中我们要对上一层可能出现的替换词中的每个单词进行检查。所以说在某次遍历中从queue中会 popleft 出多个单词。
            #! 如果没有这个变量, 我们把一个单词的多个替换词当成了多次替换, 而其实这些变换词都属于一次替换得到的结果
            numOfWordInCurrentLevel = len(queue)
            for _ in range(numOfWordInCurrentLevel):
                currentWord = queue.popleft()
                if currentWord == endWord:
                    return count
                # * 对 currentWord 的每个字母都进行替换, 替换的范围是 "a-z" 这26个字母, 每次替换后检查替换的结果是否在 wordSet 中, 在的话就意味 replacedWord 是「未访问」状态, 将其加入队列
                for charIdx in range(len(currentWord)):
                    for i in range(26):
                        char = chr(ord('a') + i)
                        replacedWord = currentWord[:charIdx] + \
                            char + currentWord[charIdx+1:]

                        if replacedWord in wordSet:
                            queue.append(replacedWord)
                            wordSet.remove(replacedWord)
        return 0


s = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

res = s.ladderLength(beginWord, endWord, wordList)
print(res)
