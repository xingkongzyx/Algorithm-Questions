""" 
* 『拉链法』是说, 我们定义了一个比较小的数组(data), 然后使用 hash 方法求出 key 应该出现在「data 数组」中的位置；但是由于不同的 key 在求完 hash 之后, 可能会存在「碰撞冲突」, 所以「data 数组」并不直接保存元素, 而是每个位置都指向了另一个「子数组」用于存储元素。
* 在查找/删除/添加一个 key 的时候需要两个步骤：① 使用 hash 方法求出 key 应该出现在「data 数组」中的位置 ② 在「data 数组」中这个位置的「子数组」中进行操作。
? 详解, 必看: https://leetcode.cn/problems/design-hashset/solution/xiang-jie-hashset-de-she-ji-zai-shi-jian-4plc/
? 官解: https://leetcode.cn/problems/design-hashset/solution/she-ji-ha-xi-ji-he-by-leetcode-solution-xp4t/

/ 时间复杂度: O(N/b), N 是元素个数, b 是桶数。
/ 空间复杂度: O(N)
"""


class MyHashSet:

    def __init__(self):
        self.base = 1000
        self.data = [[] for _ in range(self.base)]

    def add(self, key: int) -> None:
        hashedKey = self.hash(key)
        for storedKey in self.data[hashedKey]:
            if storedKey == key:
                return

        self.data[hashedKey].append(key)

    def remove(self, key: int) -> None:
        hashedKey = self.hash(key)
        for i in range(len(self.data[hashedKey])):
            if self.data[hashedKey][i] == key:
                self.data[hashedKey].pop(i)
                return

    def contains(self, key: int) -> bool:
        hashedKey = self.hash(key)
        for storedKey in self.data[hashedKey]:
            if storedKey == key:
                return True
        return False

    def hash(self, key):
        return key % self.base
