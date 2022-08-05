/* 
* 放置的规则是: 一行一行考虑皇后可以放置在哪一个位置上, 某一行在考虑某一列是否可以放置皇后的时候, 需要根据前面已经放置的皇后的位置。由于是一行一行考虑放置皇后, 摆放的这些皇后肯定不在同一行
! 棋盘的宽度就是 for循环 的长度, 递归的深度就是棋盘的高度, 这样就可以套进回溯法的模板里了。
? https://programmercarl.com/0051.N%E7%9A%87%E5%90%8E.html#%E6%80%BB%E7%BB%93
? 回溯过程的幻灯片演示: https://leetcode.cn/problems/n-queens/solution/gen-ju-di-46-ti-quan-pai-lie-de-hui-su-suan-fa-si-/
 */
var solveNQueens = function (n) {
    let result = [];
    let chessBoard = new Array(n);
    for (let i = 0; i < chessBoard.length; i++) {
        chessBoard[i] = new Array(n).fill(".");
    }
    function backtracking(startRow, currentChessboard, n) {
        //* 递归终止条件
        if (startRow === n) {
            let stringBoard = new Array(n);
            for (let i = 0; i < n; i++) {
                stringBoard[i] = currentChessboard[i].join("");
            }
            result.push(stringBoard);
            return;
        }
        //* for 循环用于模拟递归树的宽度, 回溯用于模拟树的深度
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
