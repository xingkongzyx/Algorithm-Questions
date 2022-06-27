var findBottomLeftValue = function (root) {
    let queue = [root];
    let result = root.val;

    while (queue.length > 0) {
        let curLevelLen = queue.length();
        result = queue[0].val;

        for (let i = 0; i < curLevelLen; i++) {
            let poppedNode = queue.shift();
            if (poppedNode.left) {
                queue.push(poppedNode.left);
            }

            if (poppedNode.right) {
                queue.push(poppedNode.right);
            }
        }
    }
    return result;
};
