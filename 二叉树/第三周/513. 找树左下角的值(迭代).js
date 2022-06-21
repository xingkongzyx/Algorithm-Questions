//! 层序遍历
var findBottomLeftValue = function (root) {
    let queue = [];
    if (root !== null) queue.push(root);
    let leftVal;
    while (queue.length > 0) {
        let currentLevelLength = queue.length;

        for (let i = 0; i < currentLevelLength; i++) {
            let poppedNode = queue.shift();
            if (i === 0) leftVal = poppedNode.val;

            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);
        }
    }

    return leftVal;
};
