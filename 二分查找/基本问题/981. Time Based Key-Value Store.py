""" 
* 因为是timestamps是单调的, 那么我们可以使用二分法快速确定需要查找的 value 在 potential_list 中的位置

* 调用 set(key, value, timestamp_prev) 所存储的值, 其中 timestamp_prev <= timestamp. 如果有多个这样的值, 则返回对应最大的 timestamp_prev 的那个值, 也就是『最后一个』「<= timestamp」的值. 没有也返回空字符串


/ set 操作：以 O(1) 的复杂度找到某个 key 对应的数组, 利用 timestamp 严格递增的特性, 以 O(1) 复杂度将新 Node 加入当前数组尾部；
/ get 操作：以 O(1) 的复杂度找到某个 key 对应的数组, 利用 timestamp 严格递增的特性, 通过二分以 O(logn) 复杂度找到可能符合条件的 Node。

? https://leetcode.cn/problems/time-based-key-value-store/solution/gong-shui-san-xie-yi-ti-shuang-jie-ha-xi-h5et/

"""


class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []

        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        potential_list = self.data[key]
        left = 0
        right = len(potential_list) - 1

        while left < right:
            mid = left + (right - left + 1) // 2
            if potential_list[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid

        # # 边界情况, 有可能 potential_list 中的所有的 timestamp 都比传入的大, 所以这样的极端情况也要检查并返回 ""
        if potential_list[left][0] <= timestamp:
            return potential_list[left][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
