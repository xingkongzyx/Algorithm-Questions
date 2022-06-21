/* 
* dp[i][j]：长度为i，末尾项为 nums[i-1] 的子数组，与长度为j，末尾项为 nums[j-1] 的子数组，二者的最大公共后缀子数组长度。

* 1) 若当前两个元素值不同，即 nums1[i-1] != nums2[j-1]，因为以 nums1[i-1] 和 nums2[j-1] 结尾的公共子数组不存在，因为它们的末元素不等
# 因为公共子数组必须是连续的，而此时的元素值不同，相当于直接断开了，此时状态转移方程：dp[i][j] = 0。
* 2) 若当前两个元素值相同，即 nums1[i-1] == nums2[j-1]，以它们俩为结尾的最长公共子数组的长度就是以 nums1[i-2] 和 nums2[j-2] 结尾的最长公共子数组的长度加1，此时状态转移方程：dp[i][j] = dp[i - 1][j - 1] + 1。之所以这样定义状态是因为原问题所要求的最长公共子数组如果存在，它一定是以某一个A的元素结尾，也以某一个B的元素结尾，现在就是遍历所有可能的分别以哪两个元素结尾的情况，取其中的最长的情况即可
/ 链接：https://leetcode.cn/problems/maximum-length-of-repeated-subarray/solution/zui-chang-gong-gong-zi-shu-zu-wen-ti-jing-dian-dpt/


? 与 1143 LCS 不同的是，这题dp数组需要记录的是「结尾」构成公共数组的长度，LCS 需要的是 nums1[0,i-1] 和 nums2[0,j-1] 「区间内」公共数组的长度

/ 链接：https://leetcode.cn/problems/maximum-length-of-repeated-subarray/solution/by-dodo_1202-exk2/

? 本题与公共子序列不同，子序列不一定都是连续的，只要前面有相同的子序列，哪怕当前比较的字符不一样，那么当前字符串之前的子序列也不会为 0。
? 而子串(子数组)是连续的，若当前比较的字符不相同，则当前位置的最长公共子数组(子串)的长度为 0，即 dp[i][j] = 0(就是没有)。
*/

var findLength = function (nums1, nums2) {
    let dp = new Array(nums1.length + 1);
    for (let i = 0; i < nums1.length + 1; i++) {
        dp[i] = new Array(nums2.length + 1).fill(0);
    }
    let maxLen = 0;
    for (let row = 1; row <= nums1.length; row++) {
        for (let col = 1; col <= nums2.length; col++) {
            if (nums1[row - 1] === nums2[col - 1]) {
                dp[row][col] = dp[row - 1][col - 1] + 1;
                maxLen = Math.max(maxLen, dp[row][col]);
            } else {
                dp[row][col] = 0;
            }
        }
    }
    console.log(dp);
    return maxLen;
};
const nums1 = [1, 2, 3],
    nums2 = [3, 2, 1];
findLength(nums1, nums2);
