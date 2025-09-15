/* 
* 我们对整棵二叉树进行一次遍历。设根节点的值为「rootVal」，我们只需要通过遍历，在左右子树中找出严格大于「rootVal」的「最小节点的值」，即为「所有节点中的第二小的值」。
! 解题的关键点在于 root value 就是当前 tree 最小的值。
//? 前序遍历解法: 1. https://leetcode.cn/problems/second-minimum-node-in-a-binary-tree/solution/gong-shui-san-xie-yi-ti-shuang-jie-shu-d-eupu/ 
? 2. 官方解法
/时间复杂度：O(n)，其中 n 是二叉树中的节点个数。我们最多需要对整棵二叉树进行一次遍历。
/空间复杂度：O(n)。我们使用深度优先搜索的方法进行遍历，需要使用的栈空间为 O(n)。

*/

var findSecondMinimumValue = function (root) {
    let ans = -1;
    /// 递归函数的含义是: 从 root 为根的二叉树进行搜索，找到值比「初始根节点 rootVal」大的最小数，使用全局变量 ans 存储答案。
    function dfs(node, rootVal) {
        //* 终止条件1: 遇到空节点
        if (node === null) return;

        //# 中
        //* 如果遇到了一个数字比 rootVal 大, 如果此时 ans 还为 -1, 说明这是第一次遇到比 rootVal 大的值, 直接更新 ans. 否则与 ans 已有的值进行比较选取较小的(因为求的就是第二小的值)
        if (node.val > rootVal) {
            if (ans === -1) ans = node.val;
            else ans = Math.min(ans, node.val);
        }

        //# 左
        dfs(node.left, rootVal);
        //# 右
        dfs(node.right, rootVal);
    }

    dfs(root, root.val);
    return ans;
};

/* 
* 上面的写法是对的（能过题），但利用这道题的特殊性质可以再快不少：
*     在这棵“特殊二叉树”里：每个非叶子结点有两个孩子，且 node.val = min(node.left.val, node.right.val)
*     因此：任何结点的孩子值都 ≥ 该结点的值。
* 
* 据此可以做两类剪枝：
* 1. 遇到比根值大的结点就不必再往下搜
* 如果 node.val > rootVal，它已经是一个“候选第二小”，而且它的孩子都 ≥ node.val，不可能更小，直接返回，不再下潜。
* 2. 全局已找到更好的答案时，剪掉更差的分支
* 若当前已有 ans，且 node.val >= ans，这条分支的所有值都 ≥ node.val ≥ ans，不可能改进答案，直接返回。
*/
var findSecondMinimumValueOptimize = function (root) {
    const rootVal = root.val;
    let ans = -1;

    function dfs(node) {
        if (!node) return;

        // 剪枝2：这条分支的最小值都不会小于当前 ans
        if (ans !== -1 && node.val >= ans) return;

        if (node.val > rootVal) {
            // 找到一个候选；无需再探孩子（剪枝1）
            ans = ans === -1 ? node.val : Math.min(ans, node.val);
            return;
        }

        // 只在 node.val === rootVal 时继续向下
        dfs(node.left);
        dfs(node.right);
    }

    dfs(root);
    return ans;
};
