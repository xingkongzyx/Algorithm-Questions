//? 与 79 题非常像
//? https://leetcode.cn/problems/path-with-maximum-gold/solution/hui-su-suan-fa-tu-wen-xiang-jie-by-sdwwld/
/// 复杂度的分析: https://leetcode.cn/problems/path-with-maximum-gold/solution/tong-ge-lai-shua-ti-la-duo-yuan-dfs-hui-l53w6/
var getMaximumGold = function (grid) {
    let numRows = grid.length;
    let numCols = grid[0].length;
    let visited = new Array(numRows);
    for (let i = 0; i < numRows; i++) {
        visited[i] = new Array(numCols).fill(false);
    }

    let directions = [
        [0, 1],
        [1, 0],
        [-1, 0],
        [0, -1],
    ];
    let maxVal = 0;
    for (let i = 0; i < numRows; i++) {
        for (let j = 0; j < numCols; j++) {
            if (grid[i][j] !== 0) {
                let curVal = backtracking(i, j);
                console.log(
                    `current position is ${grid[i][j]}, curVal is ${curVal}`
                );
                maxVal = Math.max(curVal, maxVal);
            }
        }
    }
    /// 函数的作用是: 以(rowIdx, colIdx) 为起始坐标点, 沿着他的「上下左右」4 个方向查找可以挖到最多金子的路径。在这个过程中只能选择「当前坐标」「四个方向」中其中的「一个方向」挖出的金子作为结果, 而不能「左边挖到的金子+右边挖到的金子+上边挖到的金子+下边挖到的金子」这样加一起作为结果。题目中有要求: From your position, you can walk one step to the left, right, up, or down. 〖or〗这个单词说明了要求。
    function backtracking(rowIdx, colIdx) {
        /*
         * 递归终止条件有哪些:
         * ➀ 当前的点, 越出矩阵边界。
         * ➁ 当前的点, 之前访问过, 不满足「每个单元格只能被开采（进入）一次」。
         * ➂ 当前的点, 黄金数目为 0
         */
        if (
            isValid(rowIdx, colIdx) === false ||
            grid[rowIdx][colIdx] === 0 ||
            visited[rowIdx][colIdx] === true
        ) {
            return 0;
        }

        let curVal = grid[rowIdx][colIdx];

        //* 标记这个位置已经被搜索过
        visited[rowIdx][colIdx] = true;

        //* 然后沿着当前坐标的「上下左右」4个方向查找
        let directionMaxVal = 0;
        for (let i = 0; i < directions.length; i++) {
            let [x_offset, y_offset] = directions[i];
            rowIdx = rowIdx + x_offset;
            colIdx = colIdx + y_offset;
            //* 获取「4个方向」扩散的最大值
            directionMaxVal = Math.max(
                directionMaxVal,
                backtracking(rowIdx, colIdx)
            );
            //* 回溯，撤回更新后的坐标
            rowIdx = rowIdx - x_offset;
            colIdx = colIdx - y_offset;
        }

        curVal += directionMaxVal;
        //* 回溯, 撤回标记
        visited[rowIdx][colIdx] = false;
        return curVal;
    }
    function isValid(rowIdx, colIdx) {
        return (
            rowIdx >= 0 &&
            rowIdx < numRows &&
            colIdx >= 0 &&
            colIdx < numCols
        );
    }
    return maxVal;
};

const grid = [
    [1, 0, 7],
    [2, 0, 6],
    [3, 4, 5],
    [0, 3, 0],
    [9, 0, 20],
];
getMaximumGold(grid);
