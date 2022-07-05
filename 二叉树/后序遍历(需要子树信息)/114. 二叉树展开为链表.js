//> “不去管函数的内部细节是如何处理的，我们只看其函数作用以及输入与输出” 就像看起来简单但是实际威力巨大的功法口诀 一般。
//* 对于函数flatten来说, 它的函数作用是：将一个二叉树, 原地将它展开为链表, 没有返回值
//? https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solution/114-er-cha-shu-zhan-kai-wei-lian-biao-by-ming-zhi-/
//! 后序遍历
var flatten = function (root) {
    if (root === null) return null;

    //* 左: 将根节点的左子树变成链表
    flatten(root.left);
    //* 右: 将根节点的右子树变成链表
    flatten(root.right);

    //* 中
    let tempRight = root.right;
    //* 把树的右边换成左边的链表
    root.right = root.left;
    //* 记得要将左边置空
    root.left = null;

    //* 找到树的最右边的节点
    let tempNode = root;
    while (tempNode.right !== null) {
        tempNode = tempNode.right;
    }
    //* 把右边的链表接到刚才树的最右边的节点
    tempNode.right = tempRight;
};
