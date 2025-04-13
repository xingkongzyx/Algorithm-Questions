/**
 * @param {number[][]} grid - 输入的二进制矩阵（0 表示可通行，1 表示障碍）
 * @return {number} - 返回从左上角到右下角的最短路径长度（包含起点和终点），无法到达返回 -1
 * ? https://leetcode.cn/problems/shortest-path-in-binary-matrix/solutions/1076268/bfszui-duan-lu-jing-wen-ti-bfsdfsde-si-k-ngc5
 */
var shortestPathBinaryMatrix = function (grid) {
    const n = grid.length;

    // 若起点或终点为障碍，直接无法通行
    if (grid[0][0] !== 0 || grid[n - 1][n - 1] !== 0) return -1;

    // 特殊情况：只有一个格子，且是通路
    if (n === 1) return 1;

    // 定义 8 个方向：上、下、左、右、4 个对角线方向
    const directions = [
        [0, 1],
        [1, 0],
        [1, 1],
        [-1, -1],
        [-1, 0],
        [0, -1],
        [-1, 1],
        [1, -1],
    ];

    // 判断是否在边界范围内
    const inBorder = (x, y) => x >= 0 && x < n && y >= 0 && y < n;

    // 记录访问过的位置，初始化为 false
    const visited = Array.from({ length: n }, () =>
        Array(n).fill(false)
    );
    visited[0][0] = true; // 起点标记为已访问

    const queue = [[0, 0]]; // BFS 队列，起点入队
    let steps = 1; // 初始步数为 1（包含起点）

    // 开始 BFS 遍历
    while (queue.length > 0) {
        const levelSize = queue.length; // 当前层级的节点数

        for (let i = 0; i < levelSize; i++) {
            const [x, y] = queue.shift();

            // 遍历 8 个可能方向
            for (const [dx, dy] of directions) {
                const nx = x + dx;
                const ny = y + dy;

                // 若到达终点且为可通路，返回步数（+1 因为当前为下一层）
                if (
                    nx === n - 1 &&
                    ny === n - 1 &&
                    grid[nx][ny] === 0
                ) {
                    return steps + 1;
                }

                // 判断是否是合法通路、未访问过
                if (
                    inBorder(nx, ny) &&
                    grid[nx][ny] === 0 &&
                    !visited[nx][ny]
                ) {
                    visited[nx][ny] = true; // 标记为已访问
                    queue.push([nx, ny]); // 加入下一层队列
                }
            }
        }

        // 每处理完一层，步数增加
        steps++;
    }

    // 如果 BFS 结束都没找到路径，返回 -1
    return -1;
};
