//* 使用前序求的就是深度，使用后序求的是高度。
//* 高度是从下到上求(后续遍历)，深度是从上到下求解(前序遍历)

var maxDepth = function (root) {
    //* 如果根节点就是 Null, 说明深度是 0
    if (root === null) return 0;
    //* result 代表的是最大深度
    let result = 0;

    function getDepth(node, depth) {
        //* 传入的 depth 已经代表了在当前这一层的深度是多少(root节点默认为1), 从 root 开始算
        if (depth > result) result = depth;
        //* 终止条件，如果左右节点都是空，深度不可能再继续增加，直接返回
        if (node.left === null && node.right === null) return;

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
