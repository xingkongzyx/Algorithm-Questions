var solveNQueens = function (n) {
    let result = [];
    let chessBoard = new Array(n);
    for (let i = 0; i < chessBoard.length; i++) {
        chessBoard[i] = new Array(n).fill(".");
    }
    function backtracking(startRow, currentChessboard, n) {
        if (startRow === n) {
            let currentSolution = currentChessboard.map(function (
                arr
            ) {
                return arr.join("");
            });
            result.push(currentSolution);
        }

        for (let col = 0; col < n; col++) {
            if (isValid(startRow, col, currentChessboard)) {
                currentChessboard[startRow][col] = "Q";
                backtracking(startRow + 1, currentChessboard, n);
                currentChessboard[startRow][col] = ".";
            }
        }
    }

    function isValid(row, col, chessBoard) {
        //* 判断不同行的同一列是否有 "Q", 有则说明这个位置不合格, 返回false
        for (let rowIdx = 0; rowIdx < row; rowIdx++) {
            if (chessBoard[rowIdx][col] === "Q") return false;
        }
        //* 判断同斜线是否有 "Q", 有则说明这个位置不合格, 返回false
        //* 这里判断的左上斜线是否有 "Q"
        for (
            let rowIdx = row - 1, colIdx = col - 1;
            rowIdx >= 0 && colIdx >= 0;
            rowIdx--, colIdx--
        ) {
            if (chessBoard[rowIdx][colIdx] === "Q") return false;
        }

        //* 判断同斜线是否有 "Q", 有则说明这个位置不合格, 返回false
        //* 这里判断的右上斜线是否有 "Q"
        for (
            let rowIdx = row - 1, colIdx = col + 1;
            rowIdx >= 0 && colIdx < chessBoard.length;
            rowIdx--, colIdx++
        ) {
            if (chessBoard[rowIdx][colIdx] === "Q") return false;
        }

        return true;
    }
    backtracking(0, chessBoard, n);
    return result;
};
let res = solveNQueens(4);
console.log(res);
