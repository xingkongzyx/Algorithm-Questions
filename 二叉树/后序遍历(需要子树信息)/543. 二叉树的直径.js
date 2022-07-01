/* 
//! 后序遍历 值得再看
? https://leetcode.cn/problems/diameter-of-binary-tree/solution/liang-chong-si-lu-shi-yong-quan-ju-bian-liang-yu-b/
? https://leetcode.cn/problems/diameter-of-binary-tree/solution/java-shen-du-you-xian-bian-li-dfs-by-sugar-31/
> 最大的直径不一定是经过根节点的,可能最大的直径出现在子树中
二叉树直径实际上就是二叉树中的最长路径,我们是可以划分出子问题的：
二叉树的最长路径 = max{左子树的最长路径, 右子树的最长路径, 经过根结点的最长路径}

最大的直径有三种可能性:
1. 不穿过根节点，在左子树中
2. 不穿过根节点，在右子树中
3. 穿过根节点，相当于 左子树 + 右子树 + 根节点
时间复杂度：O(n) n为二叉树的节点 遍历n
空间复杂度：O(Height) 常数变量 递归的深度为二叉树的高度

*/

var diameterOfBinaryTree = function (root) {
    //* ans 用来记录以某个节点为根节点的时候，最大的路径
    let ans = 0;

    /// traverse 函数的作用是：找出以 root 为根节点的二叉树的最大深度
    function traverse(node) {
        if (node === null) return 0;

        let leftDepth = traverse(node.left);
        let rightDepth = traverse(node.right);
        ans = Math.max(ans, leftDepth + 1 + rightDepth);

        return Math.max(leftDepth, rightDepth) + 1;
    }
    traverse(root);

    //* 两结点之间的路径长度是以它们之间「边的数目」表示，而 ans 计算出的是最长路径经过的节点的数目，边的数目 = 经过的节点的数目 - 1
    return ans - 1;
};
