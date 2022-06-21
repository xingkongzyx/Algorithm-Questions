// 时间复杂度：同样每个节点都需要入队列/出队列一次，所以是 O(n)O(n)
// 空间复杂度：最坏的情况下会包含所有的叶子节点，完全二叉树叶子节点是 n/2个，所以时间复杂度是 0(n)0(n)

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
// ! 前序遍历
// 使用recursive的解法 O(N) time->因为遍历了树中的每一个node, O(d) space, d is the depth of the tree
var invertTreeRecursive = function (root) {
    if (root === null) return root;
    [root.left, root.right] = [root.right, root.left];
    invertTree(root.left);
    invertTree(root.right);
    return root;
};
