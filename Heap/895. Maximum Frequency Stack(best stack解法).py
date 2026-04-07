""" 
问: 是否会出现中间的某个栈为空的情况？
答: 不会。因为出栈一定是在元素频率最高的栈上发生的, 即上面动画中最右侧的非空栈。
问: 如果有多个相同频率的数字, 怎么保证弹出的是一定最接近栈顶的那个数字？
答: 因为这个做法本质上就是把原始栈拆分成多个栈, 每个栈都存储着相同频率的数字（这里的频率指的是数字入栈时的频率）, 且保持了原有的入栈顺序, 因此弹出的是一定最接近栈顶的那个数字。

链接: https://leetcode.cn/problems/maximum-frequency-stack/solutions/1998430/mei-xiang-ming-bai-yi-ge-dong-hua-miao-d-oich/

? 代码: https://leetcode.cn/problems/maximum-frequency-stack/solution/895-zui-da-pin-lu-zhan-python-by-bluegre-pux4/
? 动画解释: https://leetcode.com/problems/maximum-frequency-stack/discuss/1862015/BEST-Explanation-Visually




## `self.cnt` 是否必须？

**是的，`self.cnt` 是必须的。** 它在这个解法中承担着不可替代的作用。

### `self.cnt` 的职责

`self.cnt`是一个 `defaultdict(int)`，记录了**每个元素当前的出现频率**。它在两个操作中都被使用：

1. **[`push`](895.%20Maximum%20Frequency%20Stack(best%20stack解法).py:28)**：通过 `self.cnt[val] += 1` 得知 `val` 当前应该被放入哪个频率栈。
2. **[`pop`](895.%20Maximum%20Frequency%20Stack(best%20stack解法).py:34)**：通过 `self.cnt[answer] -= 1` 在弹出后将该元素的频率回退。

### 为什么不能去掉？

假设我们去掉 `self.cnt`，会面临以下问题：

#### 问题 1：`push` 时无法知道元素的频率

调用 [`self.stack[self.cnt[val]].append(val)`](895.%20Maximum%20Frequency%20Stack(best%20stack解法).py:30) 时，需要知道 `val` **目前**的频率才能把它放到正确的频率栈里。没有 `self.cnt`，你就无法 $O(1)$ 地获取这个信息。

#### 问题 2：`pop` 时无法回退元素频率

[`self.cnt[answer] -= 1`](895.%20Maximum%20Frequency%20Stack(best%20stack解法).py:39) 确保下次再 `push` 同一个元素时，频率是正确的。如果没有这一步，频率会持续增长而不会因 `pop` 而回退，导致逻辑错误。

### 能否用 `self.stack` 反推频率？

理论上，你可以遍历 `self.stack` 的所有频率层来"数"某个元素出现了多少次，但这会退化为 $O(n)$ 的时间复杂度，失去了这个解法 $O(1)$ push/pop 的核心优势。

### 数据流示意

```mermaid
graph TD
    subgraph "push(5) → push(7) → push(5) → push(7) → push(4) → push(5)"
        A["self.cnt = {5:3, 7:2, 4:1}"]
        B["self.stack = {<br/>1: [5,7,4]<br/>2: [5,7]<br/>3: [5]}"]
        C["self.maxFreq = 3"]
    end
    A --- B --- C
```

此时执行 `pop()`：
- 从 `self.stack[3]` 弹出 `5`
- `self.cnt[5]` 从 3 → 2（**这一步必须依赖 `self.cnt`**）
- `self.maxFreq` 从 3 → 2

如果之后再 `push(5)`，`self.cnt[5]` 是 2，所以 `+1` 后变为 3，`5` 会被正确放入 `self.stack[3]`。

### 结论

`self.cnt` 是这个解法中**不可或缺**的组成部分，它以 $O(1)$ 的空间代价实现了对每个元素频率的实时追踪，是保证 `push` 和 `pop` 都为 $O(1)$ 的关键。
"""

from collections import defaultdict


class FreqStack:

    def __init__(self):
        # 维护两个字典, 以便快速查询频率和数字

        # 所有频率对应的数字集合, 用list实现后进先出
        self.stack = defaultdict(list)
        # 所有数字对应的频率
        self.cnt = defaultdict(int)
        # o(1)找到最大的频率
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        self.stack[self.cnt[val]].append(val)
        if self.cnt[val] > self.maxFreq:  # 更新self.maxFreq
            self.maxFreq = self.cnt[val]

    def pop(self) -> int:
        answer = self.stack[self.maxFreq].pop()
        if len(self.stack[self.maxFreq]) == 0:
            del self.stack[self.maxFreq]
            self.maxFreq -= 1  # maxFreq 必然是连续的, 直接减一即可
        self.cnt[answer] -= 1
        return answer
