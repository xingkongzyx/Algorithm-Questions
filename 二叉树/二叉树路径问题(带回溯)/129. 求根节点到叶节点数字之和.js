var sumNumbers = function (root) {
    if (root === null) return 0;
    let sum = 0;
    let currentPath = [root.val];
    function traverse(node) {
        //* 终止条件就是遇到叶子节点
        if (node.left === null && node.right === null) {
            let digits = currentPath.length;
            let currentSum = 0;
            for (let i = 0; i < currentPath.length; i++) {
                currentSum +=
                    parseInt(currentPath[i]) *
                    Math.pow(10, digits - i - 1);
            }
            sum += currentSum;
            return;
        }

        if (node.left) {
            currentPath.push(node.left.val);
            traverse(node.left);
            currentPath.pop();
        }

        if (node.right) {
            currentPath.push(node.right.val);
            traverse(node.right);
            currentPath.pop();
        }
    }

    traverse(root);
    return sum;
};
