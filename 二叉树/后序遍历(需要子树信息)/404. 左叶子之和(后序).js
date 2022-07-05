//! 后序遍历
/*
# 在这里到达左叶子的判断标准为：
#  ➊ 是否是当前节点的左孩子
#  ➋ 当前节点的左孩子是不是叶子节点（叶子结点：没有左右孩子）


 * 1. 确定递归函数的参数和返回值
 * 递归函数的含义是: 在以 node 为根节点的子树中计算左叶子之和
 * 输入: 根节点
 * 返回: 当前子树的左叶子之和
 *
 * 2. 确定终止条件
 * 依然是 "if (root == NULL) return 0;"
 *
 * 3. 确定单层递归的逻辑
 * 首先递归求取左子树左叶子之和，和右子树左叶子之和，然后判断当前节点的左子节点是否是左叶子节点，是的话说明 leftSum = node.left.val. 最后通过相加便是整个树的左叶子之和。
 */

/// 非常像「222. 完全二叉树的节点个数」以及「104. 二叉树的最大深度」的题目，左子树的节点个数是多少(这里是左子树左叶子的和是多少)，右子树的节点个数是多少(这里是右子树左叶子的和是多少). 然后再加上当前节点个数(这里是如果当前节点的左节点是左叶子, 它的值就是 leftSum)
var sumOfLeftLeaves = function (root) {
    if (root === null) return 0;

    let leftSum = sumOfLeftLeaves(root.left);
    let rightSum = sumOfLeftLeaves(root.right);
    //* 判断当前节点是否有左叶子节点. 如果当前节点的左子节点就是题目所要的「左叶子」，说明前面获取的 leftSum 肯定是 0
    if (
        root.left !== null &&
        root.left.left === null &&
        root.left.right === null
    )
        leftSum = root.left.val;

    return leftSum + rightSum;
};
