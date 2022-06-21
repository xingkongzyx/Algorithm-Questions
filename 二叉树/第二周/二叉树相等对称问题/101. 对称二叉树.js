/* 
# 本题遍历只能是“后序遍历”，因为我们要通过递归函数的返回值来判断两个子树的内侧节点和外侧节点是否相等。
# 正是因为要遍历两棵树而且要比较内侧和外侧节点，所以准确的来说是一个树的遍历顺序是左右中，一个树的遍历顺序是右左中。
*/

var isSymmetric = function (root) {
    if (root === null) return true;
    return symmetricHelper(root.left, root.right);
};

function symmetricHelper(leftTree, rightTree) {
    if (leftTree === null && rightTree !== null) return false;
    else if (leftTree !== null && rightTree === null) return false;
    else if (leftTree === null && rightTree === null) return true;
    else if (leftTree.val !== rightTree.val) return false;
    else
        return (
            symmetricHelper(leftTree.left, rightTree.right) &&
            symmetricHelper(leftTree.right, rightTree.left)
        );
}
