/*
# 我们记录上一个遍历节点的值，对当前节点的处理策略就是比较当前节点值和上一个节点值，前者大于后者即为满足条件。
https://leetcode.cn/problems/validate-binary-search-tree/solutions/232885/zhong-xu-bian-li-qing-song-na-xia-bi-xu-miao-dong-/
https://leetcode.cn/problems/validate-binary-search-tree/solutions/2501570/javapython3czhong-xu-bian-li-pan-duan-sh-enhd/
*/
var isValidBST = function (root) {
    // 用于记录中序遍历过程中的前一个值
    let preVal = null;

    // 递归函数意义: 判断以当前节点为根节点的树是否为 BST
    function dfs(node) {
        if (node === null) return true;
        // 判断以当前节点为根节点的左子树是否为BST，不属于的话直接返回
        let leftRes = dfs(node.left);
        if (!leftRes) return false;

        // 针对当前节点进行检查，必须要大于它前一个被遍历到的值
        let curNodeCheck = true;
        if (preVal !== null) {
            curNodeCheck = preVal < node.val;
            preVal = node.val;
        } else {
            preVal = node.val;
        }
        if (!curNodeCheck) return false;

        // 判断以当前节点为根节点的右子树是否为BST，不属于的话直接返回
        let rightRes = dfs(node.right);

        return rightRes;
    }

    return dfs(root);
};
