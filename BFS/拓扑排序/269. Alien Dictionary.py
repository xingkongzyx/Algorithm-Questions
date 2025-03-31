""" 「」
    ? 非常好的分析: https://leetcode.cn/problems/alien-dictionary/solution/si-lu-jiu-shi-tuo-bu-pai-xu-dan-shi-by-shiman/
    ! 唯一能够判断字母大小关系的条件是: 相邻两个单词中, 第一对不同的字母(前一个小于后一个)。根据大小关系建图, 输出拓扑排序结果即可

    * 使用拓扑排序求解时, 将火星词典中的每个字母看成一个节点, 将字母之间的顺序关系看成「有向边」。对于火星词典中的两个相邻单词, 同时从左到右遍历, 当遇到「第一个」不相同的字母时, 该位置的两个字母之间即存在顺序关系。
    * 以下两种情况不存在合法字母顺序：
    * 1. 字母之间的顺序关系存在由至少 2 个字母组成的环, 例如 words=["a", "b", "a"];
    * 2. 相邻两个单词满足后面的单词是前面的单词的前缀, 且后面的单词的长度「小于」前面的单词的长度, words=["ab", "a"]。
    * 其余情况下都存在合法字母顺序, 可以使用拓扑排序得到字典顺序。
    ? https://leetcode.cn/problems/alien-dictionary/solution/-by-max-lfsznscofe-zf3j/
    ? 代码借鉴: https://leetcode.cn/problems/alien-dictionary/solution/python3-tuo-bu-pai-xu-by-zhouquan/

    / 下面代码的整体思路:
    / ➀ 统计所有的结点（字母）
    / ➁ 建图, 邻接表 - 用字典比较方便
    / ➂ 统计入度
    / ➃ 拓扑排序
    / ➄ 看res是否包含了所有的点(图论中的意义是有无环loop)
    / ➅ 再check一遍, 给的顺序中有无逆序. 前面内容相同, 短的小, 应该在前面. 注意特殊样例['aba'], 这是绝了
    ? https://leetcode.cn/problems/alien-dictionary/solution/cpython3-tuo-bu-pai-xu-topsort-by-hanxin-oyux/

    > 针对于 ["z","x","a","ab","ac"] 的情况，理想情况应输出 "bczxa" 或者 "zxabc"，但我们的答案输出的是 "zbxca" 相当于把所有入度为 0 的元素同时加入了队列，而没有按照每个入度为 0 的元素所代表的后面的 word 顺序进行遍历，但是答案机制没有考虑这一点



    """

from typing import List
class Solution:
    def alienOrder(self, words: List[str]) -> str:
            # # 在排序的单词列表中, 从每两个相邻单词中确认第一对不同的字符, 并确认这对字符的指向关系。注意: 只有第一个不同的字符才是正确的排序, 如 "ert" 和 "wrf" , 只能推断出 "e" 的优先级高于 "w", 剩余字符的优先级不能推断。将字符串的优先级构建为图, 然后进行拓扑排序。如果图中无环, 则将拓扑排序输出, 否则顺序是非法的。同时还要考虑到一种特例, 形如 ["abc", "ab"] 这样的相邻单词是违反题目关于单词排序定义的, 要返回空。

            # * 每个字母代表图的一个顶点; 邻接表表示有向图.
            graph = {}
            inDegree = {}

           # * 初始化 graph 和入度表. 注意这个初始化是要对每个出现的字符都进行初始化
           # / 为什么每个出现的字符都要初始化呢? 例如 words = [zab], 此时，你需要把 z, a, b 这三个字符也都搞在一起，随便输出一个 "zab" 的排列。为了达到这个效果就得把所有的字符加入到 inDegree 中，这就像在 course schedule题目中创建的 inDegree 数组是包含所有课程编号的，无论它是否有前置课，这样才能保证所有的课都能上到。这里也是一样，所有的字符加入到 inDegree 中才能保证初始化 queue 时加入所有入度为 0 的元素时，能够让所有字符都被使用到。

            for word in words:
                for char in word:
                    if char not in graph:
                        graph[char] = []
                        inDegree[char] = 0
            # * 两两单词中的每个字母进行比较, 确定图的方向.
            for i in range(len(words) - 1):
                wordOne = words[i]
                wordTwo = words[i + 1]
                minLen = min(len(wordOne), len(wordTwo))
                j = 0
                while j < minLen:
                    if wordOne[j] != wordTwo[j]:
                        # * 当前的两个字母按这门新语言的字母顺序进行了排序, 所以优先级高 -> 优先级低。 加入graph。
                        graph[wordOne[j]].append(wordTwo[j])
                        # ! 为什么这里需要break？当前的两个字母不同, 字母顺序也不同; 所以单词在字典中的排序顺序只和这两个字母有关, 而和后面的无关。因此我们需要看下一个单词对比而不是当前单词的字母对比。
                        break
                    j += 1

            # * 填充入度表
            for nexts in graph.values():
                for next_char in nexts:
                    inDegree[next_char] += 1

            # * 把入度为0的点装进queue里
            queue = collections.deque()
            for key in inDegree.keys():
                if inDegree[key] == 0:
                    queue.append(key)

            res = []
            while queue:
                pre = queue.popleft()
                res.append(pre)

                # * 删除了pre节点, 那么这个pre所对应的next,全部的入度都要-1. 然后顺带检查next的入度是否为0,  如果为0的话那么要把next加入queue.
                for next in graph[pre]:
                    inDegree[next] -= 1
                    if inDegree[next] == 0:
                        queue.append(next)
            is_bad_dag = False
            # * 判断有向图是否有环: 出队元素个数不等于图顶点个数, 说明有环
            if len(res) != len(inDegree):
                is_bad_dag = True

            # * abc 排在 ab 前面, 也属于非法输入。这种情况, a-> a b->b 不可能, c -> "" 也不可能
            for i in range(len(words) - 1):
                wordOne = words[i]
                wordTwo = words[i + 1]
                wordOneLen = len(wordOne)
                wordTwoLen = len(wordTwo)
                if wordOneLen > wordTwoLen and wordOne[:wordTwoLen] == wordTwo:
                    is_bad_dag = True
                    break
            return "" if is_bad_dag else "".join(res)
