/* 
//! 反中序遍历
? https://leetcode.cn/problems/convert-bst-to-greater-tree/solution/shou-hua-tu-jie-zhong-xu-bian-li-fan-xiang-de-by-x/

# 这里又要用到递归了，递归的一个非常重要的点就是：不去管函数的内部细节是如何处理的，我们只看其函数作用以及输入与输出。对于函数 inOrder 来说：
* 函数作用：将以 root 为根节点的二叉树变为「累加树」, 从而使得每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。借助辅助变量 sum 来保存「比当前节点值大的所有节点值的和」。
* 输入：二叉搜索树的根节点
* 输出：无
* 遍历过程中需要将已经遍历的节点的值进行累加，然后再赋值给当前节点。
*/

const convertBST = (root) => {
    //* sum 用于 保存「比当前节点值大的所有节点值的和」。
    let sum = 0;
    const inOrder = (root) => {
        if (root == null) {
            //* 遍历到null节点，开始返回
            return;
        }
        //* 先进入右子树
        inOrder(root.right);

        //* 节点值累加给sum
        sum += root.val;
        //* 累加的结果，赋给root.val
        root.val = sum;
        //* 然后才进入左子树
        inOrder(root.left);
    };
    inOrder(root);
    return root;
};
