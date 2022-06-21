/* 
* 1. 先确定右边评分大于左边的情况（也就是从前向后遍历）
* 局部最优：只要右边评分比左边大，右边的孩子就多一个糖果，
* 全局最优：相邻的孩子中，评分高的右孩子获得比左边孩子更多的糖果

* 2. 再确定左孩子大于右孩子的情况（从后向前遍历）
* 局部最优：只要左边评分比右边大，要确保左边孩子的糖果就比右边的孩子多一个，同时还要确保满足右边评分大于左边的情况. 所以取 result[i + 1] + 1 和 result[i] 最大的糖果数量，保证第i个小孩的糖果数量即大于左边的也大于右边的。
* 全局最优：相邻的孩子中，评分高的孩子获得更多的糖果。
*/

var candy = function (ratings) {
    let numOfStudents = ratings.length;
    let result = new Array(numOfStudents).fill(1);

    for (let i = 1; i < numOfStudents; i++) {
        if (ratings[i] > ratings[i - 1])
            result[i] = Math.max(result[i - 1] + 1, result[i]);
    }
    let total = result[numOfStudents - 1];
    for (let j = numOfStudents - 2; j >= 0; j--) {
        if (ratings[j] > ratings[j + 1])
            result[j] = Math.max(result[j + 1] + 1, result[j]);
        total += result[j];
    }

    return total;
};

let res = candy([1, 0, 2]);
console.log(res);
