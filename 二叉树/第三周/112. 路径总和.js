// > 本题我们要找一条符合条件的路径，所以递归函数需要返回值，及时返回
// ! 可以使用深度优先遍历的方式来遍历二叉树.
// ! 本题前中后序遍历都可以，因为中节点也没有处理逻辑

/*
 * 1. 确定递归函数的参数和返回类型
 *   参数：需要二叉树的根节点，还需要一个计数器，这个计数器用来计算二叉树的一条边之和是否正好是目标和
 *   返回值：如果要搜索其中一条符合条件的路径，那么递归一定需要返回值，因为遇到符合条件的路径了就要及时返回。（本题的情况）
 *
 * 2. 确定终止条件
 *   让计数器targetSum初始为目标和，然后每次减去遍历路径节点上的数值。如果最后targetSum == 0，同时到了叶子节点的话，说明找到了目标和。
 *   如果遍历到了叶子节点，count不为0，就是没找到。
 *
 *
 * 3. 确定单层递归的逻辑
 *    通过递归函数判断现有node的左边是否存在满足的路径，如果递归函数返回true，说明找到了合适的路径，应该立刻返回。这里往下面继续遍历一条路径时也涉及到了回溯的使用。
 #    并且我们的递归函数没有处理空节点的条件句，所以应该避免将空节点加入
 */

var hasPathSum = function (root, targetSum) {
    if (root === null) return false;
    let result = helper(root, targetSum - root.val);
    return result;
};

function helper(node, targetSum) {
    //* 同样是到达叶子节点就到达了递归终止条件, 在这里检查是否找到了满足要求的一条路径
    if (node.left === null && node.right === null) {
        if (targetSum === 0) return true;
        else return false;
    }
    if (node.left) {
        targetSum -= node.left.val; //> 递归，处理节点;
        let leftRes = helper(node.left, targetSum);
        if (leftRes) return true;
        targetSum += node.left.val; //> 回溯，撤销处理结果
    }

    if (node.right) {
        targetSum -= node.right.val; //> 递归，处理节点;
        let rightRes = helper(node.right, targetSum);
        if (rightRes) return true;
        targetSum += node.right.val; //> 回溯，撤销处理结果
    }

    return false;
}
