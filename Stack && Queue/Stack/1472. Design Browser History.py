""" 
? https://leetcode.cn/problems/design-browser-history/solution/yong-shu-zu-shi-xian-quan-o1de-she-ji-by-x0sr/
? 代码借鉴: https://leetcode.cn/problems/design-browser-history/solution/-by-wywy-m-brat/
/ 时间复杂度: O(1)
"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.data = [homepage]
        # * 表示当前「正在访问」的位置
        self.curIdx = 0
        # * 表示最后一个有效的位置，或者说能够 forward 的「最远位置」，防止访问已经删除的 url
        self.endIdx = 0

    def visit(self, url: str) -> None:
        self.curIdx += 1
        if self.curIdx == len(self.data):
            # # 如果 cur 指针原本就在数组的「最后一个位置」，+1 后，将处于空位，不能直接使用 curIdx 赋值，会出现越界问题。只能使用 append 进行填充
            self.data.append(url)
        else:
            # # 如果 cur 指针在前面，我们只需要把更新后的 curIdx 对应的位置直接改变其原有值。
            self.data[self.curIdx] = url
        # * 最后更新 endIdx, 此时 forward 能到达的最远位置就是 curIdx 的位置
        self.endIdx = self.curIdx

    def back(self, steps: int) -> str:
        self.curIdx = max(0, self.curIdx - steps)
        return self.data[self.curIdx]

    def forward(self, steps: int) -> str:
        self.curIdx = min(self.endIdx, self.curIdx + steps)
        return self.data[self.curIdx]
