//> 113.路径总和ii要遍历整个树，找到所有路径，所以递归函数不要返回值！

var pathSum = function (root, targetSum) {
    let totalPaths = [];
    if (root === null) return totalPaths;
    let currentPath = [root.val];
    helper(root, targetSum - root.val, currentPath, totalPaths);
    return totalPaths;
};

function helper(node, sum, currentPath, totalPaths) {
    //# 到达了叶子节点，并且当前记录的sum正好满足条件
    if (node.left === null && node.right === null) {
        if (sum === 0) {
            //! 将栈中的节点拷贝一份，推入返回结构res中
            //! 若不拷贝的话，推入的是引用，currentPath改变，totalPaths里的currentPath也会改变
            totalPaths.push([...currentPath]);
        }
        return;
    }
    //# 如果存在左节点，继续遍历左子树
    if (node.left) {
        currentPath.push(node.left.val);
        sum -= node.left.val;
        helper(node.left, sum, currentPath, totalPaths);
        //# 向上回溯, currentPath弹出一个节点, sum回到原来的value
        currentPath.pop();
        sum += node.left.val;
    }
    //# 如果存在右节点，继续遍历右子树
    if (node.right) {
        currentPath.push(node.right.val);
        sum -= node.right.val;
        helper(node.right, sum, currentPath, totalPaths);
        //# 向上回溯, currentPath弹出一个节点, sum回到原来的value
        currentPath.pop();
        sum += node.right.val;
    }
    return;
}
