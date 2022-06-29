var isUnivalTree = function (root) {
    function helper(node, val) {
        if (node === null) {
            return true;
        }
        //# 中
        if (node.val !== val) {
            console.log(node.val, val);
            return false;
        }

        //# 左
        let leftCheck = helper(node.left, val);
        //# 右
        let rightCheck = helper(node.right, val);

        return leftCheck && rightCheck;
    }
    return helper(root, root.val);
};
