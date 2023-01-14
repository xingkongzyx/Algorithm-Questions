/* 
> 后序遍历
* 这道题解决之前的前置问题是：如何求出一个二叉树的高度: https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/。当我们可以把上面那道题AC掉之后 我们就可以继续解决问题了

! 高度平衡二叉树, 题目给的定义是：一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。


# 递归函数逻辑: 判断以当前节点为根节点的子树是否满足平衡的条件, 如果满足则是返回最大高度, 不满足平衡条件的时候则返回 -1。
# 递归终止条件是: 当当前节点是 None, 返回高度 0.
# 递归单层逻辑: 分别检查左右子树是否满足平衡的条件, 如果其中任意一边不满足则直接返回 -1. 都满足的话再检查以当前节点为根节点的子树是否满足左右平衡, 满足的话则返回最大高度.  


/ 时间复杂度：O(n)，其中 nn 是二叉树中的节点个数。使用自底向上的递归，每个节点的计算高度和判断是否平衡都只需要处理一次，最坏情况下需要遍历二叉树中的所有节点，因此时间复杂度是 O(n)。
/ 空间复杂度：O(n)，其中 nn 是二叉树中的节点个数。空间复杂度主要取决于递归调用的层数，递归调用的层数不会超过 n。

? 官解: https://leetcode.cn/problems/balanced-binary-tree/solution/ping-heng-er-cha-shu-by-leetcode-solution/
? 两者递归方式的讲解: https://leetcode.cn/problems/balanced-binary-tree/solution/ping-heng-er-cha-shu-di-gui-zi-ding-xiang-xia-zi-d/

*/
var isBalanced = function (root) {
    let res = checkBalanceHelper(root);
    if (res === -1) return false;
    else return true;
};

function checkBalanceHelper(node) {
    if (node === null) return 0;

    //# 左, 获取左子树的层数
    let leftHeight = checkBalanceHelper(node.left);
    // * 如果层数为-1直接退出
    if (leftHeight === -1) return -1;

    //# 右, 获取右子树的层数
    let rightHeight = checkBalanceHelper(node.right);
    // * 如果层数为-1直接退出
    if (rightHeight === -1) return -1;

    let diff = Math.abs(leftHeight - rightHeight);

    // # 如果左右节点高度相差大于 1, 直接返回-1, 否则返回最大高度
    if (diff > 1) {
        return -1;
    } else {
        //# 中
        return Math.max(leftHeight, rightHeight) + 1;
    }
}
