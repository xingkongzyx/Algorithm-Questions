""" 
? https://leetcode.com/problems/word-search-ii/solutions/712733/python-trie-solution-with-dfs-explained/?orderBy=most_votes
? https://leetcode.cn/problems/word-search-ii/solution/dan-ci-sou-suo-ii-by-leetcode-solution-7494/ 
"""
# from typing import List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endWord = None

    def add(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.endWord = word


class Solution:
    def findWords(self, board, words):
        self.numWords = len(words)
        wordTrie = TrieNode()
        for word in words:
            wordTrie.add(word)
        numRows = len(board)
        numCols = len(board[0])
        dir_x = [0, 0, 1, -1]
        dir_y = [-1, 1, 0, 0]

        def inArea(row, col):
            return 0 <= row < numRows and 0 <= col < numCols

        def DFS(row, col, curNode):
            if self.numWords == 0:
                return
            if curNode.endWord != None:
                result.append(curNode.endWord)
                curNode.endWord = None
                self.numWords -= 1

            # 递归终止条件: 越界，或者访问过，或者不在字典树中，直接返回
            if not inArea(row, col) or board[row][col] not in curNode.children or board[row][col] == '#':
                return

            curChar = board[row][col]
            board[row][col] = '#'

            for i in range(4):
                newRow = row + dir_x[i]
                newCol = col + dir_y[i]
                DFS(newRow, newCol, curNode.children[curChar])

            board[row][col] = curChar

        result = []
        for i in range(numRows):
            for j in range(numCols):
                DFS(i, j, wordTrie)

        return result
