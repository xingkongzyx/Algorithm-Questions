var minDepth = function (root) {
    //* 如果根节点就是 Null, 说明深度是 0
    if (root === null) return 0;
    //* result 代表的是最小深度
    let result = Infinity;

    function getDepth(node, depth) {
        //* 终止条件，如果左右节点都是空，说明遇到了叶子节点，判断此时的深度与最小深度(result)哪个更小
        if (node.left === null && node.right === null) {
            result = Math.min(depth, result);
        }

        if (node.left) {
            depth += 1;
            getDepth(node.left, depth);
            depth -= 1;
        }
        if (node.right) {
            depth += 1;
            getDepth(node.right, depth);
            depth -= 1;
        }
    }
    //* root节点的所在深度默认为1
    getDepth(root, 1);
    return result;
};
