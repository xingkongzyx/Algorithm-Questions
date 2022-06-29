var maxDepth = function (root) {
    let queue = [];
    if (root !== null) queue.push(root);
    let depth = 0;
    while (queue.length > 0) {
        let currentLevelSize = queue.length;
        while (currentLevelSize > 0) {
            let poppedNode = queue.shift();
            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);
            currentLevelSize--;
        }
        depth++;
    }
    return depth;
};
