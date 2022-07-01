//! 二叉树层序遍历来进行迭代解题

var maxDepth = function (root) {
    let queue = [];
    if (root !== null) queue.push(root);
    let depth = 0;

    while (queue.length > 0) {
        let currentLevelLength = queue.length;
        while (currentLevelLength > 0) {
            let poppedNode = queue.shift();
            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);
            currentLevelLength--;
        }
        depth++;
    }

    return depth;
};
