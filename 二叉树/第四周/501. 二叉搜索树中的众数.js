/* var findMode = function (root) {
    let inOrderTraversalResult = {};
    let inOrderTraversal = function (node) {
        if (node === null) return;

        inOrderTraversal(node.left);
        if (node.val in inOrderTraversalResult)
            inOrderTraversalResult[node.val]++;
        else inOrderTraversalResult[node.val] = 1;
        inOrderTraversal(node.right);
    };
    inOrderTraversal(root);
    let modes = [];
    let times = 0;
    for (let key in inOrderTraversalResult) {
        if (inOrderTraversalResult[key] > times) {
            times = inOrderTraversalResult[key];
        }
    }

    for (let key in inOrderTraversalResult) {
        if (inOrderTraversalResult[key] == times) {
            modes.push(key);
        }
    }

    return modes;
}; */

//> 因为是BST才能使用如下方法，如果是一般的tree使用上面的方法
//> 中序遍历
var findMode = function (root) {
    let prevNode = null;
    let count = 0;
    let result = [];
    let maxCount = 0;
    function inOrderTraverse(currentNode) {
        if (currentNode === null) return;

        inOrderTraverse(currentNode.left);
        if (prevNode === null) count = 1;
        else if (prevNode.val === currentNode.val) count++;
        else count = 1;

        prevNode = currentNode;

        if (count === maxCount) result.push(currentNode.val);

        if (count > maxCount) {
            maxCount = count;
            result = [currentNode.val];
        }
        inOrderTraverse(currentNode.right);
    }

    inOrderTraverse(root);
    return result;
};
