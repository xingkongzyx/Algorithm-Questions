/* 
## 代码逻辑讲解
* 1. **为什么要建｢反图｣ (`reverseAdj`)？**
    我们想从｢已经安全的节点｣往回看，看看哪些节点指向了它们。若一个节点的所有后继都安全，它也安全。反图能让我们快速找到｢谁指向了当前安全节点｣。
* 2. **`remainingOut` 的意义**
    初始时，`remainingOut[u]` 等于原图中 u 的出边数量。每当我们确认了一条出边的目标节点是安全的，就把这条边从“未确认”集合里剔除（`remainingOut[u]--`）。当它减到 0，意味着 u 的所有后继都安全，于是 u 也安全。
* 3. **队列的作用**
    队列里始终装的是｢刚刚被确认安全｣的节点。我们用它来继续反推，看看有没有其它节点因此变得安全 —— 这就是一个典型的｢拓扑排序式｣传播过程。

## 举例说明它为什么能工作

* 以示例 `[[1,2],[2,3],[5],[0],[5],[],[]]` 为例：
* 原图出度计数 `remainingOut` 初始为：
  ```
  节点:   0  1  2  3  4  5  6
  出度:   2  2  1  1  1  0  0
  ```

* 出度为 0 的节点是 5、6，入队：`queue = [5, 6]`
! 原因是题目的定义: A node is a terminal node if there are no outgoing edges.

* 处理节点 5（安全）：
  反图里，谁指向 5？节点 2 和 4

  * 对 2：remainingOut[2] 由 1 → 0，入队
  * 对 4：remainingOut[4] 由 1 → 0，入队
    `queue = [5, 6, 2, 4]`

* 处理节点 6（安全）：
  没有人指向 6，略过。

* 处理节点 2（安全）：
  指向 2 的是 0、1

  * 0：remainingOut\[0] 2 → 1（还没到 0，不入队）
  * 1：remainingOut\[1] 2 → 1

* 处理节点 4（安全）：
  没有人指向 4，略过。

* 队列耗尽，最终被标记安全的是 `{2, 4, 5, 6}`。
  节点 0、1、3 仍各有至少一条出边指向“不安全”的节点（它们之间形成环），因此不安全。

* **关键点**：
* 我们只在某节点的所有出边都指向安全节点时才把它视为安全。
* 这个判断通过 `remainingOut` 是否为 0 实现。
* 通过反图，我们能高效地把“安全信息”向前驱节点传播。
*/

/**
 * 返回所有“最终安全节点”：
 * 这些节点沿着任意路径最终都会到达出度为 0 的节点，而不会进入环。
 *
 * 思路：反图 + 出度计数（拓扑式消减）
 * 1. 统计每个点还剩多少条未被“证明安全”的出边（remainingOut）
 * 2. 构建反图 reverseAdj：v <- u 表示 u 指向 v（原图边 u->v 的逆）
 * 3. 先把所有出度为 0 的点入队，它们天然安全
 * 4. 不断出队一个安全点 v，遍历它在反图中的所有前驱 u
 *    - 对 u 来说，有一条出边 u->v 已被证明安全，将 remainingOut[u]--；
 *    - 若 u 的 remainingOut 变为 0，说明 u 的所有后继都安全，u 也安全，入队
 * 5. 队列处理完，所有标记为安全的点即为结果
 *
 * @param {number[][]} graph - 邻接表形式的有向图，graph[u] = u 指向的所有 v
 * @returns {number[]} 升序排列的安全节点下标
 */
function eventualSafeNodes(graph) {
    const n = graph.length;

    // reverseAdj[v] = 所有指向 v 的前驱节点集合（反图的邻接表）
    const reverseAdj = Array.from({ length: n }, () => []);

    // remainingOut[u] = 当前还剩多少条“未确认安全”的出边
    const remainingOut = new Array(n);

    // 1. 构建 remainingOut 与 reverseAdj
    for (let u = 0; u < n; u++) {
        const targets = graph[u];
        remainingOut[u] = targets.length;
        for (const v of targets) {
            reverseAdj[v].push(u); // 反向记录：v <- u
        }
    }

    // 2. 初始化队列：所有出度为 0 的节点必然安全
    const queue = [];
    for (let i = 0; i < n; i++) {
        if (remainingOut[i] === 0) queue.push(i);
    }

    // 3. BFS/拓扑式消减
    const isSafe = new Array(n).fill(false);
    // 用 head 指针模拟队头，避免 shift() 的 O(n) 开销
    for (let head = 0; head < queue.length; head++) {
        const safeNode = queue[head];
        isSafe[safeNode] = true;

        // safeNode 的所有前驱节点，尝试减少其 remainingOut
        for (const pred of reverseAdj[safeNode]) {
            if (--remainingOut[pred] === 0) {
                queue.push(pred); // 该前驱节点所有出边均已指向安全节点 -> 它也安全
            }
        }
    }

    // 4. 按索引顺序输出安全节点（索引天然有序，无需再 sort）
    const result = [];
    for (let i = 0; i < n; i++) if (isSafe[i]) result.push(i);
    return result;
}

// 示例
const input = [[1, 2], [2, 3], [5], [0], [5], [], []];
console.log(eventualSafeNodes(input)); // => [2, 4, 5, 6]
