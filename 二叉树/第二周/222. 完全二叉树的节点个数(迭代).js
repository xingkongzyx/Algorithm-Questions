var countNodes = function (root) {
    let queue = [];
    if (root !== null) {
        queue.push(root);
    }

    let nodeCount = 0;
    while (queue.length > 0) {
        let poppedNode = queue.shift();
        nodeCount++;
        if (poppedNode.left) queue.push(poppedNode.left);
        if (poppedNode.right) queue.push(poppedNode.right);
    }

    return nodeCount;
};
