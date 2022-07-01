/* 
# 与下面题目是同类型的
106.从中序与后序遍历序列构造二叉树(opens new window)
654.最大二叉树 (opens new window)中其实已经讲过了，如果根据数组构造一棵二叉树。
701.二叉搜索树中的插入操作(opens new window)
450.删除二叉搜索树中的节点 
*/
var sortedArrayToBST = function (nums) {
    let buildTreeHelper = function (nums, left, right) {
        if (left > right) return null;
        let mid = Math.floor((left + right) / 2);

        let node = new TreeNode(nums[mid]);
        node.right = buildTreeHelper(nums, mid + 1, right);
        node.left = buildTreeHelper(nums, left, mid - 1);
        return node;
    };

    let root = buildTreeHelper(nums, 0, nums.length - 1);
    return root;
};
