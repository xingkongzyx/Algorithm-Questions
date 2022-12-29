""" 
? https://leetcode.cn/problems/design-add-and-search-words-data-structure/solution/yu-dao-tong-pei-fu-shi-di-gui-chu-li-python-dai-ma/
"""


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curNode = self.root
        for char in word:
            if char not in curNode.children:
                curNode.children[char] = TrieNode()

            curNode = curNode.children[char]

        curNode.isEnd = True

    def search(self, word: str) -> bool:
        return self.backtracking(word, self.root, 0)

    def backtracking(self, word, curNode, curIdx):
        if curIdx == len(word):
            return curNode.isEnd

        curChar = word[curIdx]

        if curChar != ".":
            if curChar not in curNode.children:
                return False
            else:
                nxtNode = curNode.children[curChar]
                return self.backtracking(word, nxtNode, curIdx + 1)
        else:
            for childChar in curNode.children:
                nxtNode = curNode.children[childChar]
                tempRes = self.backtracking(word, nxtNode, curIdx + 1)
                if tempRes:
                    return True

        return False
