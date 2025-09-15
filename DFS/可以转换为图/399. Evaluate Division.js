/* 
* DFS 中的难题
? 思路讲解 https://leetcode.cn/problems/evaluate-division/solutions/512094/dfsxiang-jie-pou-xi-guo-cheng-qi-shi-hen-aqin
*/

/**
 * 计算多个变量比值的结果：LeetCode 399. Evaluate Division（仅 DFS 版, 无缓存）
 * @param {string[][]} equations - 形如 [["a","b"], ["b","c"], ...]
 * @param {number[]} values - 对应的比值, 比如 a / b = values[0]
 * @param {string[][]} queries - 询问的比值, 比如 ["a","c"] 表示 a / c
 * @return {number[]} 每个 query 的结果, 找不到路径则是 -1.0
 */
var calcEquation = function (equations, values, queries) {
    // 构建图的邻接表：每个变量指向它的邻居和对应的权重（比值）
    // graph.get(x) = [[y, x/y], ...]
    const graph = new Map();
    /**
     * 构造加权无向图（邻接表表示）
     * 每个 equation a / b = v, 意味着：
     *   a -> b 权重 v
     *   b -> a 权重 1 / v
     */
    for (let i = 0; i < equations.length; i++) {
        const [a, b] = equations[i];
        const value = values[i];

        if (!graph.has(a)) graph.set(a, []);
        if (!graph.has(b)) graph.set(b, []);

        graph.get(a).push([b, value]); // a / b = value
        graph.get(b).push([a, 1 / value]); // b / a = 1 / value
    }

    const answers = [];

    for (const [source, target] of queries) {
        // 如果任一变量不在图中, 答案必定是 -1.0
        if (!graph.has(source) || !graph.has(target)) {
            answers.push(-1.0);
            continue;
        }

        // 同一个变量的比值是 1（例如 a / a）
        if (source === target) {
            answers.push(1.0);
            continue;
        }

        // 用于防止在 DFS 中重复访问导致环形死循环
        const visited = new Set();

        // 启动 DFS, 累积路径乘积; 找不到返回 null
        const result = dfs(source, target, 1.0, visited, graph);

        // 规则要求：找不到路径返回 -1.0
        answers.push(result === null ? -1.0 : result);
    }

    return answers;
};

/**
 * 深度优先搜索：寻找从 current 到 target 的一条路径, 并返回累积比值
 * @param {string} current - 当前节点
 * @param {string} target - 目标节点
 * @param {number} accumulatedProduct - 从起点到 current 的累积比值
 * @param {Set<string>} visited - 已访问节点集合（避免环）
 * @param {Map<string, Array<[string, number]>>} graph - 邻接表
 * @returns {number|null} 找到路径返回比值, 否则返回 null
 */
function dfs(current, target, accumulatedProduct, visited, graph) {
    // 找到目标, 直接返回当前的累积乘积（即 source / target）
    if (current === target) return accumulatedProduct;

    visited.add(current); // 标记当前节点为已访问

    const neighbors = graph.get(current) || [];

    // 逐个尝试邻居：相当于沿着边不断累乘权重
    for (const [neighbor, weight] of neighbors) {
        if (visited.has(neighbor)) continue; // 跳过已经走过的, 防环

        // 递归：路径乘上当前边的比值
        const res = dfs(
            neighbor,
            target,
            accumulatedProduct * weight,
            visited,
            graph
        );
        if (res !== null) {
            return res; // 一旦找到就短路返回
        }

        /* 
        ! visited.add(current) 之后为什么不在回溯时做 visited.delete(current)？
        # 在这段 DFS 里，visited 不是用来做“当前路径上的临时标记再回溯撤销”的（那是经典回溯需要撤销的场景），而是全局一次性标记某个节点已经被访问过并展开过，目的是避免重复遍历和环。
        # 因为一旦你从某个节点 cur 走过它的所有邻居（即它那一整棵子树/能到达的部分）之后，再从别的路径“绕回来”重新访问 cur 只会重复做已经做过的工作，对能否找到目标没有新增贡献。
        # 所以不撤销（不 delete）是合理的，反而避免了额外冗余。
        
        # 具体举例说明
        # 假设有一条路径 A → B → D，你在 DFS 过程中先到达 B，并从 B 递归探索它的所有可达节点（包括 D）。

            # 如果这个分支成功找到了目标，直接返回，后续不需要再看其他路径。
            # 如果这个分支没找到目标（说明 B 的整个子图都不能通到目标），那说明从 B 出发无论怎么走都走不通。此时再从 A 经由其它路径（例如 A → C → B）回到 B 也没意义：B 本身已经“穷尽”了它所有的出路，重复访问只会浪费。
        # 因此，把某个节点在第一次访问后永久标记为已访问可以安全地剪掉重复分支，等价于“已处理过的子树不再重走”。
        */
    }

    // 没有合适路径
    return null;
}
