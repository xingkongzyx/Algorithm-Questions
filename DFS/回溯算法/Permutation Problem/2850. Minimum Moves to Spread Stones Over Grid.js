/**
由于所有移走的石子个数等于所有移入的石子个数（即 0 的个数），我们可以把移走的石子的坐标记录到列表 from 中（可能有重复的坐标），移入的石子的坐标记录到列表 to 中。这两个列表的长度一定是一样的(根据题目得出)。

枚举 from 的所有排列(全排列问题)，用其中的每个排列方式与 to 匹配（即累加当前排列方式中从 permutationFrom[i] 到 to[i] 的曼哈顿距离）

所有累计方式中的最小值就是答案。

? 链接：https://leetcode.cn/problems/minimum-moves-to-spread-stones-over-grid/solutions/2435313/tong-yong-zuo-fa-zui-xiao-fei-yong-zui-d-iuw8/

 */
var minimumMoves = function (grid) {
    const fromArr = [];
    const toArr = [];

    const numRows = grid.length;
    const numCols = grid[0].length;

    for (let i = 0; i < numRows; i++) {
        for (let j = 0; j < numCols; j++) {
            let count = grid[i][j];
            if (count === 0) {
                toArr.push([i, j]);
            } else if (count > 1) {
                while (count > 1) {
                    fromArr.push([i, j]);
                    count--;
                }
            }
        }
    }

    // 枚举 from 数组的全排列并储存在 total 中
    const cur = [];
    const total = [];
    let used = new Array(fromArr.length).fill(false);
    function permutation() {
        if (cur.length === fromArr.length) {
            total.push(cur.slice());
            return;
        }

        for (let i = 0; i < fromArr.length; i++) {
            if (used[i] === false) {
                used[i] = true;
                cur.push(fromArr[i]);
                permutation();
                cur.pop();
                used[i] = false;
            }
        }
    }
    permutation();

    // 累计计算每种排列方式的距离
    let minMove = Infinity;

    for (let i = 0; i < total.length; i++) {
        let curFromPath = total[i];

        let curMove = 0;
        for (let j = 0; j < curFromPath.length; j++) {
            curMove +=
                Math.abs(curFromPath[j][0] - toArr[j][0]) +
                Math.abs(curFromPath[j][1] - toArr[j][1]);
        }

        minMove = Math.min(minMove, curMove);
    }

    return minMove;
};

minimumMoves([
    [1, 3, 0],
    [1, 0, 0],
    [1, 0, 3],
]);
// minimumMoves([
//     [1, 1, 0],
//     [1, 1, 1],
//     [1, 2, 1],
// ]);
