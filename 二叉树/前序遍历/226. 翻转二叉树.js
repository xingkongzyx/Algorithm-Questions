/* 
/ 时间复杂度：O(N)，其中 N 为二叉树节点的数目。我们会遍历二叉树中的每一个节点，对每个节点而言，我们在常数时间内交换其两棵子树。

/ 空间复杂度：O(N)。使用的空间由递归栈的深度决定，它等于当前节点在二叉树中的高度。在平均情况下，二叉树的高度与节点个数为对数关系，即 O(logN)。而在最坏情况下，树形成链状，空间复杂度为 O(N)。
*/

var invertTreeRecursive = function (root) {
    if (root === null) return root;
    //# 中
    [root.left, root.right] = [root.right, root.left];
    //# 左
    invertTree(root.left);
    //# 右
    invertTree(root.right);
    return root;
};

//* 迭代的写法
var invertTree = function (root) {
    let queue = [];
    if (root !== null) queue.push(root);
    while (queue.length > 0) {
        let poppedNode = queue.shift();
        [poppedNode.left, poppedNode.right] = [
            poppedNode.right,
            poppedNode.left,
        ];
        if (poppedNode.left) queue.push(poppedNode.left);
        if (poppedNode.right) queue.push(poppedNode.right);
    }
    return root;
};
