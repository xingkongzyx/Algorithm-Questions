/*
//! 前序遍历
? 代码参考 https://leetcode.cn/problems/trim-a-binary-search-tree/solution/marveljian-dan-de-xue-xi-bi-ji-669-by-tyanyonecanc/

/ 时间复杂度：O(n), 最坏情况下每个节点都需要访问一次
/ 空间复杂度：O(n), 在最糟糕的情况下, 我们递归调用的栈可能与节点数一样大。

* 1.确定递归函数的参数以及返回值
* 函数作用: 在「以 root 为根节点的二叉树」中删除不在 [low, high] 范围内的所有节点并返回修剪好的「二叉搜索树」的新的根节点 
* 输入: 「二叉搜索树」的根节点 root 和最小边界low 和最大边界 high
* 输出: 修剪好的「二叉搜索树」的新的根节点 

* 2 确定终止条件.
* 遇到空节点返回

* 3. 确定单层递归的逻辑
* 总: 判断根节点是否在范围内, 如果在则判断 左节点, 判断 右节点
* 1) 如果「当前节点」小于 low, 那么应该递归修剪右子树, 并将右子树经过修剪后的新的根节点返回
* 2) 如果「当前节点」大于 high, 那么应该递归修剪左子树, 并将左子树经过修剪后的新的根节点返回
* 3) 最后, 如果根节点没有问题, 则要递归地修剪左子结点和右子结点并返回修剪后的结果给根节点
* 4) 最后返回root节点
*/

var trimBST = function (root, low, high) {
    if (root === null) return null;

    //# 中 判断根节点是否在范围内
    //* 如果根结点太小, 又因为是「二叉搜索树」. 所以根结点的左子树的所有结点只会更小, 说明根结点及其左子树都应该剪掉, 结合递归函数输出的定义, 因此直接返回『右子树的修剪结果』。
    if (root.val < low) {
        return trimBST(root.right, low, high);
    }

    //* 如果根结点太大, 又因为是「二叉搜索树」. 所以根结点的右子树的所有结点只会更大, 说明根结点及其右子树都应该剪掉, 结合递归函数输出的定义, 因此直接返回『左子树的修剪结果』。
    if (root.val > high) {
        return trimBST(root.left, low, high);
    }

    //* 如果根结点没问题, 则递归地修剪左子结点和右子结点并返回修剪后的结果给根节点
    //# 左
    root.left = trimBST(root.left, low, high);
    //# 右
    root.right = trimBST(root.right, low, high);

    return root;
};
