//> 543, 687, 124 为同一类型
/* 
? 化简递归的子问题的逻辑及推理过程: https://leetcode.cn/problems/binary-tree-maximum-path-sum/solution/chao-xiang-xi-hua-jian-di-gui-de-zi-wen-hyfai/

? 题目的示例来描述一下这个算法过程: https://leetcode.cn/problems/binary-tree-maximum-path-sum/solution/er-cha-shu-de-zui-da-lu-jing-he-zhu-yao-li-jie-ti-/

/ Time: O(n), 因为要遍历所有节点
/ Space: O(h) = O(n), 递归层数取决于树高h, 最坏情况是链表高为n。
*/
var maxPathSum = function (root) {
    let maxPath = -Infinity;
    /// 函数的作用是：找出以「node节点」为起点, 向下走的的单边分支最大和
    function helper(node) {
        if (node === null) return 0;

        /*
         * Q：左右孩子贡献为什么要大于等于0？
         * A: 因为在这种方法中计算从某一节点出发的最大路径和的时候，计算公式为： 当前节点值 + 左孩子贡献 + 右孩子贡献，
         *     而左右孩子贡献是「可选的」，也就是说当某一边贡献小于0的时候，我可以在计算路径和时不算这一边
         *     这种情况也就相当于其贡献为 0，但是注意路径和至少包含「当前节点的值」。
         * 在计算左右孩子贡献的时候，可以发现代码中限制了，左右孩子贡献至少为 0。为什么不能为负呢？最直接的解释就是，假设我有无数个可以选择的子路径，每个路径都有自己的贡献，为了让路径和最大，我最会选择贡献大于0的，不然我就不选，这里有一个很关键的点，并不是所有子路径都必须加上，完全可以一条路径不选，当前节点的值就可以作为从该节点出发的最大路径和。所以，当前节点的值不管正负一定得加上，但是孩子的贡献选择大于0的（不选的意思就是默认贡献为0）。
         */

        /// 找出以「node的左子节点」为起点, 向下走的最长路径和. 如果子问题返回的答案是负数, 那么加上当前节点的值只会变得更小, 所以是负数的话我们就用0来代替.
        let leftPath = Math.max(0, helper(node.left));
        /// 找出以「node的右子节点」为起点, 向下走的最长路径和. 如果子问题返回的答案是负数, 那么加上当前节点的值只会变得更小, 所以是负数的话我们就用0来代替.
        let rightPath = Math.max(0, helper(node.right));

        /*
         * 如图所示, 题目所说的二叉树中的最大路径的计算来源可以分为以下四种：
         * ➀ 我自己就是一条路径
         * ➁ 某个结点及其左子树组成路径的和
         * ➂ 某个结点及其右子树组成路径的和
         * ➃ 以自己为桥梁, 跟左、右子树合并成一条路径
         * 「leftPath + rightPath + node.val」就包含了上面的四种情况的最大值，用其和「已经储存的最大路和」进行对比从而记录最长的路径和
         ! 相比另一个解法来说，因为我们上面用 Math.max(0, ...) 来记录单边的分支最大和。所以这里只需要加一块就能代表上面四种情况的最大值
         */
        maxPath = Math.max(maxPath, leftPath + rightPath + node.val);

        /// 返回经过 node 的单边最大分支给当前 node 的父节点计算使用

        return Math.max(leftPath, rightPath) + node.val;
    }
    helper(root);
    return maxPath;
};
