var kthSmallest = function (root, k) {
    //* 用一个全局变量保存当前访问到第几个节点。
    let count = k;
    //* 用一个全局变量保存最终的结果；
    let result = null;
    function inorder(node) {
        if (node === null) return;
        inorder(node.left);
        count -= 1;
        //* 当 count 等于 0, 说明此时遍历到了第k个节点，直接返回
        if (count == 0) {
            result = node.val;
            return;
        }
        inorder(node.right);
    }
    inorder(root);
    return result;
};
