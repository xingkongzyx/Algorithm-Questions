var preorderTraversal = (root) => {
    let stack = [];
    if (root !== null) stack.push(root);
    let result = [];
    //! 入栈 右 -> 左
    //! 出栈 中 -> 左 -> 右
    while (stack.length) {
        let poppedNode = stack.pop();
        // > 中
        result.push(poppedNode.val);
        // > 右
        if (poppedNode.right) stack.push(poppedNode.right);
        // > 左
        if (poppedNode.left) stack.push(poppedNode.left);
    }
    return result;
};
