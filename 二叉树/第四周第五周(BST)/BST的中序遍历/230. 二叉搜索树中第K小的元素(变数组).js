/* 
/ 时间复杂度：O(N)，因为每个节点只访问了一次；
/ 空间复杂度：O(N)，因为需要数组保存二叉树的每个节点值。
*/
var kthSmallest = function (root, k) {
    let arr = [];
    function inorder(node) {
        if (node === null) return;
        inorder(node.left);
        arr.push(node.val);
        inorder(node.right);
    }
    inorder(root);
    return arr[k - 1];
};
