/* 
> 这道题目的递归法和求二叉树的最大深度写法类似. 而迭代法使用层序遍历，记录遍历的节点数量就可以了。
! 递归遍历的顺序依然是后序（左右中）
* 1. 确定递归函数的参数和返回值：参数就是传入树的根节点，返回就返回以该节点为根节点二叉树的节点数量，所以返回值为int类型。
* 2. 确定终止条件：如果为空节点的话，就返回0，表示节点数为0。
* 3. 确定单层递归的逻辑：先求它的左子树的节点数量，再求的右子树的节点数量，最后取总和再加一 （加1是因为算上当前中间节点）就是目前节点为根节点的节点数量。

*/

var countNodes = function (root) {
    if (root === null) return 0;
    let leftNodes = countNodes(root.left);
    let rightNodes = countNodes(root.right);

    return 1 + leftNodes + rightNodes;
};
