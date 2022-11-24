/*
 * 递归函数 getDepth 的作用是: 计算以 node 为根节点的二叉树的最小深度, 并使用全局变量 result 记录
 * 递归函数 getDepth 的终止条件：遇到叶子节点时, 将当前这一分支的深度与目前的最小深度比较并更新。由于以叶子节点作为终止条件, 所以在递归过程中要保证当前节点 node 不为空
 * 单层递归的逻辑:
 * ➀ 如果当前节点的左子树存在, 递归计算左子树的最小深度
 * ➁ 如果当前节点的右子树存在, 递归计算右子树的最小深度
 */

var minDepth = function (root) {
    //* 如果根节点就是 Null, 说明深度是 0
    if (root === null) return 0;
    //* result 代表的是最小深度
    let result = Infinity;

    function getDepth(node, depth) {
        //* 终止条件，如果左右节点都是空，说明遇到了叶子节点，判断此时的深度与最小深度(result)哪个更小
        if (node.left === null && node.right === null) {
            result = Math.min(depth, result);
            return;
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
