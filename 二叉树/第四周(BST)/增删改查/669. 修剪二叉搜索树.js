/* 
> 思考过程：对于二叉数的递归，我们只要想清楚当前的root需要干什么就行！
? 如果当前的root太小，当前的root的左子树的所有结点只会更小，说明当前的root及其左子树都应该剪掉，因此直接返回右子树的修剪结果。
? 如果当前的root太大，当前的root的右子树的所有结点只会更大，说明当前的root及其右子树都应该剪掉，因此直接返回左子树的修剪结果。
? 如果当前的root没问题，则递归地修剪左子结点和右子结点。
? 如果结点为空，说明无需修剪，直接返回空即可。
? 左右子结点都修剪完后，返回自身作为修剪结果。

# 时间复杂度：O(n), 最坏情况下每个节点都需要访问一次
# 空间复杂度：O(n), 在最糟糕的情况下，我们递归调用的栈可能与节点数一样大。
*/

/*
 * 1.确定递归函数的参数以及返回值
 * 需要返回值，返回一个区间调整完以后的subtree，同时通过递归函数的返回值来移除节点。
 
 * 2 确定终止条件.
 * 修剪的操作并不是在终止条件上进行的，所以就是遇到空节点返回就可以了。
 
 * 3. 确定单层递归的逻辑
 * 1) 如果root（当前节点）的元素小于low的数值，那么应该递归右子树，并返回右子树符合条件的头结点。
 * 2) 如果root(当前节点)的元素大于high的，那么应该递归左子树，并返回左子树符合条件的头结点。
 * 3) 接下来要将下一层处理完左子树的结果赋给root->left，处理完右子树的结果赋给root->right。
 * 4) 最后返回root节点
 */
var trimBST = function (root, low, high) {
    if (root === null) return null;

    if (root.val > high) {
        let leftSubTree = trimBST(root.left, low, high);
        return leftSubTree;
    }

    if (root.val < low) {
        let rightSubTree = trimBST(root.right, low, high);
        return rightSubTree;
    }

    root.left = trimBST(root.left, low, high);
    root.right = trimBST(root.right, low, high);

    return root;
};
