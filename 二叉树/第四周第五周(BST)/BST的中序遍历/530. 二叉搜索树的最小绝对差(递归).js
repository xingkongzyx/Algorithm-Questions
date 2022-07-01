/* 
> 为什么使用中序遍历(超级重要)

? https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/solution/shou-hua-tu-jie-530-er-cha-sou-suo-shu-de-zui-xiao/

# 中序遍历，它对于每一个节点，都先访问处理它的左子树中的节点，再访问处理它本身，再访问处理它的右子树中的节点。
! 由于二叉搜索树的性质，中序遍历访问处理的节点值的大小是递增的。题目要求任意两个节点的最小的差值，它肯定发生在递增排列后的相邻的节点值之间。

* 我们用一个变量，保存上一个访问处理的节点值，求出当前访问的节点值与它之差，挑战最小的纪录，更小就更新。

* 1. 确定递归函数的参数和返回值
*  递归函数的参数传入的就是根节点, 不需要返回值。递归函数的用处就是在以当前 node 为根节点的路径中更新『绝对差』，并记录最小的

* 2. 确定终止条件
* ✔️ 当当前节点为空时, 表示这个节点已经是叶子节点, 这个节点没有子节点, 停止继续递归

* 3. 确定单层递归的逻辑
* 在『中序遍历』访问处理当前节点的时候，首先确保 prevNode 指针不为空，如果不为空的话则将 prevNode.val 与 node.val 求差，并将当前的『绝对差』与 result 进行比较看看是否更新 result. 
*/
var getMinimumDifference = function (root) {
    let prevNode = null;
    let result = Infinity;

    let inOrderTraversal = function (node) {
        if (node === null) return;
        //> 左
        inOrderTraversal(node.left);

        //> 中
        if (prevNode !== null) {
            result = Math.min(
                result,
                Math.abs(node.val - prevNode.val)
            );
        }
        prevNode = node;

        //> 右
        inOrderTraversal(node.right);
    };

    inOrderTraversal(root);
    return result;
};
