/* 
https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/solutions/869920/mi-gong-zhong-chi-ru-kou-zui-jin-de-chu-0ued5/?envType=study-plan-v2&envId=leetcode-75
*/
var nearestExit = function (maze, entrance) {
    const numRows = maze.length;
    const numCols = maze[0].length;

    const inBorder = (x, y) => {
        return 0 <= x && x < numRows && 0 <= y && y < numCols;
    };

    const x_dir = [0, 0, 1, -1];
    const y_dir = [1, -1, 0, 0];
    const queue = [[...entrance, 0]];
    maze[entrance[0]][entrance[1]] = "+";

    while (queue.length) {
        let [old_x, old_y, depth] = queue.shift();
        // go to 4 sides to see if there has exit
        for (let i = 0; i < 4; i++) {
            let new_x = old_x + x_dir[i];
            let new_y = old_y + y_dir[i];
            // 新坐标合法且不为墙
            if (
                inBorder(new_x, new_y) &&
                maze[new_x][new_y] !== "+"
            ) {
                // 如果新坐标就在 exit 的位置，则直接返回
                if (
                    new_x === 0 ||
                    new_x === numRows - 1 ||
                    new_y === 0 ||
                    new_y === numCols - 1
                ) {
                    // console.log('target: ', new_x, new_y)
                    return depth + 1;
                } else {
                    // 否则将当前单元格改成 "+"，避免下次重复遍历
                    maze[new_x][new_y] = "+";
                    queue.push([new_x, new_y, depth + 1]);
                }
            } else {
                continue;
            }
        }
    }

    return -1;
};
