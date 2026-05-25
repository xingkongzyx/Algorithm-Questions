/* 
David，自底向上 DP 的重点是：**不用递归，而是从后往前把答案一点点填出来**。

**1. `dp[i]` 的含义**

```javascript
dp[i]
```

表示：

```text
从排序后的第 i 个工作开始考虑，最多能获得多少利润
```

所以：

```javascript
dp[0]
```

就是从第 `0` 个工作开始考虑的最大收益，也就是最终答案。

额外有一个：

```javascript
dp[n] = 0
```

表示：

```text
已经没有工作可选了，收益是 0
```

---

**2. 为什么要从后往前算**

状态转移是：

```javascript
dp[i] = Math.max(dp[i + 1], jobs[i][2] + dp[nextIndex]);
```

你会发现，计算 `dp[i]` 需要用到：

```javascript
dp[i + 1]
dp[nextIndex]
```

而 `nextIndex` 一定大于 `i`，因为它表示当前工作后面第一个不冲突的工作。

所以 `dp[i]` 依赖的是它右边的状态。

因此要从右往左算：

```javascript
for (let i = n - 1; i >= 0; i--)
```

这样当你计算 `dp[i]` 时，`dp[i + 1]` 和 `dp[nextIndex]` 都已经算好了。

---

**3. 每个工作都有两个选择**

对于第 `i` 个工作，还是两个选择：

**选择 1：不做当前工作**

```javascript
const skip = dp[i + 1];
```

意思是：

```text
跳过第 i 个工作，从第 i + 1 个工作开始考虑
```

**选择 2：做当前工作**

```javascript
const take = currentProfit + dp[nextIndex];
```

意思是：

```text
做第 i 个工作，拿到 currentProfit，
然后从 nextIndex 开始继续选择后面的工作
```

最后取最大值：

```javascript
dp[i] = Math.max(skip, take);
```

---

**4. `findNextIndex` 的作用**

```javascript
function findNextIndex(targetEnd) {
    let left = 0;
    let right = n;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (starts[mid] >= targetEnd) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
```

它的作用是：

```text
找到第一个 startTime >= 当前工作 endTime 的工作下标
```

因为只有这样的工作才不会和当前工作冲突。

比如当前工作结束时间是 `5`，后面工作开始时间是：

```javascript
starts = [1, 2, 3, 4, 5, 6]
```

第一个 `>= 5` 的位置是下标 `4`。

所以：

```javascript
findNextIndex(5) // 4
```

如果没有任何工作满足条件，它会返回 `n`。

这也没问题，因为：

```javascript
dp[n] = 0
```

表示后面没有工作了。

---

**5. 用例子走一遍**

输入：

```javascript
startTime = [1, 2, 3, 3];
endTime   = [3, 4, 5, 6];
profit    = [50, 10, 40, 70];
```

排序后：

```javascript
jobs = [
    [1, 3, 50],
    [2, 4, 10],
    [3, 5, 40],
    [3, 6, 70]
];
```

初始化：

```javascript
dp = [0, 0, 0, 0, 0]
```

其中：

```javascript
dp[4] = 0
```

表示没有工作可选。

---

从后往前算。

**计算 `i = 3`**

当前工作：

```javascript
[3, 6, 70]
```

做它之后，找第一个 `start >= 6` 的工作，没有，所以：

```javascript
nextIndex = 4
```

不做：

```javascript
skip = dp[4] = 0
```

做：

```javascript
take = 70 + dp[4] = 70
```

所以：

```javascript
dp[3] = 70
```

现在：

```javascript
dp = [0, 0, 0, 70, 0]
```

---

**计算 `i = 2`**

当前工作：

```javascript
[3, 5, 40]
```

找第一个 `start >= 5` 的工作，没有：

```javascript
nextIndex = 4
```

不做：

```javascript
skip = dp[3] = 70
```

做：

```javascript
take = 40 + dp[4] = 40
```

取最大：

```javascript
dp[2] = 70
```

意思是：

```text
从第 2 个工作开始看，最优选择不是做 [3,5,40]，
而是跳过它，做 [3,6,70]
```

现在：

```javascript
dp = [0, 0, 70, 70, 0]
```

---

**计算 `i = 1`**

当前工作：

```javascript
[2, 4, 10]
```

找第一个 `start >= 4` 的工作，没有：

```javascript
nextIndex = 4
```

不做：

```javascript
skip = dp[2] = 70
```

做：

```javascript
take = 10 + dp[4] = 10
```

所以：

```javascript
dp[1] = 70
```

现在：

```javascript
dp = [0, 70, 70, 70, 0]
```

---

**计算 `i = 0`**

当前工作：

```javascript
[1, 3, 50]
```

找第一个 `start >= 3` 的工作：

```javascript
nextIndex = 2
```

不做：

```javascript
skip = dp[1] = 70
```

做：

```javascript
take = 50 + dp[2] = 50 + 70 = 120
```

所以：

```javascript
dp[0] = 120
```

最终：

```javascript
return dp[0]; // 120
```

---

**6. 和递归版的关系**

递归版是：

```javascript
dfs(i) = Math.max(dfs(i + 1), profit + dfs(nextIndex));
```

自底向上 DP 是：

```javascript
dp[i] = Math.max(dp[i + 1], profit + dp[nextIndex]);
```

本质完全一样。

只是递归版是从 `dfs(0)` 往下问：

```text
我要 dp[0]，那我先去算 dp[1] 和 dp[nextIndex]
```

自底向上是从最后面开始填：

```text
我先把后面的答案算好，再反过来推前面的答案
```

---

**一句话总结**

自底向上 DP 的核心是：

> `dp[i]` 表示从第 `i` 个工作开始能赚的最大钱；因为它依赖右边的状态，所以从后往前计算；每一步都比较“跳过当前工作”和“选择当前工作”哪个收益更大。
*/

var jobScheduling = function (startTime, endTime, profit) {
    const n = startTime.length;
    const jobs = [];

    for (let i = 0; i < n; i++) {
        jobs.push([startTime[i], endTime[i], profit[i]]);
    }

    jobs.sort((a, b) => a[0] - b[0]);

    const starts = jobs.map((job) => job[0]);
    const dp = new Array(n + 1).fill(0);

    function findNextIndex(targetEnd) {
        let left = 0;
        let right = n;

        while (left < right) {
            const mid = Math.floor((left + right) / 2);

            if (starts[mid] >= targetEnd) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    for (let i = n - 1; i >= 0; i--) {
        const currentEnd = jobs[i][1];
        const currentProfit = jobs[i][2];
        const nextIndex = findNextIndex(currentEnd);

        const skip = dp[i + 1];
        const take = currentProfit + dp[nextIndex];

        dp[i] = Math.max(skip, take);
    }

    return dp[0];
};
