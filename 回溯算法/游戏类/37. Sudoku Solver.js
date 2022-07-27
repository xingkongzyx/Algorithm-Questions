/* 
* 本题和其他简单回溯题目的最大区别在于, 之前的题目的候选集的待填放位置都是一维的, 所以单层搜索都是用一个 for 循环来确定每一个候选位置的选择; (N皇后问题虽然也是一个棋盘, 但是其每一行只能放一个皇后, 所以我们一行行的的放, 也相当于是一维的问题)。
> dfs找到答案就结束递归的话，可以考虑bool值返回的函数, lc 322 也是一个道理
! 但这次是一个二维棋盘的每个空位都需要填放; 所以此题的单层循环逻辑需要使用两层 for 循环来遍历数独盘的每一个位置, 即每个位置都需要在候选集中做出一次选择。
/ 为什么递归函数要返回值: 我们的回溯是要保证对每一次「非正确答案」的值进行「退回操作」的，而「退回操作」放在递归函数下方，我们无法通过函数的「空返回值」来判断：是否当前递归函数的回归是在我们遍历完整个棋盘后的自然退回（即，当前棋盘就是正确答案），还是当前棋盘的值有问题的递归函数回归，这两种操作的结果是不一样的，所以要用bool 值返回
? https://leetcode.cn/problems/sudoku-solver/solution/kan-liao-wo-de-ti-jie-shou-si-zhe-ge-pap-2s0a/
? 代码随想录: https://leetcode.cn/problems/sudoku-solver/solution/37-jie-shu-du-hui-su-sou-suo-suan-fa-xiang-jie-by-/ 

*/

var solveSudoku = function (board) {
    function backtracking(board) {
        //* 使用两层for循环来遍历 board 中的每一个「空白位置」, 并且每个位置都需要在候选集(1-9) 中尝试填入数字;
        for (let rowIdx = 0; rowIdx < board.length; rowIdx++) {
            for (let colIdx = 0; colIdx < board[0].length; colIdx++) {
                if (board[rowIdx][colIdx] !== ".") continue;
                for (let num = 1; num <= 9; num++) {
                    if (isValid(rowIdx, colIdx, board, String(num))) {
                        //* 选取一个合法数字填入「当前位置」
                        board[rowIdx][colIdx] = String(num);
                        //* 继续递归搜索其他「空白位置」
                        if (backtracking(board)) return true;
                        //* 回溯, 撤销选择;
                        board[rowIdx][colIdx] = ".";
                    }
                }
                //* 若「当前位置」填入的9个数均不满足条件, 则说明此解法无效, 返回 false */
                return false;
            }
        }
        //* 遍历完所有的棋盘，没有返回 false，说明找到了解法，返回 true
        return true;
    }
    backtracking(board);
    return board;
};

function isValid(row, col, board, currentVal) {
    // # 确保数字 1-9 在每一行只能出现一次。
    for (let i = 0; i < 9; i++) {
        if (board[row][i] === currentVal) return false;
    }
    // # 数字 1-9 在每一列只能出现一次。
    for (let i = 0; i < 9; i++) {
        if (board[i][col] === currentVal) return false;
    }

    // # 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
    let startRowInCurrentSubbox = Math.floor(row / 3) * 3;
    let startColInCurrentSubbox = Math.floor(col / 3) * 3;

    for (
        let rowIdx = startRowInCurrentSubbox;
        rowIdx < startRowInCurrentSubbox + 3;
        rowIdx++
    ) {
        for (
            let colIdx = startColInCurrentSubbox;
            colIdx < startColInCurrentSubbox + 3;
            colIdx++
        ) {
            if (board[rowIdx][colIdx] === currentVal) return false;
        }
    }

    return true;
}

const board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
];

console.log(solveSudoku(board));
