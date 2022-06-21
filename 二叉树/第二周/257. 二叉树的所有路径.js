var binaryTreePaths = function (root) {
    let totalPaths = [];
    let currentPath = [];

    traversal(root, currentPath, totalPaths);
    return totalPaths;
};

// ! 前序遍历中

/*
 * 1. 递归函数函数参数以及返回值
 * 要传入根节点，记录每一条路径的path，和存放结果集的result，这里递归不需要返回值
 *
 * 2. 确定递归终止条件
 * 因为本题找到叶子节点时，就应该开始结束的处理逻辑了（把路径放进result里）。
 * 那么什么时候算是找到了叶子节点？ 是当 cur不为空，其左右孩子都为空的时候，就找到叶子节点。
 * 所以本题的终止条件是：if (node.left === null && node.right === null)
 *
 * 3. 确定单层递归逻辑
 * 因为是前序遍历，需要先处理中间节点，中间节点就是我们要记录路径上的节点，先放进 currentPath 中。 currentPath.push(node.val);
 *
 * 然后就是递归和回溯的过程。在对左右子树进行递归的过程中，因为 currentPath 不能一直加入节点，它还要删节点，然后才能加入新的节点。
 *
 */

function traversal(node, currentPath, totalPaths) {
    // 前序遍历中 先访问node元素
    currentPath.push(node.val);

    if (node.left === null && node.right === null) {
        let pathStr = currentPath.join("->");
        totalPaths.push(pathStr);
    }

    // 前序遍历中 对左子树进行递归
    if (node.left) {
        traversal(node.left, currentPath, totalPaths);
        currentPath.pop();
    }

    // 前序遍历中 对右子树进行递归
    if (node.right) {
        traversal(node.right, currentPath, totalPaths);
        currentPath.pop();
    }
}
