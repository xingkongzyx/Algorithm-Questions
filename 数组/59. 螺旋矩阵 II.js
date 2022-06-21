// 解法1参考: https://leetcode-cn.com/problems/spiral-matrix-ii/solution/spiral-matrix-ii-mo-ni-fa-she-ding-bian-jie-qing-x/

var generateMatrix = function (n) {
    let leftBorder = 0,
        topBorder = 0;
    let rightBorder = n - 1,
        bottomBorder = n - 1;
    let filledNumber = 1;
    let result = new Array(n)
        .fill()
        .map((ele) => new Array(n).fill(0));

    let count = 0;
    while (count < n * n) {
        // 首先填充方向为 leftBorder->rightBorder
        for (let i = leftBorder; i <= rightBorder; i++) {
            // 我们的 filledNumber 就是用于填充结果数组的，与题目要求一样从1开始
            // 每次填充完成更新 filledNumber
            result[topBorder][i] = filledNumber;
            filledNumber++;
            count++;
        }
        topBorder++;
        // 其次填充方向为 topBorder->bottomBorder
        for (let i = topBorder; i <= bottomBorder; i++) {
            result[i][rightBorder] = filledNumber;
            filledNumber++;
            count++;
        }
        rightBorder--;
        // 再其次填充方向为 rightBorder->leftBorder
        for (let j = rightBorder; j >= leftBorder; j--) {
            result[bottomBorder][j] = filledNumber;
            filledNumber++;
            count++;
        }
        bottomBorder--;
        // 再其次填充方向为 bottomBorder->topBorder
        for (let j = bottomBorder; j >= topBorder; j--) {
            result[j][leftBorder] = filledNumber;
            filledNumber++;
            count++;
        }
        leftBorder++;
    }
    // console.log(result);
    return result;
};

var generateMatrix_soltion2 = function (n) {
    let startX = (startY = 0); // 起始位置
    let loop = Math.floor(n / 2); // 每个圈循环几次，例如n为奇数3，那么loop = 1 只是循环一圈，矩阵中间的值需要单独处理
    let mid = Math.floor(n / 2); // 矩阵中间的位置，例如：n为3， 中间的位置就是(1，1)，n为5，中间位置为(2, 2)
    let offset = 1; // 每一圈循环，需要控制每一条边遍历的长度
    let count = 1; // 用来给矩阵中每一个空格赋值
    let res = new Array(n).fill(0).map(() => new Array(n).fill(0));

    while (loop--) {
        let row = startX,
            col = startY;
        // 上行从左到右（左闭右开）
        for (; col < startY + n - offset; col++) {
            res[row][col] = count++;
        }
        // 右列从上到下（左闭右开）
        for (; row < startX + n - offset; row++) {
            res[row][col] = count++;
        }
        // 下行从右到左（左闭右开）
        for (; col > startX; col--) {
            res[row][col] = count++;
        }
        // 左列做下到上（左闭右开）
        for (; row > startY; row--) {
            res[row][col] = count++;
        }

        // 更新起始位置
        startX++;
        startY++;

        // 更新offset
        offset += 2;
    }
    // 如果n为奇数的话，需要单独给矩阵最中间的位置赋值
    if (n % 2 === 1) {
        res[mid][mid] = count;
    }
    return res;
};

generateMatrix(1);
