/* 
? https://leetcode.cn/problems/word-search/solution/shou-hua-tu-jie-79-dan-ci-sou-suo-dfs-si-lu-de-cha/
? 讲解很好: https://leetcode.cn/problems/word-search/solution/dan-ci-sou-suo-hui-su-suan-fa-jian-zhi-v-0vbd/
? k 神的链接: https://leetcode.cn/problems/ju-zhen-zhong-de-lu-jing-lcof/solution/mian-shi-ti-12-ju-zhen-zhong-de-lu-jing-shen-du-yo/
/ 时间复杂度与空间复杂度的讲解: https://leetcode.cn/problems/word-search/solution/tu-jie-di-gui-shen-du-you-xian-sou-suo-by-z1m/
/ 时间复杂度: O((M*N)²)
/ 空间复杂度: O(M*N)
*/
var exist = function (board, word) {
    let numRows = board.length;
    let numCols = board[0].length;
    let visited = new Array(numRows);
    for (let i = 0; i < numRows; i++) {
        visited[i] = new Array(numCols).fill(false);
    }
    let directions = [
        [-1, 0],
        [1, 0],
        [0, 1],
        [0, -1],
    ];
    
    function backtracking(rowIdx, colIdx, wordIdx) {
        //* 如果 wordIdx 指针越界了, 则证明已经找到与 word 匹配的所有字符了
        if (wordIdx === word.length) {
            return true;
        }
        /*
         * 哪些情况说明这是一个错的点：
         * ➀ 当前的点, 越出矩阵边界。
         * ➁ 当前的点, 之前访问过, 不满足「同一个单元格内的字母不允许被重复使用」。
         * ➂ 当前的点, 不是目标点, 比如你想找 E, 却来到了 D
         */
        if (
            inBound(rowIdx, colIdx) === false ||
            visited[rowIdx][colIdx] === true ||
            board[rowIdx][colIdx] !== word[wordIdx]
        ) {
            return false;
        }
        //# 单层递归逻辑: 当通过 <终止条件> 剪枝后, 说明当前 board[rowIdx][colIdx] 没有使用过并且与比较的 word 中的字符匹配, 则将当前字符的状态设置为已使用 true, 然后继续对 board[rowIdx][colIdx] 的 上、下、左、右 位置上的字符与 word 字符串上的下一字符继续进行匹配。
        //* 将 visited 数组的对应位置设为 true 避免该位置被重复使用
        visited[rowIdx][colIdx] = true;
        //* 如果从当前点 (rowIdx, colIdx) 散发的四个方向中有一个方向能成功匹配剩下的字母, 则可以返回 true
        for (let i = 0; i < 4; i++) {
            let [x_offset, y_offset] = directions[i];
            rowIdx += x_offset;
            colIdx += y_offset;
            let tempRes = backtracking(rowIdx, colIdx, wordIdx + 1);
            //* 更加明显的回溯操作
            rowIdx -= x_offset;
            colIdx -= y_offset;
            if (tempRes) return true;
        }

        //* 对于这个分支的 DFS 已经完成了, 需要回溯还原现场. 将当前访问标记设置为 false, 为了能够当当前这一趟递归不能够找到结果的时候, 在后续遍历过程中还能够访问该方格。
        visited[rowIdx][colIdx] = false;

        //* 前面如果没有找到完整匹配的结果则返回false
        return false;
    }

    function inBound(rowIdx, colIdx) {
        return (
            rowIdx >= 0 &&
            rowIdx < numRows &&
            colIdx >= 0 &&
            colIdx < numCols
        );
    }

    for (let i = 0; i < numRows; i++) {
        for (let j = 0; j < numCols; j++) {
            if (board[i][j] === word[0]) {
                let checkRes = backtracking(i, j, 0);

                if (checkRes) return true;
            }
        }
    }
    return false;
};

exist(
    [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ],
    "SEE"
);
