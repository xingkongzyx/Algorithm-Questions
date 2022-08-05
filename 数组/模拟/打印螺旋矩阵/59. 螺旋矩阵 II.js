//? 解法参考: https://leetcode-cn.com/problems/spiral-matrix-ii/solution/spiral-matrix-ii-mo-ni-fa-she-ding-bian-jie-qing-x/

//? 与 54 进行写法的统一, https://leetcode.cn/problems/spiral-matrix-ii/solution/spiral-matrix-ii-mo-ni-fa-she-ding-bian-jie-qing-x/1620630
var generateMatrix = function (n) {
    let leftBorder = 0,
        topBorder = 0;
    let rightBorder = n - 1,
        bottomBorder = n - 1;
    let filledNumber = 1;
    let result = new Array(n)
        .fill()
        .map((ele) => new Array(n).fill(0));

    while (true) {
        //* 首先填充方向为 leftBorder->rightBorder
        for (let i = leftBorder; i <= rightBorder; i++) {
            //* 我们的 filledNumber 就是用于填充结果数组的，与题目要求一样从1开始
            //* 每次填充完成更新 filledNumber
            result[topBorder][i] = filledNumber;
            filledNumber++;
        }
        topBorder++;
        if (topBorder > bottomBorder) break;
        //* 其次填充方向为 topBorder->bottomBorder
        for (let i = topBorder; i <= bottomBorder; i++) {
            result[i][rightBorder] = filledNumber;
            filledNumber++;
        }
        rightBorder--;
        if (leftBorder > rightBorder) break;
        //* 再其次填充方向为 rightBorder->leftBorder
        for (let j = rightBorder; j >= leftBorder; j--) {
            result[bottomBorder][j] = filledNumber;
            filledNumber++;
        }
        bottomBorder--;
        if (topBorder > bottomBorder) break;
        //* 再其次填充方向为 bottomBorder->topBorder
        for (let j = bottomBorder; j >= topBorder; j--) {
            result[j][leftBorder] = filledNumber;
            filledNumber++;
        }
        leftBorder++;
        if (leftBorder > rightBorder) break;
    }
    // console.log(result);
    return result;
};

generateMatrix(1);
