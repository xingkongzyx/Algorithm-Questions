// > 本题我们要找一条符合条件的路径, 类似于回溯问题，for 循环在这里变成了遍历左右两个子树，递归代表着回溯树中继续向下走
// ! 可以使用深度优先遍历的方式来遍历二叉树.
// ! 本题前中后序遍历都可以, 因为中节点也没有处理逻辑

/*
 * 1. 递归函数的参数和返回类型
*    含义: 判断当前节点所在的路径的节点的和是否满足目标和  
 *   参数: 需要二叉树的根节点, 还需要一个计数器, 这个计数器用来计算二叉树的一条边之和是否正好是目标和
 *   返回值: 满足与否(True / False)
 * 2. 确定终止条件
 *   到达叶子节点时即抵达处于终止条件, 此时检查 targetSum 是否等于 0
 *
 * 3. 确定单层递归的逻辑
 *    通过递归函数判断现有node的左边是否存在满足的路径, 如果递归函数返回true, 说明找到了合适的路径, 应该立刻返回。然后再以同样的思路判断右边
    
 # 递归函数是到达叶子节点时终止继续递归, 没有处理空节点的条件句, 所以应该避免将空节点加入
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
        targetSum -= node.left.val; //> 递归, 处理节点;
        let leftRes = helper(node.left, targetSum);
        if (leftRes) return true;
        targetSum += node.left.val; //> 回溯, 撤销处理结果
    }

    if (node.right) {
        targetSum -= node.right.val; //> 递归, 处理节点;
        let rightRes = helper(node.right, targetSum);
        if (rightRes) return true;
        targetSum += node.right.val; //> 回溯, 撤销处理结果
    }

    return false;
}
