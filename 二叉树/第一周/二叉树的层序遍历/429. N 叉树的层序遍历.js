var levelOrder = function (root) {
    let queue = [];
    if (root !== null) queue.push(root);
    let res = [];
    while (queue.length > 0) {
        let currentLevelSize = queue.length;
        let currentLevelNodes = [];
        while (currentLevelSize > 0) {
            let poppedNode = queue.shift();
            if (poppedNode !== null)
                currentLevelNodes.push(poppedNode.val);
            if (poppedNode.children.length > 0) {
                queue.push(...poppedNode.children);
            }
            currentLevelSize--;
        }
        res.push(currentLevelNodes);
    }
    return res;
};
