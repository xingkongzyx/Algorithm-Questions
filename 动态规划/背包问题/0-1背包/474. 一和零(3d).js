/* 
https://leetcode.cn/problems/ones-and-zeroes/solution/dong-tai-gui-hua-zhuan-huan-wei-0-1-bei-bao-wen-ti/
/ 把要求的0的数量和1的数量(m和n)视作背包的容量(与其他问题不同的是这里的背包容量有两个维度)。然后 strs中的每个元素都视为物品，它的容量也有两个维度(0的个数和1的个数)。这里dp目标值就是对于满足背包两个维度容量的字符串的数目有多少

/ dp[i][j][k]: 从strs数组 [0:i] 中选择, 能够满足j个0, k个1的字符串的最大数量。

/ 递推公式:
/    从strs[i]中获取 numOfZeros 和 numOfOnes
/    1. 选择 strs[i]: dp[i][j][k] = dp[i-1][j-numOfZeros][k-numOfOnes] + 1
/    2. 不选择当前考虑的字符串 strs[i]: dp[i][j][k] = dp[i-1][j][k]
/    然后计算它们间的最大值

/ 初始化:
/ 由于在递推公式中会用到 dp[i-1][*][*] 中的元素, 所以需要将三维数组中的 dp[0][*][*] 这一行初始化. 计算出nums[0]中有多少个0和1, 然后dp[0][0的个数][1的个数] 及其之后的dp数组中的位置初始化为1. 因为这些位置都能满足 numOfZerosInFirstStrEle, numOfOnesInFirstStrEle的要求
*/

var findMaxForm = function (strs, m, n) {
    let dp = new Array(strs.length);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(m + 1);
        for (let j = 0; j <= m; j++) {
            dp[i][j] = new Array(n + 1).fill(0);
        }
    }
    // 初始化:
    let numOfZerosInFirstStrEle = getNumOfElements("0", strs[0]);
    let numOfOnesInFirstStrEle = getNumOfElements("1", strs[0]);
    for (let j = 0; j <= m; j++) {
        for (let k = 0; k <= n; k++) {
            if (
                j >= numOfZerosInFirstStrEle &&
                k >= numOfOnesInFirstStrEle
            )
                dp[0][j][k] = 1;
        }
    }

    for (let i = 1; i < dp.length; i++) {
        let numOfZeros = getNumOfElements("0", strs[i]);
        let numOfOnes = getNumOfElements("1", strs[i]);
        for (let j = 0; j <= m; j++) {
            for (let k = 0; k <= n; k++) {
                if (j >= numOfZeros && k >= numOfOnes) {
                    dp[i][j][k] = Math.max(
                        dp[i - 1][j][k],
                        dp[i - 1][j - numOfZeros][k - numOfOnes] + 1
                    );
                } else {
                    dp[i][j][k] = dp[i - 1][j][k];
                }
            }
        }
    }

    // console.log(dp);
    return dp[strs.length - 1][m][n];
};

var getNumOfElements = function (ele, str) {
    let res = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] === ele) res += 1;
    }
    return res;
};

const strs = ["10", "0001", "111001", "1", "0"],
    m = 5,
    n = 3;
findMaxForm(strs, m, n);
