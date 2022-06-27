// 与 257 的最大区别就是 这里传入的 targetSum 是一个value，所以递归过程中如果没有像carl写法那样if 里面加 node.val 的话就不需要再递归后进行剑法。而257 操作的是一个 array，是个引用
//*  112 的 traversal, 也是前序遍历
function helper(node, targetSum) {
    targetSum -= node.val;
    res.push(node.val);
    if (node.left === null && node.right === null) {
        if (targetSum === 0) return true;
        else return false;
    }
    if (node.left) {
        console.log("before", targetSum);
        let leftRes = helper(node.left, targetSum);
        if (leftRes) return true;
        console.log("after", targetSum);
    }

    if (node.right) {
        let rightRes = helper(node.right, targetSum);
        if (rightRes) return true;
    }

    return false;
}

//* 257 的 traversal 也是前序遍历
function traversal(node, currentPath, totalPaths) {
    // 前序遍历中 先访问node元素
    currentPath.push(node.val);

    if (node.left === null && node.right === null) {
        let pathStr = currentPath.join("->");
        totalPaths.push(pathStr);
    }

    // 前序遍历中 对左子树进行递归
    if (node.left) {
        //# 回溯和递归是一一对应的，有一个递归，就要有一个回溯
        traversal(node.left, currentPath, totalPaths);
        currentPath.pop();
    }

    // 前序遍历中 对右子树进行递归
    if (node.right) {
        //# 回溯和递归是一一对应的，有一个递归，就要有一个回溯
        traversal(node.right, currentPath, totalPaths);
        currentPath.pop();
    }
}
