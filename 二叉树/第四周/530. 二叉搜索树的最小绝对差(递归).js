//> 为什么使用中序遍历(超级重要)

//* https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/solution/shou-hua-tu-jie-530-er-cha-sou-suo-shu-de-zui-xiao/
/* 
? 中序遍历，它对于每一个节点，都先访问处理它的左子树中的节点，再访问处理它本身，再访问处理它的右子树中的节点。
! 由于二叉搜索树的性质，中序遍历访问处理的节点值的大小是递增的。
> 题目要求任意两个节点的最小的差值，它肯定发生在递增排列后的相邻的节点值之间。
? 
? 我们用一个变量，保存上一个访问处理的节点值，求出当前访问的节点值与它之差，挑战最小的纪录，更小就更新。
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
