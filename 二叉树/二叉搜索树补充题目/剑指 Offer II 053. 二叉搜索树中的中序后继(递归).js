//? 本题与主站 285 题相同
//? https://leetcode.cn/problems/P5rCT8/

/*
   / 由于只需要找到节点 p 的中序后继, 因此不需要维护完整的中序遍历序列, 只需要在中序遍历的过程中维护上一个访问的节点和当前访问的节点。中序遍历的时候用 prevNode 指针保存上一次访问的结点, 当 prevNode == p 的时候, 那么现在访问的r node 就是我们要找的「后继节点」直接返回, 不需要继续遍历其他的子树；
 * 1. 确定递归函数的参数和返回值
 *  递归函数的参数传入的就是根节点, 返回的就是 p 的「后继节点」。
 * 2. 确定终止条件
 *  如果 root 为空, 说明这棵子树不包含 p, 自然也没有 p 的「后继节点」, 返回 null
 *
 * 3. 确定单层递归的逻辑
 *  因为二叉搜索树的节点是有序的, 所以可以有方向的去搜索。
 *  使用中序遍历, 在检查当前节点前, 首先对左子树进行递归搜索查看是否拥有 「后继节点」, 如果有的话直接返回(非常重要, 也是提高效率的关键), 不再继续遍历. 如果没有的话则将 prevNode 更新为左子树节点(node.left)
 *  然后查看当前位置如果 prevNode 不为空的情况下 prevNode 是否就是 p, 如果是的话返回它的「后继节点」也就是 当前正在遍历的 node 节点. 如果 prevNode 不是 p, 则更新 prevNode 到当前 node
 *  对右子树进行递归搜索查看是否拥有 p 的「后继节点」, 如果有的话直接返回(非常重要, 也是提高效率的关键), 不再继续遍历. 如果没有的话则将 prevNode 更新.
 *
 */

var inorderSuccessor = function (root, p) {
    let prevNode = null;
    function traverse(node) {
        if (node === null) return null;

        // 左
        let leftRes = traverse(node.left);
        if (leftRes != null) return leftRes;

        // 中
        if (prevNode != null && prevNode == p) {
            return node;
        }
        prevNode = node;

        // 右
        let rightRes = traverse(node.right);
        if (rightRes != null) return rightRes;

        return null;
    }

    let result = traverse(root);
    return result;
};
