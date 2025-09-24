// ! 前序遍历

/*
 * 1. 确定递归函数的参数和返回值
 * 函数作用：搜索「二叉搜索树」中 val 对应的节点
 * 输入：「二叉搜索树」的根节点 root 和要搜索的值 val
 * 输出：值为 val 的「二叉搜索树」节点的引用
 *
 * 2. 确定终止条件
 *  如果root为空，或者找到这个数值了，就返回root节点。
 *
 * 3. 确定单层递归的逻辑
 * 因为二叉搜索树的节点是有序的，所以可以有方向的去搜索。
 * 如果root.val > val，递归搜索左子树，如果root.val < val，递归搜索右子树，最后如果都没有搜索到，就返回NULL。
 *
 */

var searchBST = function (root, val) {
    //* 递归终止条件
    if (root === null) return null;
    //# 中
    if (root.val === val) return root;
    //# 左
    else if (root.val > val) return searchBST(root.left, val);
    //# 右
    else if (root.val < val) return searchBST(root.right, val);
};
