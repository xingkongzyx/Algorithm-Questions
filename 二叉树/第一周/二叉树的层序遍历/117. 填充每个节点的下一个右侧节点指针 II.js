var connect = function (root) {
    let queue = [];
    if (root !== null) queue.push(root);
    while (queue.length > 0) {
        let currentLevelSize = queue.length;
        let headNode;
        for (let i = 0; i < currentLevelSize; i++) {
            let poppedNode = queue.shift();
            if (i === 0) headNode = poppedNode;
            else {
                headNode.next = poppedNode;
                headNode = headNode.next;
            }

            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);
        }
        headNode.next = null;
    }
    return root;
};
