/* 
/ 时间复杂度：O(N)，N是二叉树的节点个数。
/ 空间复杂度：O(N)，无论是 BFS 还是 DFS 都需要额外的空间。
*/

var isUnivalTree = function (root) {
    //* 递归函数 helper 的作用是: 判断以 node 为根节点的二叉树是否是「单值二叉树」(满足其所有子节点都与传入的 val 相等)
    function helper(node, val) {
        if (node === null) {
            return true;
        }
        //# 中
        if (node.val !== val) {
            return false;
        }

        //# 左
        let leftCheck = helper(node.left, val);
        //# 右
        let rightCheck = helper(node.right, val);

        return leftCheck && rightCheck;
    }
    return helper(root, root.val);
};
