var canPartition = function (nums) {
    let sum = 0;
    for (let num of nums) sum += num;
    if (sum % 2 === 1) return false;

    let bagWeight = sum / 2;
    let dp = new Array(nums.length);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(bagWeight + 1).fill(0);
    }
    for (let itemIdx = 0; itemIdx < nums.length; itemIdx++) {
        dp[itemIdx][0] = 0;
    }
    for (let capacity = 0; capacity <= bagWeight; capacity++) {
        if (capacity >= nums[0]) dp[0][capacity] = nums[0];
    }
    for (let itemIdx = 1; itemIdx < nums.length; itemIdx++) {
        for (let capacity = 1; capacity <= bagWeight; capacity++) {
            //# 容量有限，无法选择第i个数字nums[itemIdx]
            if (nums[itemIdx] > capacity)
                dp[itemIdx][capacity] = dp[itemIdx - 1][capacity];
            else
                dp[itemIdx][capacity] = Math.max(
                    dp[itemIdx - 1][capacity],
                    dp[itemIdx - 1][capacity - nums[itemIdx]] +
                        nums[itemIdx]
                );
        }
    }
    console.log(dp);
    return dp[nums.length - 1][bagWeight] === bagWeight;
};
canPartition([1, 5, 11, 5]);
