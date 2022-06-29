//> 前序遍历

/* 
100. 相同的树
226. 翻转二叉树
104. 二叉树的最大深度
110. 平衡二叉树
543. 二叉树的直径
617. 合并二叉树
572. 另一个树的子树
965. 单值二叉树

作者：eh-xing-qing
链接：https://leetcode-cn.com/problems/merge-two-binary-trees/solution/yi-pian-wen-zhang-dai-ni-chi-tou-dui-che-asg8/


1. 确定递归函数的参数和返回值：
首先那么要合入两个二叉树，那么参数至少是要传入两个二叉树的根节点，返回值就是合并之后二叉树的根节点。

2. 确定终止条件：
因为是传入了两个树，那么就有两个树遍历的节点t1 和 t2，
如果 t1 === null && t2 !== null，两个树合并就应该是 t2.
如果 t1 !== null && t2 === null，两个树合并就应该是 t1.
如果两个都是null，则返回null

3. 确定单层递归的逻辑：
单层递归中，就要把两棵树的元素加到一起形成新的 treeNode.     
新的 treeNode 的左子树是：合并 t1左子树 t2左子树之后的左子树。
新的 treeNode 的右子树是：合并 t1右子树 t2右子树之后的右子树。
最终 treeNode 就是合并之后的根节点。
*/

var mergeTrees = function (root1, root2) {
    if (root1 === null && root2 !== null) return root2;
    else if (root1 !== null && root2 === null) return root1;
    else if (root1 === null && root2 === null) return null;

    // > 中
    let nodeVal = root1.val + root2.val;
    let treeNode = new TreeNode(nodeVal);
    // > 左
    treeNode.left = mergeTrees(root1.left, root2.left);
    // > 右
    treeNode.right = mergeTrees(root1.right, root2.right);

    return treeNode;
};
