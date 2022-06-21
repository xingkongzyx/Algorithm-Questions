var minDepth = function (root) {
    let queue = [];
    if (root !== null) queue.push(root);
    let depth = 0;
    while (queue.length > 0) {
        let currentLevelSize = queue.length;
        while (currentLevelSize > 0) {
            let poppedNode = queue.shift();
            //! 因为depth是在最后加一，所以在这里我们发现 left child && right child 都为空的Node时，我们因为这个level的depth还没有加，所以返回时直接返回 (depth + 1)
            if (poppedNode.left === null && poppedNode.right === null)
                return depth + 1;
            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);
            currentLevelSize--;
        }
        depth++;
    }
    return depth;
};
