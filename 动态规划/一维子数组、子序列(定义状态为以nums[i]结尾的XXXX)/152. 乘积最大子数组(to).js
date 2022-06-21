/*
! 常见误区: 数组的动态规划问题、子序列、连续子序列的一个常见的状态定义是：dp[i]是以下标 i 结尾的连续子序列的乘积的最大值。最后把整个 dp 数组看一遍求最大值即可。因此状态转移方程可能是：
! dp[i] = max(dp[i - 1] * nums[i], nums[i])

? 链接：https://leetcode.cn/problems/maximum-product-subarray/solution/dong-tai-gui-hua-li-jie-wu-hou-xiao-xing-by-liweiw/

! 但是如果我们把 dp[i−1] 直接拿过来相乘，不一定是最优解.
!   1)如果 nums[i] 项是负数，按前面定义 dp[i−1] 是以 nums[i-1] 结尾的连续子序列的乘积的最大值，得到 dp[i] 会是最小的。此时马后炮来说，dp[i-1]的存储的应是最小积，这样 (负数*最小的积) 得到结果比 (负数*最大的积) 大

!   2)如果 nums[i] 项是正数，把前面的以 nums[i-1] 结尾的连续子序列的乘积的最大值dp[i-1]直接拿来乘，没问题
! 即，对 i 来说，i−1 的最优解可能是最大积，也可能是最小乘积
! 因此，dp[i] 要放两项了，一项是局部最大积，一项是局部最小积


 * dp[i][0] 表示：以 nums[i] 结尾的连续子序列的乘积的最小值。
 * dp[i][1] 表示：以 nums[i] 结尾的连续子序列的乘积的最大值；


 * 对于以 nums[i] 为末尾的子数组能产生的最小积，它有 3 种情况：
 *      不和别人乘，就 nums[i] 自己
 *      nums[i] 是负数，希望乘上前面的最大积
 *      nums[i] 是正数，希望乘上前面的最小积
 * 所以，dp[i][0] 取三种情况中的最小值
 * dp[i][0] = min(dp[i - 1][0] * nums[i],dp[i - 1][1] * nums[i], nums[i])
 * 
 * 类似的，dp[i][1]dp[i][1] 值取三种情况中的最大值
 * dp[i][1] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])

? 链接：https://leetcode.cn/problems/maximum-product-subarray/solution/wa-ni-zhe-ti-jie-shi-xie-gei-bu-hui-dai-ma-de-nu-p/

 
/ 定义子问题是人为定义的，只要你定义的子问题能够很容易找到子问题之间的联系，能解决这个问题就可以。不一定要和绝大多数人一样。

/「力扣」第 53 题、第 300 题最常见的解法都是规定了 nums[i] 必须被选取。

/ 下面回答一下：什么场景会定义「必须被选取」会简化状态转移逻辑？
/ 这个说一下直观的感受：有不确定的地方、需要分类讨论的地方。因为不确定，所以就需要找各个确定的部分，组成了整体不确定的结果，例如这个问题 num[i] 可以在「连续子数组」的任何一个位置，规定它必须在末尾，容易找到不同规模的子问题之间的联系（状态转移方程）。因为不确定正数还是负数，就规定正数的时候是什么什么情况，负数的时候是什么什么情况。

/ 定义的子问题足够小，足够合适，这些子问题之间的联系，解决了整体要解决的问题，这是绝大多数动态规划在做的事情。定义「足够小」其实也是把不确定的东西确定下来的一种方式。

 */

var maxProduct = function (nums) {
    let dp = new Array(nums.length);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(2).fill(0);
    }
    dp[0][0] = nums[0];
    dp[0][1] = nums[0];
    let res = dp[0][1];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > 0) {
            dp[i][0] = Math.min(nums[i], nums[i] * dp[i - 1][0]);
            dp[i][1] = Math.max(nums[i], nums[i] * dp[i - 1][1]);
        } else {
            dp[i][0] = Math.min(nums[i], nums[i] * dp[i - 1][1]);
            dp[i][1] = Math.max(nums[i], nums[i] * dp[i - 1][0]);
        }

        res = Math.max(res, dp[i][1]);
    }
    return res;
};
var maxProduct_lazy_version = function (nums) {
    let dp = new Array(nums.length);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(2).fill(0);
    }
    dp[0][0] = nums[0];
    dp[0][1] = nums[0];
    let res = dp[0][1];
    for (let i = 1; i < nums.length; i++) {
        // # 偷懒版，反正最大值最小值只会出现于下面的三种情况
        dp[i][0] = Math.min(
            nums[i],
            nums[i] * dp[i - 1][0],
            nums[i] * dp[i - 1][1]
        );
        dp[i][1] = Math.max(
            nums[i],
            nums[i] * dp[i - 1][1],
            nums[i] * dp[i - 1][0]
        );
        res = Math.max(res, dp[i][1]);
    }
    return res;
};
const nums = [2, 3, -2, 4];
console.log(maxProduct(nums));
