//! 后序遍历
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
