//? https://leetcode.cn/problems/count-complete-tree-nodes/solution/tu-jie-222-wan-quan-er-cha-shu-de-jie-dian-ge-shu-/
var countNodes = function (root) {
    if (root === null) return 0;
    let temp = root;
    let leftDepth = 0;
    //* 求左子树的高度
    while (temp) {
        temp = temp.left;
        leftDepth += 1;
    }
    temp = root;
    //* 求右子树的高度
    let rightDepth = 0;
    while (temp) {
        temp = temp.right;
        rightDepth += 1;
    }

    //* 如果两边高度相同，说明这是一个 perfect binary tree，直接通过数学计算返回节点数量
    if (leftDepth === rightDepth) {
        return 2 ** leftDepth - 1;
    }
    //* 当前子树不是完美二叉树，只是完全二叉树，递归处理左右子树
    return 1 + countNodes(root.left) + countNodes(root.right);
};
