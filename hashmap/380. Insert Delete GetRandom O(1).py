
# ? https://leetcode.cn/problems/insert-delete-getrandom-o1/solution/o1-shi-jian-cha-ru-shan-chu-he-huo-qu-su-rlz2/
class RandomizedSet:

    def __init__(self):
        self.data = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.data.append(val)
            self.map[val] = len(self.data) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        else:
            eleIdx = self.map[val]
            lastEleInData = self.data[-1]
            self.data[eleIdx] = lastEleInData
            self.map[lastEleInData] = eleIdx
            self.data.pop()
            # * 从哈希表中删除的操作在最后进行的原因是防止要删除的是数组的「最后一个元素」，否则有前脚删完，后脚就又被 "self.map[lastEleInData] = eleIdx" 这个代码添加的风险
            del self.map[val]
            return True

    def getRandom(self) -> int:
        return choice(self.data)
