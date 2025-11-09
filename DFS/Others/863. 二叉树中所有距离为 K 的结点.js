/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * 题意：返回与 target 节点距离为 k 的所有节点值
 * 思路：
 * 1. 将二叉树转换成无向图（每条边都是双向的）
 * 2. 从 target 出发执行 BFS，找到距离为 k 的所有节点
 */

var distanceK = function (root, target, k) {
    const graph = new Map(); // Map<number, number[]>，键和值都用节点的 val 表示

    /**
     * 使用 BFS 建立无向图
     * 每个节点与其左右子节点相连（双向边）
     */
    function buildGraph(node) {
        if (!node) return;
        const queue = [node];

        while (queue.length) {
            const cur = queue.shift(); // 当前节点
            const v = cur.val; // 当前节点值

            // 确保当前节点在图中有一个空邻接表
            if (!graph.has(v)) graph.set(v, []);

            // 处理左子节点
            if (cur.left) {
                queue.push(cur.left);
                const lv = cur.left.val; // 左子节点值
                if (!graph.has(lv)) graph.set(lv, []);
                // 双向连接
                graph.get(v).push(lv);
                graph.get(lv).push(v);
            }

            // 处理右子节点
            if (cur.right) {
                queue.push(cur.right);
                const rv = cur.right.val; // 右子节点值
                if (!graph.has(rv)) graph.set(rv, []);
                // 双向连接
                graph.get(v).push(rv);
                graph.get(rv).push(v);
            }
        }
    }

    // 第一步：建图
    buildGraph(root);

    // 第二步：从 target 节点出发执行 BFS
    const t = target.val; // 注意：用节点值而不是节点对象
    if (!graph.has(t)) return [];

    // 特殊情况：k = 0，直接返回自身
    if (k === 0) return [t];

    const visited = new Set([t]); // 记录访问过的节点值
    let queue = [t]; // 当前层队列（节点值）

    // BFS，层序遍历直到距离为 k
    while (k > 0 && queue.length) {
        const size = queue.length;
        k--;
        for (let i = 0; i < size; i++) {
            const cur = queue.shift();
            for (const nxt of graph.get(cur)) {
                // 如果这个邻居节点没访问过，加入队列
                if (!visited.has(nxt)) {
                    visited.add(nxt);
                    queue.push(nxt);
                }
            }
        }
        // 当 k 变为 0 时，当前队列中的节点即为目标节点
        if (k === 0) return queue;
    }

    // 如果没有符合条件的节点，返回空数组
    return [];
};
