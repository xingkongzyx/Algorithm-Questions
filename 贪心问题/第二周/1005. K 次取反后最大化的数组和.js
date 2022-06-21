/* 
第一步：将数组按照绝对值大小从大到小排序，注意要按照绝对值的大小
第二步：从前向后遍历，遇到负数将其变为正数，同时K--
第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
第四步：求和

*/

var largestSumAfterKNegations = function (nums, k) {
    nums.sort((a, b) => Math.abs(b) - Math.abs(a));

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] < 0 && k > 0) {
            nums[i] *= -1;
            k--;
        }
    }
    console.log(nums, k);
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
