/* 
! 用后序遍历（左右中）来计算树的高度。
* 1. 确定递归函数的参数和返回值：参数就是传入树的根节点，返回就返回这棵树的深度，所以返回值为int类型。
* 2. 确定终止条件：如果为空节点的话，就返回0，表示高度为0。
* 3. 确定单层递归的逻辑：
# 与求最大深度的逻辑不同: 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。，注意是叶子节点。左右孩子都为空的节点才是叶子节点!
* 如果左子树为空，右子树不为空，说明最小深度是 1 + 右子树的深度。反之，右子树为空，左子树不为空，最小深度是 1 + 左子树的深度。 最后如果左右子树都不为空，返回左右子树深度最小值 + 1 。 
*/
var minDepth = function (root) {
    if (root === null) return 0;

    let leftDepth = minDepth(root.left);
    let rightDepth = minDepth(root.right);
    if (root.left === null && root.right !== null) {
        return 1 + rightDepth;
    } else if (root.left !== null && root.right === null) {
        return 1 + leftDepth;
    } else {
        return 1 + Math.min(leftDepth, rightDepth);
    }
};
