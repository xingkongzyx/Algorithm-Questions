function chess(board) {
    let size = board.length;
    let player_postion_x = 0;
    let player_postion_y = 0;
    const x_list = [];
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            if (board[i][j] === "X") x_list.push(i, j);
            else if (board[i][j] === "O") {
                player_postion_x = i;
                player_postion_y = j;
            }
        }
    }

    let queue = [[player_postion_x, player_postion_y, 0]];
    let maxCount = 0;
    while (queue.length > 0) {
        let [o_row, o_col, count] = queue.shift();
        maxCount = Math.max(maxCount, count);
        if (
            o_row - 2 >= 0 &&
            o_col - 2 >= 0 &&
            board[o_row - 1][o_col - 1] === "X" &&
            board[o_row - 2][o_col - 2] !== "X"
        ) {
            queue.push([o_row - 2, o_col - 2, count + 1]);
        }
        if (
            o_row - 2 >= 0 &&
            o_col + 2 < size &&
            board[o_row - 1][o_col + 1] === "X" &&
            board[o_row - 2][o_col + 2] !== "X"
        ) {
            queue.push([o_row - 2, o_col + 2, count + 1]);
        }
    }
    console.log(maxCount);
    return maxCount;
}

function isIn2dArr(array, search) {
    for (let i = 0; i < array.length; i++) {
        if (array[i].join("") === search.join("")) return true;
    }
    return false;
}
chess(["..X...", "......", "....X.", ".X....", "..X.X.", "...O.."]);
chess(["X....", ".X...", "..O..", "...X.", "....."]);
chess(["......", "....X.", "X.X.X.", "......", "..X.X.", "...O.."]);
