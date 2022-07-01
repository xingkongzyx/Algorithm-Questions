/* 
* 开启 while 循环，当 root 为 null 时就结束循环（root 就是一个指针）。
*   - 如果 p.val、q.val 都小于 root.val，它们都在 root 的左子树，root=root.left，遍历到 root 的左子节点。
*   - 如果 p.val、q.val 都大于 root.val，它们都在 root 的右子树，root=root.right，遍历到 root 的右子节点。
*   - 其他情况，当前的 root 就是最近公共祖先，返回 root，结束遍历

链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/di-gui-he-die-dai-fa-by-hyj8/
*/

var lowestCommonAncestor = function (root, p, q) {
    while (root !== null) {
        if (root.val > p.val && root.val > q.val) root = root.left;
        else if (root.val < p.val && root.val < q.val)
            root = root.right;
        else return root;
    }
};
