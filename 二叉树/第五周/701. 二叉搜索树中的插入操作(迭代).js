var insertIntoBST = function (root, val) {
    if (root === null) return new TreeNode(val);
    let currentNode = root;
    while (true) {
        if (currentNode.val > val) {
            if (currentNode.left === null) {
                currentNode.left = new TreeNode(val);
                break;
            }
            currentNode = currentNode.left;
        } else if (currentNode.val < val) {
            if (currentNode.right === null) {
                currentNode.right = new TreeNode(val);
                break;
            }
            currentNode = currentNode.right;
        }
    }

    return root;
};
