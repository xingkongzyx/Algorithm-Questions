// ! 前序遍历

var sumOfLeftLeaves = function (root) {
    let stack = [];
    let sum = 0;
    if (root !== null) stack.push(root);
    while (stack.length > 0) {
        let poppedNode = stack.pop();
        //# 访问当前Node(中)
        if (
            poppedNode.left !== null &&
            poppedNode.left.left === null &&
            poppedNode.left.right === null
        )
            sum += poppedNode.left.val;
        //# 处理左边node(左)
        if (poppedNode.right !== null) stack.push(poppedNode.right);
        //# 处理右边node(右)
        if (poppedNode.left !== null) stack.push(poppedNode.left);
    }

    return sum;
};
