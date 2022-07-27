/* 
> 这道题属于 DFS, 并没有明显的回溯操作
* 若起点处是雷, 即 'M', 直接将其修改为 'X', 游戏结束; 若起点处是空, 即 'E', 则从起点开始向 8 邻域中的空地搜索, 直到到达邻接💥的空地停止。
? https://leetcode.cn/problems/minesweeper/solution/dfs-he-bfs-jie-fa-bu-xu-yao-e-wai-kai-pi-kong-jian/
/ 时间复杂度：O(m × n). 其中 n 和 m 分别代表面板的宽和高。最坏情况下会遍历整个面板。
/ 空间复杂度：O(m × n). 空间复杂度取决于递归的栈深度，而递归栈深度在最坏情况下有可能遍历整个面板而达到 O(m × n)。
 */
const updateBoard = (board, click) => {
    const rowLimit = board.length;
    const colLimit = board[0].length;
    const dx = [1, 1, 1, -1, -1, -1, 0, 0];
    const dy = [1, 0, -1, 0, 1, -1, 1, -1];

    /// 辅助函数, 用于检查当前点是否在 board 的合法区域内
    const inBound = (x, y) =>
        x >= 0 && x < rowLimit && y >= 0 && y < colLimit;

    const backtracking = (x, y) => {
        //# 递归终止条件1, 当前点不在界内或不是"E", 直接返回
        if (!inBound(x, y) || board[x][y] != "E") return;

        let numOfMines = 0;
        //* 统计周围雷的个数
        for (let i = 0; i < 8; i++) {
            const nX = x + dx[i];
            const nY = y + dy[i];
            if (inBound(nX, nY) && board[nX][nY] == "M") {
                numOfMines++;
            }
        }
        //# 递归终止条件2, 当前点周围有雷; 将该位置修改为雷数, 然后终止该路径的搜索。
        if (numOfMines !== 0) {
            board[x][y] = numOfMines + "";
            return;
        }

        //* 如果周围没有雷, 标记B, 递归周围的点
        board[x][y] = "B";
        for (let i = 0; i < 8; i++) {
            backtracking(x + dx[i], y + dy[i]);
        }
    };

    const [cX, cY] = click;
    if (board[cX][cY] == "M") {
        // 第一下就踩雷了
        board[cX][cY] = "X";
    } else {
        backtracking(cX, cY); // 开启dfs
    }
    console.log(board);
    return board;
};

updateBoard(
    [
        ["E", "E", "E"],
        ["E", "M", "E"],
        ["E", "E", "E"],
    ],
    [2, 0]
);
