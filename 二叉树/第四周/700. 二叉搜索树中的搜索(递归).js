// ! 前序遍历

/*
 * 1. 确定递归函数的参数和返回值
 *  递归函数的参数传入的就是根节点和要搜索的数值，返回的就是以这个搜索数值所在的节点。
 * 2. 确定终止条件
 *  如果root为空，或者找到这个数值了，就返回root节点。
 *
 * 3. 确定单层递归的逻辑
 * 因为二叉搜索树的节点是有序的，所以可以有方向的去搜索。
 *  如果root.val > val，搜索左子树，如果root.val < val，就搜索右子树，最后如果都没有搜索到，就返回NULL。
 *
 */

var searchBST = function (root, val) {
    if (root === null || root.val === val) return root;

    if (root.val > val) return searchBST(root.left, val);

    if (root.val < val) return searchBST(root.right, val);

    return null;
};
