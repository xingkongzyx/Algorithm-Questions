""" 
/ 时间复杂度: addWord() 的时间复杂度为 O(n), n 为输入单词的平均长度, search() 的平均时间复杂度为 O(n), 最坏情况下查找的单词全是点, 所以最坏的时间复杂度为 O(n^C), C 固定为 26。
/ 空间复杂度: O(C*N), C 固定为 26, N 为输入单词的长度之和, 最坏情况为所有单词都没有共同的前缀, 每个单词中的每个字母都要占用 O(C) 的空间。
? https://leetcode.cn/problems/design-add-and-search-words-data-structure/solution/yu-dao-tong-pei-fu-shi-di-gui-chu-li-python-dai-ma/
? 带注释: https://leetcode.cn/problems/design-add-and-search-words-data-structure/solutions/1054648/python-qian-zhui-zi-dian-shu-dfsjian-zhi-g6r0/?orderBy=most_votes

! 关于这道问题的难点是通配符 "." 的处理，其实也不难：在遇到 "." 的时候，使用递归方法，将该结点的每一个分支都看过去，只要有一个分支返回 true 就可以了，全部分支都走过去，都没有返回 true 的才返回 false。

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
        # * 如果当前字符是字母, 则判断当前字符对应的子结点是否存在, 如果子结点不存在则说明单词不存在, 返回 false; 如果子结点存在则移动到子结点, 继续搜索下一个字符(继续搜索是指继续对下一个字符进行递归搜索)
            if curChar not in curNode.children:
                return False
            else:
                nxtNode = curNode.children[curChar]
                return self.backtracking(word, nxtNode, curIdx + 1)
        else:
        # * 如果当前字符是点号, 由于点号可以表示任何字母, 因此需要对当前结点的所有子结点再继续检查下一个字符, 只要有一组满足条件, 则能够立即返回 true
        # # 这里便包含了回溯的步骤, 如果当前子节点返回 false, 则回溯到上一个状态, 然后对下一个子节点继续进行搜索
            for childChar in curNode.children:
                nxtNode = curNode.children[childChar]
                tempRes = self.backtracking(word, nxtNode, curIdx + 1)
                if tempRes:
                    return True
            return False
