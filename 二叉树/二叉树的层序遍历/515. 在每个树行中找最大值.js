var largestValues = function (root) {
    let res = [];
    let queue = [];
    if (root !== null) queue.push(root);

    while (queue.length > 0) {
        let size = queue.length;
        let currentLevelMaxVal = queue[0].val;
        while (size > 0) {
            let poppedNode = queue.shift();
            if (poppedNode.val > currentLevelMaxVal)
                currentLevelMaxVal = poppedNode.val;
            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);
            size--;
        }
        res.push(currentLevelMaxVal);
    }
    return res;
};
