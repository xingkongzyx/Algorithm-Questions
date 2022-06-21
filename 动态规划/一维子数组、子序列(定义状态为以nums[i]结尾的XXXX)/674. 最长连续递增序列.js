/*
 * dp[i] 表示：以 nums[i] 结尾 的「连续递增的子数组」的长度。注意：这个定义中 nums[i] 必须被选取，且必须是这个子数组的最后一个元素；
 *
 * 与 300 的区别就在于，这道题求的是 subarray，而 subarray 是不能通过删减nums中的元素得到的，所以在dp中递推时，只用看 dp[i-1] 而不像 300 要看 dp[j]
 */
var findLengthOfLCIS = function (nums) {
    let dp = new Array(nums.length).fill(1);
    let result = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) dp[i] = dp[i - 1] + 1;
        result = Math.max(result, dp[i]);
    }
    // console.log(dp);
    return result;
};
findLengthOfLCIS([1, 3, 5, 4, 7]);
