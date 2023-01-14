from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.word = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.isEnd = True
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.num_words = len(words)
        wordTrie = Trie()

        for word in words:
            wordTrie.insert(word)

        numRows = len(board)
        numCols = len(board[0])
        directions = [
            [-1, 0],
            [1, 0],
            [0, 1],
            [0, -1],
        ]
        visited = [[False for _ in range(numCols)] for _ in range(numRows)]
        result = []

        def inArea(row, col):
            return 0 <= row < numRows and 0 <= col < numCols

        def backtracking(rowIdx, colIdx, trieNode):
            if self.num_words == 0:
                return
            if not inArea(rowIdx, colIdx) or visited[rowIdx][colIdx] == True or board[rowIdx][colIdx] not in trieNode.children:
                return

            curChar = board[rowIdx][colIdx]
            visited[rowIdx][colIdx] = True
            trieNode = trieNode.children[curChar]

            if trieNode.isEnd:
                result.append(trieNode.word)
                trieNode.isEnd = False
                self.num_words -= 1

            for i in range(4):
                newRowIdx = rowIdx + directions[i][0]
                newColIdx = colIdx + directions[i][1]

                backtracking(newRowIdx, newColIdx, trieNode)

            visited[rowIdx][colIdx] = False

        for i in range(numRows):
            for j in range(numCols):
                backtracking(i, j, wordTrie.root)
                if self.num_words == 0:
                    break

        return result
