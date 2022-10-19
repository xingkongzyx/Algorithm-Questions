""" 「」
> 双向 BFS 适用于 <起点> 和 <终点> 都知道的的情况下使用。
! 已知目标终点的情况下, 可以分别从起点和目标终点执行BFS, 直到遍历的部分「有交集」。这种方式搜索的单词数量会更小一些

* 双向 BFS 代码, 代码其实不复杂。相对于之前单向 BFS, 有如下改进
* 
* 使用两个 queue, 分别从 start 和 end 两头开始 BFS
* 每次选择较小的 queue 开始 BFS, 也就是将小的作为 startQueue, 大的作为 endQueue
* 如果 endQueue 中能找到 startQueue, 就结束
* 否则, 在访问 queue 中加入访问记录, 并加入到 tmp 中, 作为子节点。
? https://leetcode.cn/problems/word-ladder/solution/cpp-yi-ge-si-lu-de-zhuan-bian-cong-1156msjia-su-da/


? python 版本的代码: https://leetcode.cn/problems/word-ladder/solution/python3-bfshe-shuang-xiang-bfsshi-xian-dan-ci-jie-/
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

        # * 处理edge case
        if not wordList or endWord not in wordList:
            return 0

        wordSet = set(wordList)

        # * 将 endWord 从 wordSet 中去除, 代表它已经被访问过
        wordSet.discard(endWord)

        beginQueue = deque([beginWord])
        endQueue = deque([endWord])

        count = 0
        while len(beginQueue) > 0 and len(endQueue) > 0:

            # * 优先选择从「包含元素数量较少」的 queue 进行扩散，这里就是确保每次进行扩散的 beginQueue 一定是「包含元素数量较少」的 queue
            if len(beginQueue) > len(endQueue):
                beginQueue, endQueue = endQueue, beginQueue

            count += 1

            # * 逻辑到这里, 保证 beginQueue 是「包含元素数量较少」的 queue
            numOfWordInCurrentLevel = len(beginQueue)

            for _ in range(numOfWordInCurrentLevel):
                currentWord = beginQueue.popleft()
                """ 
                * 如果按照单向BFS的写法, 应该在这里进行判断, 但实际上这里两个队列永远不会出现「交集」。
                / 简单的例子: beginWord="hot" endWord="lot" wordList=["lot"].
                * 在第一次也是唯一一次的BFS遍历中, 从 beginQueue 开始, wordSet 以经是空(因为前面已经把 endWord 从 wordSet 中移除了), 所以对 currentWord("hot") 无论进行怎样的变化，都无法满足下面的 "if replacedWord in wordSet:" 的判断, 最终导致这一次循环后两个队列都为空, 循环终止. 并且在这次循环中 currentWord("hot") 不在 endQueue(["lot"]) 中
                if currentWord in endQueue:
                            return count + 1
                """
                # * 对 currentWord 的每一个字符进行替换, 检查替换的结果是否已经在 endQueue 中
                for charIdx in range(len(currentWord)):
                    for num in range(26):
                        char = chr(ord('a') + num)
                        replacedWord = currentWord[:charIdx] + \
                            char + currentWord[charIdx + 1:]

                        # > 如果在这里进行判断结果就不一样了, 此时 currentWord("hot") 经过变换得到 replacedWord("lot") 是在 endQueue 中, 能够被成功捕捉到, 代表出现「交集」, 从 beginWord -> endWord 转化成功, 返回转化所需的步骤 steps.
                        if replacedWord in endQueue:
                            return count + 1

                        # * 如果 replacedWord 没通过上面的检查, 但是它出现在 wordSet 中, 说明当前替换方法「满足要求」并且当前替换还「没有被访问」过
                        if replacedWord in wordSet:
                            # * 把 replacedWord 放到 beginQueue 中, 在下一轮中进行处理。并将其从 wordSet 移除, 代表「已被访问」
                            wordSet.remove(replacedWord)
                            beginQueue.append(replacedWord)
        return 0


s = Solution()

beginWord = "hot"
endWord = "lot"
wordList = ["lot"]

res = s.ladderLength(beginWord, endWord, wordList)
print(res)
