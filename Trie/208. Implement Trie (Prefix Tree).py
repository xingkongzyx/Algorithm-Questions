""" 
? 非常好: https://leetcode.cn/problems/implement-trie-prefix-tree/solution/by-lfool-k6hb/
? https://leetcode.cn/problems/implement-trie-prefix-tree/solution/shi-xian-trie-qian-zhui-shu-qian-zhui-sh-2acp/

/ 时间复杂度: 初始化为 O(1), 其余操作为 O(|S|). 其中 |S| 是每次插入或查询的字符串的长度。
/ 空间复杂度: O(|T| * Σ). T 为所有插入的字符串长度之和。Σ 为字符集的大小, |Σ|=26
"""


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curTrieNode = self.root

        for char in word:
            if char not in curTrieNode.children:
                # * create a new TrieNode for the new character
                curTrieNode.children[char] = TrieNode()

            curTrieNode = curTrieNode.children[char]
        curTrieNode.isEnd = True

    def search(self, word: str) -> bool:
        curTrieNode = self.root

        for char in word:
            if char not in curTrieNode.children:
                return False

            curTrieNode = curTrieNode.children[char]

        return curTrieNode.isEnd

    def startsWith(self, prefix: str) -> bool:
        curTrieNode = self.root
        for char in prefix:
            if char not in curTrieNode.children:
                return False
            curTrieNode = curTrieNode.children[char]

        return True

        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
