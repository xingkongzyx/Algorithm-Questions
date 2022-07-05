/*
 * 递归函数的含义是: 在以 node 为根节点的子树中寻找左叶子节点，找到后将其值加到全局变量 sum 中
 * 输入: 根节点
 * 返回: 无
 * 单层递归逻辑:
 * ➀ 判断当前节点是否存在左叶子节点, 在这里到达左叶子的判断标准为：
 *   ➊ 是否是当前节点的左孩子
 *   ➋ 当前节点的左孩子是不是叶子节点（叶子结点：没有左右孩子），是的话将它的值累加到 sum 中
 * ➁ 在左子树中递归寻找左叶子节点，在右子树中递归寻找左叶子节点
 */
var sumOfLeftLeaves = function (root) {
    let sum = 0;
    function helper(node) {
        if (node === null) return;
        //# 中
        if (
            node.left !== null &&
            node.left.left === null &&
            node.left.right === null
        )
            sum += node.left.val;
        //# 左
        helper(node.left);
        //# 右
        helper(node.right);
    }
    helper(root);
    return sum;
};
