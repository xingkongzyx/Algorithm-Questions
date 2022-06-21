var rob = function (nums) {
    if (nums.length == 0) return 0;
    if (nums.length == 1) return nums[0];

    // 1) 不考虑尾元素
    let dp = new Array(nums.length);
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0], nums[1]);

    for (let i = 2; i < nums.length - 1; i++) {
        dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
    }
    let res1 = dp[nums.length - 2];
    // 2) 不考虑首元素
    dp[0] = 0;
    dp[1] = nums[1];
    for (let i = 2; i < nums.length; i++) {
        dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
    }
    let res = Math.max(res1, dp[nums.length - 1]);
    return res;
};
