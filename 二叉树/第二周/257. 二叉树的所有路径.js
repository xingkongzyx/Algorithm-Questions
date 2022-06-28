var binaryTreePaths = function (root) {
    let totalPaths = [];
    let currentPath = [root.val];

    traversal(root, currentPath, totalPaths);
    return totalPaths;
};

/*
 * 1. 递归函数函数参数以及返回值
 * 参数只需要根节点，不需要返回值，函数调用过程中负责将目前的节点加入 currentPath 并使其左右子节点参与构建路径
 *
 * 2. 确定递归终止条件
 * 到叶子节点时，就开始结束的处理逻辑（把路径放进result里）。
 * 那么什么时候算是找到了叶子节点？ 是当 cur不为空，其左右孩子都为空的时候，就找到叶子节点。
 * 所以本题的终止条件是：if (node.left === null && node.right === null)
 *
 * 3. 确定单层递归逻辑
 * 因为是前序遍历，需要先处理中间节点，这里对中间节点的处理也是判断它是否是叶子节点(终止条件).
 *
 * 然后就是递归和回溯的过程。对节点的左右子树进行递归从而构建路径的过程中，因为 currentPath 不能一直加入节点，它还要删节点，然后才能加入新的节点。
 *
 */

function traversal(node, currentPath, totalPaths) {
    if (node.left === null && node.right === null) {
        let pathStr = currentPath.join("->");
        totalPaths.push(pathStr);
        return;
    }

    //* 对左子树进行递归
    if (node.left) {
        currentPath.push(node.left.val);
        //# 回溯和递归是一一对应的，有一个递归，就要有一个回溯
        traversal(node.left, currentPath, totalPaths);
        currentPath.pop();
    }

    //* 对右子树进行递归
    if (node.right) {
        currentPath.push(node.right.val);
        //# 回溯和递归是一一对应的，有一个递归，就要有一个回溯
        traversal(node.right, currentPath, totalPaths);
        currentPath.pop();
    }
}
