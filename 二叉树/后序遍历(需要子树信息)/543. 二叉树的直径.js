//> 543, 687, 124 为同一类型

/* 
//! 后序遍历 值得再看
? https://leetcode.cn/problems/diameter-of-binary-tree/solution/javascriptshen-du-you-xian-bian-li-dfs-guan-fang-t/
? 分析借鉴 https://leetcode.cn/problems/diameter-of-binary-tree/solution/er-cha-shu-de-zhi-jing-by-leetcode-solution/

> 最大的直径不一定是经过根节点的,可能最大的直径出现在子树中
* 最大的直径有三种可能性:
* ➊ 不穿过根节点，在左子树中
* ➋ 不穿过根节点，在右子树中
* ➌ 穿过根节点，相当于 左子树 + 右子树 + 根节点

! 注意一点: 二叉树的「直径」或者说「路径长度的最大值」或者说「最长的一条路径经过的节点数」不一定包含根节点 root，但是一定是：经过树中某一个节点，
* 该节点的左右子树的最大高度之和 + 1, 〚左右子树的最大高度之和〛也就是「左右子节点」向下遍历经过最多的节点数之和, 这里包含了左右两个子节点的节点数。+1 则代表当前节点本身的节点数。加在一起的结果就是「最长的一条路径经过的节点数」。根据前面分析,「路径长度的最大值」为「最长的一条路径经过的节点数」-1。所以最后 ans - 1 即为所求

/ 时间复杂度：O(n) n为二叉树的节点 遍历n
/ 空间复杂度：O(Height) 常数变量 递归的深度为二叉树的高度
*/

var diameterOfBinaryTree = function (root) {
    //* 设置全局变量 ans，用来记录「路径经过节点数的最大值」
    let ans = 0;

    /// traverse 函数的作用是：找出以 root 为根节点的二叉树的最大高度(注意这里是从下到上求高度!)
    //! 下面的代码与求解『104. 二叉树的最大深度』几乎是一样的，唯一的不同就是在每个节点都更新 ans 用于记录到目前为止「路径经过节点数的最大值」
    function traverse(node) {
        if (node === null) return 0;

        let leftHeight = traverse(node.left);
        let rightHeight = traverse(node.right);

        //* 通过分别递归左右子树, 求得了左子树高度(左儿子向下遍历经过最多的节点数) 以及 右子树高度(右儿子向下遍历经过最多的节点数)，从而可以更新路径经过节点数的最大值(注意这里要 + 1)
        ans = Math.max(ans, leftHeight + rightHeight + 1);

        return Math.max(leftHeight, rightHeight) + 1;
    }
    traverse(root);

    //> 最大直径 == 路径的长度的最大值 == 该最长路径经过的节点数 - 1
    return ans - 1;
};
