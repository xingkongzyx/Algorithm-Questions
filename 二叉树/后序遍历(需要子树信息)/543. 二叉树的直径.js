//> 543, 687, 124 为同一类型

/* 
//! 后序遍历 值得再看

* 二叉树的「直径」或者说「路径长度的最大值」不一定包含根节点 root, 但是一定是：经过树中某一个节点, 该节点左右子树的最大高度之和, 于是, 可以使用 DFS, 找出所有节点的最大直径, 在取出最大值 ans;
* 定义一个全局变量 ans, 用来记录最大直径 使用 dfs(node) 遍历所有的节点, dfs(node) 的作用是：找出以 node 为根节点的二叉树的最大高度
? https://leetcode.cn/problems/diameter-of-binary-tree/solutions/141166/java-shen-du-you-xian-bian-li-dfs-by-sugar-31/
? https://leetcode.cn/problems/diameter-of-binary-tree/solutions/141445/liang-chong-si-lu-shi-yong-quan-ju-bian-liang-yu-b/?orderBy=most_votes 



/ 时间复杂度：O(n) n为二叉树的节点 遍历n
/ 空间复杂度：O(Height) 常数变量 递归的深度为二叉树的高度
*/

var diameterOfBinaryTree = function (root) {
    //* 设置全局变量 ans, 用来记录「二叉树的最长路径」
    let ans = 0;

    /// traverse 函数的作用是：找出以 node 为根节点的二叉树的最大高度(注意这里是从下到上求高度!)
    //! 下面的代码与求解『104. 二叉树的最大深度』几乎是一样的, 唯一的不同就是在每个节点都更新 ans 用于记录到目前为止「二叉树的最长路径」
    function traverse(node) {
        if (node === null) return 0;

        let leftHeight = traverse(node.left);
        let rightHeight = traverse(node.right);

        //* 通过分别递归左右子树, 求得了左子树高度 以及 右子树高度, 从而可以更新二叉树的最长路径(等于左右子树的高度之和)
        //# 每个结点都要去判断「左子树 + 右子树的高度之和」是否大于记录到目前为止的「二叉树的最长路径 ans」, 并更新最大值
        ans = Math.max(ans, leftHeight + rightHeight);

        return Math.max(leftHeight, rightHeight) + 1;
    }
    traverse(root);

    return ans;
};
