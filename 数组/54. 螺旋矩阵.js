// https://mp.weixin.qq.com/s/ywI7Ca9gq99FWyZ4UFUhxA
//www.chengxuchu.com/#/%E7%AE%97%E6%B3%95%E5%9F%BA%E5%9C%B0/%E6%95%B0%E7%BB%84%E7%AF%87/leetcode59%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B52
/* var spiralOrder = (matrix) => {
    let result = [];
    let totalElements = matrix.length * matrix[0].length;
    let count = 0;
    let leftBorder = 0,
        topBorder = 0;
    let rightBorder = matrix[0].length - 1,
        bottomBorder = matrix.length - 1;
    // 循环之中的 if (count == totalElements) break 判断很重要。没有它的话遇见[1,2,3,4] 会输出结果[1, 2, 3, 4 3, 2, 1] 因为在做第三个for-loop right->left时此时 bottomBorder仍处在index 0,仍能够继续遍历，只不过topBorder此时已经在index 1出了边界其实不应该再遍历了。我们用这个if语句进行检查
    while (count < totalElements) {
        for (let i = leftBorder; i <= rightBorder; i++) {
            result.push(matrix[topBorder][i]);
            count++;
        }
        if (count == totalElements) break;
        topBorder++;
        for (let j = topBorder; j <= bottomBorder; j++) {
            result.push(matrix[j][rightBorder]);
            count++;
        }
        if (count == totalElements) break;
        rightBorder--;
        for (let i = rightBorder; i >= leftBorder; i--) {
            result.push(matrix[bottomBorder][i]);
            count++;
        }
        if (count == totalElements) break;
        bottomBorder--;
        for (let j = bottomBorder; j >= topBorder; j--) {
            result.push(matrix[j][leftBorder]);
            count++;
        }
        if (count == totalElements) break;
        leftBorder++;
    }
    console.log(result);
    return result;
}; */

var spiralOrder = function (matrix) {
    //! 记住一点，对于二维数组它的行是由 top-bottom 进行遍历的，它的列是由 left-right进行遍历的 所以我们访问matrix某个特定元素是通过matrix[top/bottom][left/right]
    let top = 0,
        left = 0;
    let bottom = matrix.length - 1,
        right = matrix[0].length - 1;
    let res = [];
    while (true) {
        for (let i = left; i <= right; i++) {
            res.push(matrix[top][i]);
        }
        top++;
        if (top > bottom) break;

        for (let i = top; i <= bottom; i++) {
            res.push(matrix[i][right]);
        }
        right--;
        if (left > right) break;
        for (let i = right; i >= left; i--) {
            res.push(matrix[bottom][i]);
        }
        bottom--;
        if (top > bottom) break;

        for (let i = bottom; i >= top; i--) {
            res.push(matrix[i][left]);
        }
        left++;
        if (left > right) break;
    }
    return res;
};

spiralOrder([[1, 2, 3, 4]]);
