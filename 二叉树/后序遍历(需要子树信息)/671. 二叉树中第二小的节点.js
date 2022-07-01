/* 
> 后序遍历(简单起见可以关注前序的解法)
* 关键结论: 二叉树根节点的值为所有节点中的最小值。同理，当前节点的左子节点的值是左子树中的最小值，右子节点的值是右子树中的最小值。注意当前如果左右子节点和根节点的值相同时，不能直接进行判断，因为左右子树中可能会存在第二小的值。此时，通过递归来找到解。如果当前节点的值和左子节点的值相同，那么递归的去找左子树中的第二小的节点；如果当前节点的值和右子节点的值相同，那么递归的去找右子树中的第二小的节点。

? 概念引用: https://leetcode.cn/problems/second-minimum-node-in-a-binary-tree/solution/cshuang-bai-jie-fa-by-dui-mian-de-er-ha-ni-kan-sha/
? 代码引用: https://leetcode.cn/problems/second-minimum-node-in-a-binary-tree/solution/ji-bai-liao-100de-javayong-hu-by-reedfan/284679


*/
/// 函数的作用就是输入一个二叉树的节点 node ，返回【以这个节点 node 为根节点的子树】中第二小的值
var findSecondMinimumValue = function (root) {
    //* 没有最小节点
    if (root == null || (root.left == null && root.right == null))
        return -1;

    //* 找出候选数，默认就是子节点值，如果子节点值和 root 值相同，递归，在子树中寻找候选数
    let left = root.left.val;
    let right = root.right.val;
    if (root.left.val == root.val)
        left = findSecondMinimumValue(root.left);
    if (root.right.val == root.val)
        right = findSecondMinimumValue(root.right);
    /* 
    / 什么时候 left == -1 ? root.left 为根节点的子树的节点值全部相同，且 root.left.val == root.val。那么自然这颗子树没有第二小的节点。
    / 什么时候 left != -1 ? root.left 为根节点的子树中有node.val【大于】root.val的节点，第一小的节点值root.val。
    / left是【以root.left为根节点的子树==左子树】中第二的值，该值【大于】root.val
    / right是【以root.right为根节点的子树==右子树】中最小的值，该值【大于】root.val
    / 在 left、right、root.val 三个值当中，root.val一定是最小的
    
    */
    //* 如果左右候选数都正常，返回较小值就可
    if (left != -1 && right != -1) {
        return Math.min(left, right);
    }
    //* 如果通过递归找到的候选数有 -1，说明那个子树中没有可供候选的数
    if (left != -1) {
        //* 左子树正常，答案就是左边的候选数
        return left;
    } else {
        //* 右子树正常，返回答案
        //* 或者右子树也没有候选数，返回-1，即right
        return right;
    }
};
