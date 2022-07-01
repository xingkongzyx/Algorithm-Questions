//! 后序遍历

//# 如果左节点不为空，且左节点没有左右孩子，那么这个节点的左节点就是左叶子
//# 判断当前节点是不是左叶子是无法判断的，必须要通过节点的父节点来判断其左孩子是不是左叶子。

/*
 * 1. 确定递归函数的参数和返回值
 * 判断一个树的左叶子节点之和，那么一定要传入树的根节点，递归函数的返回值为数值之和，所以为int
 *
 * 2. 确定终止条件
 * 依然是 "if (root == NULL) return 0;"
 *
 * 3. 确定单层递归的逻辑
 * 当遇到左叶子节点的时候，记录数值，然后通过递归求取左子树左叶子之和，和 右子树左叶子之和，相加便是整个树的左叶子之和。
 */

/// 非常像「二叉树的节点个数」以及「二叉树的最大深度」的题目，左子树的节点个数是多少(这里是左子树左叶子的和是多少)，右子树的节点个数是多少(这里是右子树左叶子的和是多少). 然后再加上当前节点个数(这里是如果当前节点的左节点是左叶子, 它的值就是 leftSum)
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
