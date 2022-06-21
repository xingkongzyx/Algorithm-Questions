/*
 * 局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。
 *
 * 全局最优：选取最大“连续和”
 *
 * 从代码角度上来讲：遍历nums，从头开始用count累积，如果count一旦加上nums[i]变为负数，那么就应该从nums[i+1]开始从0累积count了，因为已经变为负数的count，只会拖累总和。
 *
 > 时间复杂度：O(n)
 > 空间复杂度：O(1)
 */

var maxSubArray = function (nums) {
    let result = nums[0];
    let count = 0;
    let startIdx = 0;
    while (startIdx < nums.length) {
        count += nums[startIdx];

        //# 取区间累计的最大值（相当于不断确定最大子序终止位置）
        result = Math.max(result, count);

        //# 相当于重置最大子序起始位置，因为遇到负数一定是拉低总和
        if (count < 0) count = 0;

        startIdx++;
    }
    return result;
};

let nums = [-2];
console.log(maxSubArray(nums));
