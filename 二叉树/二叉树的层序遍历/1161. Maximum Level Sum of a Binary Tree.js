var maxLevelSum = function (root) {
    let result = 1;

    let queue = [root];
    let totalSum = -Infinity;
    let curLevel = 0;

    while (queue.length > 0) {
        curLevel++;
        let levelNodes = queue.length;
        let curSum = 0;
        for (let i = 0; i < levelNodes; i++) {
            let node = queue.shift();
            curSum += node.val;
            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
        }
        if (curSum > totalSum) {
            totalSum = curSum;
            result = curLevel;
        }
    }

    return result;
};
