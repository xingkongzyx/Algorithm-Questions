var solveSudoku = function (board) {
    function backtracking(board) {
        for (let rowIdx = 0; rowIdx < board.length; rowIdx++) {
            for (let colIdx = 0; colIdx < board[0].length; colIdx++) {
                if (board[rowIdx][colIdx] !== ".") continue;
                for (let num = 1; num <= 9; num++) {
                    if (isValid(rowIdx, colIdx, board, String(num))) {
                        board[rowIdx][colIdx] = String(num);
                        if (backtracking(board)) return true;
                        board[rowIdx][colIdx] = ".";
                    }
                }

                return false;
            }
        }
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
