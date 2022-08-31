""" 
* 『拉链法』是说, 我们定义了一个比较小的数组(data), 然后使用 hash 方法求出 key 应该出现在「data 数组」中的位置；但是由于不同的 key 在求完 hash 之后, 可能会存在「碰撞冲突」, 所以「data 数组」并不直接保存元素, 而是每个位置都指向了另一个「子数组」用于存储元素。
* 在查找/删除/添加一个 key 的时候需要两个步骤：① 使用 hash 方法求出 key 应该出现在「data 数组」中的位置 ② 在「data 数组」中这个位置的「子数组」中进行操作。
> 具体的讲解看 705
? 方法3: https://leetcode.cn/problems/design-hashmap/solution/xiang-jie-hashmap-de-she-ji-zai-shi-jian-85k9/
"""


class MyHashMap(object):

    def __init__(self):
        self.base = 3
        self.data = [[] for _ in range(self.base)]
        print(self.data)

    def put(self, key, value):
        hashedKey = self.hashFunc(key)
        for pair in self.data[hashedKey]:
            if pair[0] == key:
                pair[1] = value
                return

        self.data[hashedKey].append([key, value])

    def get(self, key):
        hashedKey = self.hashFunc(key)
        for pair in self.data[hashedKey]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashedKey = self.hashFunc(key)
        for pair in self.data[hashedKey]:
            if pair[0] == key:
                val = pair[1]
                self.data[hashedKey].remove([key, val])

    def hashFunc(self, val):
        return val % self.base


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 3)
param_2 = obj.get(1)
obj.remove(1)
