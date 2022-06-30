//* 通过递归中序遍历将二叉搜索树转变成一个有序的数组
//* 然后只要比较一下，这个数组是否是有序的，注意二叉搜索树中不能有重复元素。

var isValidBST = function (root) {
    let traverseResults = [];

    let traverse = function (node) {
        if (node === null) return;
        traverse(node.left);
        traverseResults.push(node.val);
        traverse(node.right);
    };

    traverse(root);
    for (let i = 1; i < traverseResults.length; i++) {
        if (traverseResults[i - 1] < traverseResults[i]) continue;
        else return false;
    }

    return true;
};
