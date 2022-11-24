/*
* 使用前序求的就是深度，使用后序求的是高度。
* 高度是从下到上求(后续遍历)，深度是从上到下求解(前序遍历)
? 结合这篇文章的图来看: https://programmercarl.com/0110.  %E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E9%80%92%E5%BD%92

 * 递归函数 getDepth 的作用是: 计算以 node 为根节点的二叉树的最大深度, 并使用全局变量 result 记录
 * 递归函数 getDepth 的终止条件：遇到叶子节点时, 将当前这一分支的深度与目前的最大深度比较并更新。由于以叶子节点作为终止条件, 所以在递归过程中保证当前节点 node 不为空
 * 单层递归的逻辑:
 * ➀ 如果当前节点的左子树存在, 递归计算左子树的最大深度
 * ➁ 如果当前节点的右子树存在, 递归计算右子树的最大深度
 */
var maxDepth = function (root) {
    //* 如果根节点就是 Null, 说明深度是 0
    if (root === null) return 0;

    //* result 代表的是全局最大深度
    let result = 0;

    function getDepth(node, depth) {
        //* 终止条件, 如果左右节点都是空, 深度不可能再继续增加, 直接返回
        if (node.left === null && node.right === null) {
            //* 在到达叶子节点时检查depth. 因为传入的 depth 已经代表了在当前这一层的深度是多少(root节点默认为1), 看 depth 是否已经超过了其他叶子节点所在深度
            if (depth > result) result = depth;
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
