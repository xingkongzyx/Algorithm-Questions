/* 
? https://leetcode.cn/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-di-gui-jie-fa-dai-m-p5rs/

! 判断一棵二叉树是否轴对称，其实就是判断这颗二叉树的左右两个子树是否互为镜像。
* 两个子树是否互为镜像当且仅当:
* 1. 两个子树根节点的值相同
* 2. 第一棵子树的左子树和第二棵子树的右子树对称，且第一棵子树的右子树和第二棵子树的左子树对称；
*/

var isSymmetric = function (root) {
    if (root === null) return true;
    return symmetricHelper(root.left, root.right);
};

function symmetricHelper(leftTree, rightTree) {
    if (leftTree === null && rightTree !== null) return false;
    else if (leftTree !== null && rightTree === null) return false;
    else if (leftTree === null && rightTree === null) return true;
    //* 前序遍历查看节点值是否相等，不相等返回false
    if (leftTree.val !== rightTree.val) return false;
    return (
        symmetricHelper(leftTree.left, rightTree.right) &&
        symmetricHelper(leftTree.right, rightTree.left)
    );
}
