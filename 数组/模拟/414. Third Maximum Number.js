/* 
* 遍历数组, 对于数组中的元素 num:
* 若 num>a, 我们将 c 替换为 b, b 替换为 a, a 替换为 num, 这模拟了将 num 插入有序集合, 并删除有序集合中的最小值的过程; 
* 若 a>num>b, 类似地, 我们将 c 替换为 b, b 替换为 num, a 保持不变；
* 若 b>num>c, 类似地, 我们将 c 替换为 num, a 和 b 保持不变；
* 其余情况不做处理。
! 注意上述替换过程中的顺序, 否则会出现失去某些值的错误情况

? https://leetcode.cn/problems/third-maximum-number/solutions/1032401/di-san-da-de-shu-by-leetcode-solution-h3sp/?orderBy=most_votes
*/
var thirdMax = function (nums) {
    let a = -Infinity;
    let b = -Infinity;
    let c = -Infinity;

    for (let num of nums) {
        if (num > a) {
            c = b;
            b = a;
            a = num;
        } else if (num < a && num > b) {
            c = b;
            b = num;
        } else if (num < b && num > c) {
            c = num;
        }
    }

    if (c == -Infinity) return a;
    return c;
};
