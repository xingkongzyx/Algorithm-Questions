/*
 * dp[3]，就是 元素1为头结点搜索树的数量 + 元素2为头结点搜索树的数量 + 元素3为头结点搜索树的数量
 *   1. 元素1为头结点搜索树的数量 = 右子树有2个元素的搜索树数量 * 左子树有0个元素的搜索树数量
 *   2. 元素2为头结点搜索树的数量 = 右子树有1个元素的搜索树数量 * 左子树有1个元素的搜索树数量
 *   3. 元素3为头结点搜索树的数量 = 右子树有0个元素的搜索树数量 * 左子树有2个元素的搜索树数量
 >  时间复杂度：O(n^2)  空间复杂度：O(n)
 */

var numTrees = function (n) {
    let dp = new Array(n + 1).fill(0);
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;

    for (let numOfNodes = 3; numOfNodes <= n; numOfNodes++) {
        //# dp[numOfNodes] += dp[以 root 为头结点左子树节点数量] * dp[以 root 为头结点右子树节点数量]
        for (let root = 1; root <= numOfNodes; root++) {
            dp[numOfNodes] += dp[root - 1] * dp[numOfNodes - root];
        }
    }
    // console.log(dp);
    return dp[n];
};
numTrees(3);
