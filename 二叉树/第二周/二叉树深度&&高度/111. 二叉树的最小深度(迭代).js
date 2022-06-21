var minDepth = function (root) {
    let queue = [];
    if (root !== null) queue.push(root);
    let depth = 0;

    while (queue.length > 0) {
        let currentLevelLength = queue.length;
        depth++;
        while (currentLevelLength > 0) {
            let poppedNode = queue.shift();
            //# 只有当左右孩子都为空的时候，才说明遍历到最低点了。如果其中一个孩子为空则不是最低点
            if (poppedNode.left === null && poppedNode.right === null)
                return depth;
            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);
            currentLevelLength--;
        }
    }

    return depth;
};
