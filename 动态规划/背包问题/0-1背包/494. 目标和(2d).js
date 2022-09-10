// ? https://leetcode.cn/problems/target-sum/solution/hen-xiang-xi-de-zhuan-hua-wei-0-1bei-bao-irvy/
var findTargetSumWays = function (nums, target) {
    //# 为了避免 nums = [100]，target = -200的情况。这种情况开拓数组传入负数会报错。所以把target的值替换为它的绝对值就可以了，原因是这个数组如果可以用加法凑出某个正数，那么也一定能用减法凑出它的相反数。
    target = Math.abs(target);

    let totalSum = 0;
    for (let i = 0; i < nums.length; i++) {
        totalSum += nums[i];
    }
    //> nums 中所有元素都是非负整数 >= 0, 所以这里不用比较绝对值
    if (target > totalSum) return 0;

    if ((totalSum + target) % 2 !== 0) return 0;

    let bagWeight = (target + totalSum) / 2;
    //# 构建dp数组: 使用 下标为[0, i]的nums[i]能够填满j（包括j）这么大容量的包，有dp[i][j]种方法。
    let dp = new Array(nums.length);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(bagWeight + 1).fill(0);
    }

    //! 初始化注意，对于第一列也就是装满容量为0的背包可能有nums[i]为0的情况，这种情况无法在最开始初始化，只能在后序遍历时计算

    //# 所以我们能够进行的初始化只有第一行: 对于dp[0][0] 就是从下标为0的元素进行选择满足容量为0的背包，一共有dp[0][0]种方式。如果nums[0]=0，则容量为0的背包来说，要么选择nums[0]，要么不选择nums[0]，所以一共两者情况 dp[0][0] = 2. 对于其他dp[0][j]，nums[0]=0 无法装入j
    //# 如果不是nums[0]=0，则对于第一行容量正好为nums[0]的背包装满它只有一种方式就是只放nums[0], 但dp[0][0]要初始化为1，因为不选择nums[0]也是一种方式
    if (nums[0] == 0) {
        dp[0][0] = 2;
    } else if (nums[0] <= bagWeight) {
        dp[0][0] = 1;
        dp[0][nums[0]] = 1;
    }

    /* 
*   对于第i个数字，我们有两种选择：
*   1.选择使用第i个数字凑成此时的capacity，此时背包的容量需要减去nums[i]。递推式为 dp[i - 1][capacity - nums[i]]；
*   2.选择放弃第i个数字，只使用下标为[0, i-1]的数字，背包的容量不变。递推式为 dp[i - 1][j]；
*   3.当背包的容量小于第i个数字时，即capacity < nums[i]，无法将第i个数字放入背包，只能跳过，递推式同2。
   
?   链接：https://leetcode.cn/problems/target-sum/solution/hen-xiang-xi-de-zhuan-hua-wei-0-1bei-bao-irvy/
*/

    for (let i = 1; i < nums.length; i++) {
        //! 背包应该从容量为0开始！！这是因为，题目中指出了 nums[i] >=0，也就是nums[i]可能为0，因此需要考虑到背包容量也为0的情况
        for (let capacity = 0; capacity <= bagWeight; capacity++) {
            if (capacity < nums[i])
                dp[i][capacity] = dp[i - 1][capacity];
            else
                dp[i][capacity] =
                    dp[i - 1][capacity] +
                    dp[i - 1][capacity - nums[i]];
        }
    }
    return dp[nums.length - 1][bagWeight];
};

let nums = [1, 1, 1, 1, 1];
target = 3;
res = findTargetSumWays(nums, target);
console.log(res);
