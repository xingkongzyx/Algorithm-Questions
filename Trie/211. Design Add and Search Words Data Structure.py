""" 
/ 时间复杂度: addWord() 的时间复杂度为 O(n), n 为输入单词的平均长度, search() 的平均时间复杂度为 O(n), 最坏情况下查找的单词全是点, 所以最坏的时间复杂度为 O(n^C), C 固定为 26。
/ 空间复杂度: O(C*N), C 固定为 26, N 为输入单词的长度之和, 最坏情况为所有单词都没有共同的前缀, 每个单词中的每个字母都要占用 O(C) 的空间。
? https://leetcode.cn/problems/design-add-and-search-words-data-structure/solutions/1054648/python-qian-zhui-zi-dian-shu-dfsjian-zhi-g6r0/

! 关于这道问题的难点是通配符 "." 的处理, 其实也不难：在遇到 "." 的时候, 使用递归方法, 将该结点的每一个分支都看过去, 只要有一个分支返回 true 就可以了, 全部分支都走过去, 都没有返回 true 的才返回 false。

"""


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        cur = self.root

        # 对于一个单词中的所有字母, 如果不存在则插入对应字典, 并且将指针移动到其孩子对应字符位置的TrieNode上
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
        # 当单词插入完成后, 才把对应位置的isEnd设置为True
        cur.isEnd = True


    def search(self, word: str) -> bool:
        cur = self.root

        def backtracking(node, startIdx):
            nonlocal word

            if startIdx == len(word):
                return True and node.isEnd    # 这里哪怕找到了匹配项, 我们也要确认是否当前匹配段为一个单词（可以回头看看TireNode的举例）, 同时满足才返回True

            for idx in range(startIdx, len(word)):
                # 如果不是'.', 我们只需判断是否该单词存在于当前的TrieNode的children上, 存在即继续向下搜索, 否则返回False
                if word[idx] != '.':
                    if word[idx] not in node.children:
                        return False
                    else:
                        return backtracking(node.children[word[idx]], idx + 1)
                else:
                    # 如果为'.', 且当前TrieNode没有孩子了, 也就是说没有任意一个字母和通配符匹配, 可以直接返回False
                    if not node.children:
                        return False
                    else:
                        # 如果已经发现了完全匹配项, 直接剪枝返回, 避免无效迭代
                        res = False

                        # 因为是通配符, 我们需要匹配所有可能的字符, 直到出现完全匹配项。所以对于任何可能存在于children的字母
                        # 我们都需要尝试匹配, 除非之前已经找到了完全匹配项
                        for key in node.children:
                            tmp = backtracking(node.children[key], idx + 1)

                            # 如果已经发现匹配项了, 直接中断后续迭代
                            res = res or tmp
                            if res:
                                return res
                        return False
        return backtracking(cur, 0)