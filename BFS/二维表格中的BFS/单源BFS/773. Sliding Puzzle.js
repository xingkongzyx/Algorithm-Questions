/*
* 计算 2x3 滑动拼图从初始状态到目标状态所需的最少移动次数
* 目标状态为：1,2,3
             4,5,0

# 解法概况:            
# 将 2×3 棋盘展平为长度为 6 的字符串，每个状态节点可通过将 “0” 与其上下左右相邻位置的数字交换来生成相邻状态。
# 用 BFS 按层遍历这些状态，记录已访问过的字符串以防重复，并在第一次遇到目标状态时返回当前步数。
# 通过预先计算好每个下标可交换的位置，避免了在遍历时反复计算移动合法性。

? https://labuladong.online/algo/essential-technique/bfs-framework/#%E4%BA%8C%E3%80%81773-%E6%BB%91%E5%8A%A8%E8%B0%9C%E9%A2%98
*/
var slidingPuzzle = function (board) {
    /* 
    定义一维位置 0~5 的相邻索引，用于图扩展（邻接表）
    在这段代码里，neighbors 数组就是把 2×3 的棋盘按「行优先」拍平成一维后，针对每个下标（0 到 5）预先写好的“能和空格（0）交换”的下标列表。具体地：
    """
    [
        [1, 3],    // (0,0) → 右(0,1)=1、下(1,0)=3
        [0, 2, 4], // (0,1) → 左(0,0)=0、右(0,2)=2、下(1,1)=4
        [1, 5],    // (0,2) → 左(0,1)=1、下(1,2)=5
        [0, 4],    // (1,0) → 上(0,0)=0、右(1,1)=4
        [1, 3, 5], // (1,1) → 上(0,1)=1、左(1,0)=3、右(1,2)=5
        [2, 4],    // (1,2) → 上(0,2)=2、左(1,1)=4
    ]
    """
    这样，拿到当前状态字符串中空格 0 的一维下标 zeroIndex 后，就能立刻通过 neighbors[zeroIndex] 得到所有合法的交换位置。
    */
    const neighbors = [
        [1, 3], // 0 可与 1 和 3 交换
        [0, 2, 4], // 1 可与 0, 2, 4 交换
        [1, 5], // 2 可与 1 和 5 交换
        [0, 4], // 3 可与 0 和 4 交换
        [1, 3, 5], // 4 可与 1, 3, 5 交换
        [2, 4], // 5 可与 2 和 4 交换
    ];

    // 将二维数组展平成一维数组字符串，如："1,2,3,4,0,5"
    const flattenBoard = board.flat().join(",");
    const target = "1,2,3,4,5,0";

    // 若初始即是目标状态，直接返回 0
    if (flattenBoard === target) return 0;

    // 初始化 BFS 队列和访问集合
    const queue = [flattenBoard];
    const visited = new Set([flattenBoard]);

    let steps = 0;

    // 开始 BFS 遍历
    while (queue.length > 0) {
        const levelSize = queue.length;
        steps++; // 每轮扩展一层，步数+1

        for (let i = 0; i < levelSize; i++) {
            const current = queue.shift();
            const nextStates = getNeighbors(current);

            for (const next of nextStates) {
                // 找到目标状态，立即返回当前步数
                if (next === target) return steps;

                if (!visited.has(next)) {
                    visited.add(next);
                    queue.push(next);
                }
            }
        }
    }

    // 无法到达目标状态
    return -1;

    /**
     * 给定当前一维字符串状态，枚举所有“0 与相邻数字交换”能到达的新状态。
     * @param {string} state - 当前拼图状态，如 "1,2,3,4,0,5"
     * @returns {string[]} - 所有可达的下一状态字符串
     */
    function getNeighbors(state) {
        const res = [];
        const arr = state.split(","); // 转换为数组以便交换
        const zeroIdx = arr.indexOf("0"); // 找出空格位置

        for (const adjIdx of neighbors[zeroIdx]) {
            // 交换 0 与相邻值，生成新状态
            [arr[zeroIdx], arr[adjIdx]] = [arr[adjIdx], arr[zeroIdx]];
            res.push(arr.join(","));
            // 恢复原状态，便于下一次交换
            [arr[zeroIdx], arr[adjIdx]] = [arr[adjIdx], arr[zeroIdx]];
        }

        return res;
    }
};
