/* 
* 第一步：将数组按照绝对值大小从大到小排序，注意要按照绝对值的大小
# 有「负数」的时候对应的贪心理论: 局部最优 - 让「绝对值大」的负数变为正数，当前数值达到最大。整体最优 - 整个数组和达到最大。
* 第二步：从前向后遍历，遇到负数将其变为正数，同时K--
* 第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
# 全是「正数」的时候对应的贪心理论: 此时nums是「有序正整数」序列。局部最优 - 只找「值最小的正整数」也就是 nums[-1] 进行反转，当前数值可以达到最大。整体最优 - 整个数组和达到最大。
* 第四步：求和
? https://programmercarl.com/1005.K%E6%AC%A1%E5%8F%96%E5%8F%8D%E5%90%8E%E6%9C%80%E5%A4%A7%E5%8C%96%E7%9A%84%E6%95%B0%E7%BB%84%E5%92%8C.html#%E6%80%9D%E8%B7%AF
*/

var largestSumAfterKNegations = function (nums, k) {
    nums.sort((a, b) => Math.abs(b) - Math.abs(a));

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] < 0 && k > 0) {
            nums[i] *= -1;
            k--;
        }
    }

    if (k !== 0 && k % 2 === 1) {
        nums[nums.length - 1] *= -1;
    }

    let sum = 0;
    for (let num of nums) sum += num;

    return sum;
};
let nums = [3, -1, 0, 2],
    k = 3;
console.log(largestSumAfterKNegations(nums, k));
