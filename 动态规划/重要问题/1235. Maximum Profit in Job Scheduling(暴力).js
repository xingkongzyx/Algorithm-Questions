/* 
这个暴力递归版的核心函数是：

```javascript
function dfs(index) {
    ...
}
```

它的含义是：

> **从排序后的第 `index` 个工作开始考虑，最多可以获得多少利润。**

注意，这里的 `index` 不是原始输入里的工作编号，而是 **按开始时间排序之后的工作下标**。

假设排序后的工作是：

```javascript
jobs = [
    [1, 3, 50],
    [2, 4, 10],
    [3, 5, 40],
    [3, 6, 70]
];
```

那么：

```javascript
dfs(0)
```

表示：从第 `0` 个工作开始考虑，最大收益是多少。

```javascript
dfs(1)
```

表示：从第 `1` 个工作开始考虑，最大收益是多少。

```javascript
dfs(2)
```

表示：从第 `2` 个工作开始考虑，最大收益是多少。

---

**1. 递归终止条件**

```javascript
if (index >= n) {
    return 0;
}
```

意思是：

> 如果已经没有工作可以考虑了，那么最大收益就是 `0`。

比如总共有 `4` 个工作，下标是：

```text
0, 1, 2, 3
```

当递归走到：

```javascript
dfs(4)
```

说明已经越过最后一个工作了，没有任何工作可选，所以返回：

```javascript
0
```

这是递归的出口。

---

**2. 不选当前工作**

```javascript
const skip = dfs(index + 1);
```

意思是：

> 我不做第 `index` 个工作，直接去考虑下一个工作。

例如当前是：

```javascript
dfs(0)
```

也就是正在看：

```javascript
[1, 3, 50]
```

如果不做这个工作，就继续看第 `1` 个工作：

```javascript
dfs(1)
```

所以：

```javascript
const skip = dfs(index + 1);
```

代表 **跳过当前工作后能拿到的最大收益**。

---

**3. 选当前工作**

先取出当前工作的结束时间和收益：

```javascript
const currentEnd = jobs[index][1];
const currentProfit = jobs[index][2];
```

比如当前工作是：

```javascript
[1, 3, 50]
```

那么：

```javascript
currentEnd = 3;
currentProfit = 50;
```

如果选择这个工作，就一定能先拿到：

```javascript
50
```

但是后面不能随便选工作了，只能选开始时间 `>= 3` 的工作。

---

**4. 找下一个不冲突的工作**

```javascript
let nextIndex = index + 1;

while (nextIndex < n && jobs[nextIndex][0] < currentEnd) {
    nextIndex++;
}
```

这段代码的意思是：

> 从当前工作的下一个位置开始，找到第一个开始时间 `>= 当前结束时间` 的工作。

为什么是：

```javascript
jobs[nextIndex][0] < currentEnd
```

因为：

- `jobs[nextIndex][0]` 是后面某个工作的开始时间
- `currentEnd` 是当前工作的结束时间
- 如果后面工作的开始时间 `< currentEnd`，说明时间重叠，不能选

所以继续往后找。

举例：

```javascript
jobs = [
    [1, 3, 50],
    [2, 4, 10],
    [3, 5, 40],
    [3, 6, 70]
];
```

当前选了：

```javascript
[1, 3, 50]
```

它的结束时间是 `3`。

接下来找第一个 `start >= 3` 的工作：

```javascript
[2, 4, 10] // start = 2，小于 3，冲突，跳过
[3, 5, 40] // start = 3，可以选
```

所以：

```javascript
nextIndex = 2
```

---

**5. 计算选当前工作的收益**

```javascript
const take = currentProfit + dfs(nextIndex);
```

意思是：

> 做当前工作获得 `currentProfit`，再加上从 `nextIndex` 开始能获得的最大收益。

例如：

```javascript
currentProfit = 50;
nextIndex = 2;
```

那么：

```javascript
const take = 50 + dfs(2);
```

意思是：

```text
我做 [1,3,50] 这个工作，后面只能从第 2 个工作继续选。
```

---

**6. 在“选”和“不选”之间取最大值**

```javascript
return Math.max(skip, take);
```

也就是：

```text
当前工作我可以选，也可以不选。
哪种方式赚得更多，就返回哪种。
```

这就是递归的核心：

```javascript
dfs(index) = Math.max(
    dfs(index + 1),
    jobs[index][2] + dfs(nextIndex)
);
```

用公式表示：

$$
dfs(i) = \max(dfs(i + 1), profit_i + dfs(next_i))
$$

---

**完整例子走一遍**

输入：

```javascript
startTime = [1, 2, 3, 3];
endTime   = [3, 4, 5, 6];
profit    = [50, 10, 40, 70];
```

整理并排序后：

```javascript
jobs = [
    [1, 3, 50],
    [2, 4, 10],
    [3, 5, 40],
    [3, 6, 70]
];
```

调用：

```javascript
dfs(0)
```

它会比较两种情况：

```text
不选 jobs[0]：
dfs(1)

选 jobs[0]：
50 + dfs(2)
```

所以：

```text
dfs(0) = max(dfs(1), 50 + dfs(2))
```

继续看：

```text
dfs(2)
```

当前是：

```javascript
[3, 5, 40]
```

两种选择：

```text
不选它：
dfs(3)

选它：
40 + dfs(4)
```

而：

```javascript
dfs(4) = 0
```

因为没有工作了。

再看：

```text
dfs(3)
```

当前是：

```javascript
[3, 6, 70]
```

两种选择：

```text
不选它：
dfs(4) = 0

选它：
70 + dfs(4) = 70
```

所以：

```text
dfs(3) = 70
```

回到：

```text
dfs(2)
```

```text
不选 jobs[2]：dfs(3) = 70
选 jobs[2]：40 + dfs(4) = 40
```

所以：

```text
dfs(2) = 70
```

再回到：

```text
dfs(0)
```

```text
选 jobs[0] = 50 + dfs(2) = 50 + 70 = 120
```

这就是最终答案里的一条最优路径：

```text
[1,3,50] + [3,6,70] = 120
```

---

**为什么这个叫暴力递归**

因为它没有保存已经算过的结果。

比如：

```javascript
dfs(3)
```

可能会被很多不同路径反复调用，每次都重新计算。

所以当工作数量变大时，调用次数会急剧膨胀，最坏接近：

$$
O(2^n)
$$

它适合理解思路，但不适合通过大数据。

---

关键点就是记住这句话：

> `dfs(index)` 表示：**从第 `index` 个工作开始往后选，最多能赚多少钱。**


*/
var jobScheduling = function (startTime, endTime, profit) {
    const n = startTime.length;

    const jobs = [];

    for (let i = 0; i < n; i++) {
        jobs.push([startTime[i], endTime[i], profit[i]]);
    }

    jobs.sort((a, b) => a[0] - b[0]);

    function dfs(index) {
        if (index >= n) {
            return 0;
        }

        // 选择 1：不做当前工作
        const skip = dfs(index + 1);

        // 选择 2：做当前工作
        const currentEnd = jobs[index][1];
        const currentProfit = jobs[index][2];

        let nextIndex = index + 1;

        while (nextIndex < n && jobs[nextIndex][0] < currentEnd) {
            nextIndex++;
        }

        const take = currentProfit + dfs(nextIndex);

        return Math.max(skip, take);
    }

    return dfs(0);
};
