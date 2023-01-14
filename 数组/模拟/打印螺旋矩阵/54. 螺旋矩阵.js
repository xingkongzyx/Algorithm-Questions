//> 54, 59 在这里进行了写法统一, 不要参考代码随想录的解法
//? 这篇文章的动画讲解了这个方法 https://leetcode.cn/problems/spiral-matrix/solution/dong-hua-mo-ni-yi-xia-jiu-neng-gao-dong-i27qf/
//? 必看: 参考了剑指offer 29 的解法, 代码能够统一 https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/mian-shi-ti-29-shun-shi-zhen-da-yin-ju-zhen-she-di/
var spiralOrder = function (matrix) {
    //! 记住一点, 对于二维数组它的行是由 top-bottom 进行遍历的, 它的列是由 left-right进行遍历的 所以我们访问matrix某个特定元素是通过matrix[top/bottom][left/right]
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
