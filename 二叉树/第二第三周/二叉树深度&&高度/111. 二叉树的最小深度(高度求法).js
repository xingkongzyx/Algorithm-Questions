/* 
! 用后序遍历（左右中）来计算树的高度。
* 1. 确定递归函数的参数和返回值：参数就是传入树的根节点，返回就返回这棵树的深度，所以返回值为int类型。
* 2. 确定终止条件：如果为空节点的话，就返回0，表示高度为0。
* 3. 确定单层递归的逻辑：
# 与求最大深度的逻辑不同: 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。，注意是叶子节点。左右孩子都为空的节点才是叶子节点!
* 如果左子树为空，右子树不为空，说明最小深度是 1 + 右子树的深度。反之，右子树为空，左子树不为空，最小深度是 1 + 左子树的深度。 最后如果左右子树都不为空，返回左右子树深度最小值 + 1 。 

! 我们还可以像求最大深度那样使用递归的方式，返回Math.min(左子树的深度，右子树的深度)+1，看起来很有道理，如果左右子树都不为空或者都为空是没问题的。但有一个问题，如果左右子树一个为空一个不为空，就会有问题了，因为为空的那个子节点的深度是0，我们不能用它，所以这里要有个判断。

? 链接：https://leetcode.cn/problems/minimum-depth-of-binary-tree/solution/acm-xuan-shou-tu-jie-leetcode-by-rocky04-hbup/

*/
var minDepth = function (root) {
    if (root === null) return 0;

    let leftDepth = minDepth(root.left);
    let rightDepth = minDepth(root.right);
    //* 如果 root.left 和 root.right 只有一个为 空，说明他只有一个子结点，我们只需要返回它另一个子节点的最小深度 +1 即可
    if (root.left === null && root.right !== null) {
        return 1 + rightDepth;
    } else if (root.left !== null && root.right === null) {
        return 1 + leftDepth;
    } else {
        //* 如果left和right都为空或者都不为空，说明他有零个或者两个子节点，我们只需要返回 最小深度 +1 即可。
        return 1 + Math.min(leftDepth, rightDepth);
    }
};
