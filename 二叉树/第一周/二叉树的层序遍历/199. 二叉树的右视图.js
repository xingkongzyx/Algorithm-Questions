/*
 * 层序遍历的时候，判断是否遍历到单层的最后面的元素，如果是，就放进result数组中，随后返回result就可以了。
 */

var rightSideView = function (root) {
    let res = [];
    let queue = [];
    if (root !== null) queue.push(root);
    while (queue.length > 0) {
        let currentLevelSize = queue.length;
        while (currentLevelSize > 0) {
            let poppedNode = queue.shift();
            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);

            if (currentLevelSize === 1) res.push(poppedNode.val);
            currentLevelSize--;
        }
    }
    return res;
};
