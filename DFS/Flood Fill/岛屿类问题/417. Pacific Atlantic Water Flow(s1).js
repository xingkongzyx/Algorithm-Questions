/* 
* 对于一个点它能流动到两边的大洋, 那么反过来, 两边大洋的水反着流就能达到这个点。既然水开始倒流了, 那么逻辑也需要反过来, 因此只有当下一个点的高度比当前的点的高度「大于或等于」时, 水才能流过去。
* 为什么这么考虑呢？试想一下, 如果采用「正序」, 我们需要对「每个来源」(本题里即每个节点)做 DFS, 看它是否符合要求。如果采用「倒序」的话, 我们只要从结果开始往上溯源。在本题里, 结果是四条边。明显, 结果数量远小于来源。
? https://leetcode.cn/problems/pacific-atlantic-water-flow/solution/tai-ping-yang-da-xi-yang-shui-liu-wen-ti-f86l/

* 主要步骤: 将水的流向反转, 假设太平洋和大西洋的水「从低向高」攀登, 分别能到达哪些位置, 分别用 p_visited 和 a_visited 表示。两者的『交集』就代表能「同时」流向太平洋和大西洋的位置。

? 思路来源: https://leetcode.cn/problems/pacific-atlantic-water-flow/solution/by-fuxuemingzhu-jqz4/
? 代码来源: https://leetcode.cn/problems/pacific-atlantic-water-flow/solution/417java-dfscong-bian-yuan-wang-li-fang-wen-xiang-j/


/ 时间复杂度: O(mn), 其中 m 和 n 分别是矩阵 heights 的行数和列数。深度优先搜索最多遍历每个单元格两次, 寻找太平洋和大西洋都可以到达的单元格需要遍历整个矩阵, 因此时间复杂度是 O(mn)。
/ 空间复杂度: O(mn), 其中 m 和 n 分别是矩阵 heights 的行数和列数。深度优先搜索的递归调用层数是 O(mn), 记录每个单元格是否可以到达太平洋和大西洋需要 O(mn) 的空间, 因此空间复杂度是 O(mn)。
*/

/**
 * 给定一个 m×n 的高度矩阵 heights，
 * 返回所有既能流向太平洋 (Pacific) 又能流向大西洋 (Atlantic) 的坐标 [i, j]。
 *
 * 思路：分别从矩阵的四条“海洋边界”做反向 DFS，
 * 标记所有可以“逆流”到该边界的格子（只能从高度低的爬到高度高的或相等的）。
 * 最后取两次 DFS 的交集即可。
 */
var pacificAtlantic = function (heights) {
    // 输入校验：确保矩阵非空
    if (!heights || heights.length === 0 || heights[0].length === 0) {
        return [];
    }

    const m = heights.length; // 行数
    const n = heights[0].length; // 列数

    // visitedP[i][j] = true 表示 (i,j) 能通过逆流达到太平洋
    const visitedP = Array.from({ length: m }, () =>
        Array(n).fill(false)
    );
    // visitedA[i][j] = true 表示 (i,j) 能通过逆流达到大西洋
    const visitedA = Array.from({ length: m }, () =>
        Array(n).fill(false)
    );

    // 定义四个方向：右、左、下、上
    const dirs = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ];

    /**
     * 判断坐标 (x, y) 是否在矩阵范围内
     */
    function inBounds(x, y) {
        return x >= 0 && x < m && y >= 0 && y < n;
    }

    /**
     * 反向 DFS 从 (x, y) 开始：
     *   - prevHeight：上一个格子的高度
     *   - 只能在 heights[x][y] >= prevHeight 时才继续，保证“逆流”只能往更高处或持平处走
     *   - visited 数组用来标记已访问格子，避免重复
     */
    function dfs(x, y, prevHeight, visited) {
        // 越界检查
        if (!inBounds(x, y)) return;
        // 已访问检查
        if (visited[x][y]) return;
        // 高度检查：当前格子高度必须 >= 来时的高度
        if (heights[x][y] < prevHeight) return;

        // 标记为已访问（可到达该海洋）
        visited[x][y] = true;

        // 遍历四个方向
        for (const [dx, dy] of dirs) {
            dfs(x + dx, y + dy, heights[x][y], visited);
        }
    }

    // 1) 从太平洋边界（上边界和左边界）发起 DFS
    for (let col = 0; col < n; col++) {
        // 上边界 => 太平洋
        dfs(0, col, -Infinity, visitedP);
    }
    for (let row = 0; row < m; row++) {
        // 左边界 => 太平洋
        dfs(row, 0, -Infinity, visitedP);
    }

    // 2) 从大西洋边界（下边界和右边界）发起 DFS
    for (let col = 0; col < n; col++) {
        // 下边界 => 大西洋
        dfs(m - 1, col, -Infinity, visitedA);
    }
    for (let row = 0; row < m; row++) {
        // 右边界 => 大西洋
        dfs(row, n - 1, -Infinity, visitedA);
    }

    // 3) 收集既能到达太平洋又能到达大西洋的格子
    const result = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (visitedP[i][j] && visitedA[i][j]) {
                result.push([i, j]);
            }
        }
    }

    return result;
};

pacificAtlantic([
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]);
