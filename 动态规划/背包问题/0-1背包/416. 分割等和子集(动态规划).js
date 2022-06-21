/* 
/ 重要的四点
/ 背包的体积为sum / 2
/ 背包要放入的商品（集合里的元素）重量为 元素的数值，价值也为元素的数值
/ 背包如果正好装满，说明找到了总和为 sum / 2 的子集。
/ 背包中每一个元素是不可重复放入。
/ 那么对于这个问题，我们可以先对集合求和，得出 sum，把问题转化为背包问题：给一个可装载重量为 sum / 2 的背包和 nums.length 个物品，每个物品的重量为 nums[i], 价值为nums[i]。现在让你装物品，是否存在一种装法，能够恰好将背包装满？

* 1. 确定dp数组以及下标的含义
* dp[j]表示 背包总容量是j，最大可以凑成j的子集总和为dp[j]。
* 
* 2. 确定递推公式
* 本题，相当于背包里放入数值，那么物品i的重量是nums[i]，其价值也是nums[i]。
* 所以递推公式：dp[j] = max(dp[j], dp[j - nums[i]] + nums[i]);
* 
* 3. dp数组如何初始化
* 因为题目给的价值都是正整数，那么非0下标都初始化为0就可以了，如果题目给的价值有负数，那么非0下标就要初始化为负无穷。
* 
* 4. 确定遍历顺序
* 如果使用一维dp数组，物品遍历的for循环放在外层，遍历背包的for循环放在内层，且内层for循环倒序遍历！
*/

var canPartition = function (nums) {
    let sum = 0;
    for (let num of nums) sum += num;

    /// 如果sum为奇数，肯定找不到，因为sum/2为小数，而数组只包含正整数。
    if (sum % 2 === 1) return false;

    let bagWeight = sum / 2;
    let dp = new Array(bagWeight + 1).fill(0);

    for (let itemIdx = 0; itemIdx < nums.length; itemIdx++) {
        for (
            let capacity = bagWeight;
            capacity >= nums[itemIdx];
            capacity--
        ) {
            dp[capacity] = Math.max(
                dp[capacity],
                dp[capacity - nums[itemIdx]] + nums[itemIdx]
            );
        }
    }
    // console.log(dp);
    return dp[bagWeight] === bagWeight;
};
console.log(canPartition([1, 2, 3, 5]));
