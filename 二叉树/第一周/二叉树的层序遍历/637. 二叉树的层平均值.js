var averageOfLevels = function (root) {
    let res = [];
    let queue = [];
    if (root !== null) queue.push(root);
    while (queue.length > 0) {
        let currentLevelSize = queue.length;
        let currentLevelSum = 0;
        let i = 0;
        while (i < currentLevelSize) {
            let poppedNode = queue.shift();
            currentLevelSum += poppedNode.val;
            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);
            i++;
        }
        res.push(currentLevelSum / currentLevelSize);
    }
    return res;
};
