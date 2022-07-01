/* 
//! 后序遍历
//? https://leetcode.cn/problems/balanced-binary-tree/solution/balanced-binary-tree-di-gui-fang-fa-by-jin40789108/
* 这道题的递归终止条件有两个：
* 1. 当越过叶子节点时，返回高度 0；
* 2. 当左（右）子树高度『leftHeight == -1』或者『rightHeight == -1』时，代表此子树的 左（右）子树 不是平衡树，因此直接返回 -1；

*/
var isBalanced = function (root) {
    let res = getHeight(root);
    if (res === -1) return false;
    else return true;
};

function getHeight(node) {
    if (node === null) return 0;

    //# 左
    let leftHeight = getHeight(node.left);
    if (leftHeight === -1) return -1;

    //# 右
    let rightHeight = getHeight(node.right);
    if (rightHeight === -1) return -1;

    let diff = Math.abs(leftHeight - rightHeight);

    if (diff > 1) {
        return -1;
    } else {
        //# 中
        return Math.max(leftHeight, rightHeight) + 1;
    }
}
