var countNodes = function (root) {
    if (root === null) return 0;
    let temp = root;
    let leftDepth = 0;
    // 求左子树的深度
    while (temp) {
        temp = temp.left;
        leftDepth += 1;
    }
    temp = root;
    let rightDepth = 0;
    while (temp) {
        temp = temp.right;
        rightDepth += 1;
    }

    if (leftDepth === rightDepth) {
        return 2 ** leftDepth - 1;
    }
    // 当前子树不是完美二叉树，只是完全二叉树，递归处理左右子树
    return 1 + countNodes(root.left) + countNodes(root.right);
};
