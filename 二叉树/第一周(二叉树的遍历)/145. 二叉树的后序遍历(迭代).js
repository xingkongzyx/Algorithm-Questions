// 前序是 中->左->右
// 后序是 左->右->中
// 改变办法就是将前序的遍历顺序变为 中->右->左，最后再reverse result array
var postorderTraversal = function (root) {
    let stack = [];
    let result = [];
    if (root !== null) stack.push(root);

    while (stack.length > 0) {
        let poppedNode = stack.pop();
        result.push(poppedNode.val);
        if (poppedNode.left) stack.push(poppedNode.left);
        if (poppedNode.right) stack.push(poppedNode.right);
    }

    return result.reverse();
};
