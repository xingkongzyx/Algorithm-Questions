//! 前序遍历
/*
 # 这道题是从上向下查找目标区间, 遇到目标区间内的节点, 直接返回。而不需要像 236 那样使用后序遍历, 需要遍历整棵树并且有处理左右两棵子树递归的结果的代码逻辑
 * 递归函数的意义, 在「以 root 为根节点的子树」中寻找 p 节点和 q 节点的『最近公共祖先』, 或者说寻找一个节点 targetNode 使得 p、q节点 既不「同时大于」 targetNode, 也不「同时小于」 targetNode, 这里面就包含了等于的情况, 则root就是 p、q 的『最近公共祖先』

/ 时间复杂度：O(n)，其中 n 是给定的二叉搜索树中的节点个数。上述代码需要的时间与节点 p 和 q 在树中的深度线性相关，而在最坏的情况下，树呈现链式结构，p 和 q 一个是树的唯一叶子结点，一个是该叶子结点的父节点，此时时间复杂度为 Θ(n)。

? lowest-common-ancestor-of-a-binary-search-tree/solution/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-26/
 */
var lowestCommonAncestor = function (root, p, q) {
    if (root === null) return null;

    //# 中
    //* 只要 p.val 和 q.val 不是都大于(小于) root.val, 即只要 p, q 不同处在 root 的一个子树, root 即为所求！
    if (
        (root.val >= p.val && root.val <= q.val) ||
        (root.val <= p.val && root.val >= q.val)
    )
        return root;

    //# 左
    //* 如果 p.val 和 q.val 都比 root.val 小, 则p、q肯定在 root 的左子树, 『最近公共祖先』肯定也在左子树。递归左子树并直接返回递归的结果就行！
    if (root.val > p.val && root.val > q.val) {
        return lowestCommonAncestor(root.left, p, q);
    }

    //# 右
    //* 如果 p.val 和 q.val 都比 root.val 大, 则p、q肯定在 root 的右子树。『最近公共祖先』肯定也在右子树。递归右子树并直接返回递归的结果就行！
    if (root.val < p.val && root.val < q.val) {
        return lowestCommonAncestor(root.right, p, q);
    }

    //* 上面『#中』后面的代码等价于下面的 return root, 只不过是前序遍历, 将对当前节点的处理逻辑放在『#左右』前面更加清晰, 因为前面已经有对当前节点的处理逻辑, 所以 return root 不会运行
    // return root;
};
