var inorderTraversal = function (root) {
    if (root === null) return [];
    let cur = root;
    let stack = [];
    let result = [];
    while (cur !== null || stack.length > 0) {
        if (cur) {
            stack.push(cur);
            cur = cur.left;
        } else {
            let poppedNode = stack.pop();
            result.push(poppedNode.val);
            cur = poppedNode.right;
        }
    }
    return result;
};
