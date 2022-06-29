/* 
//! 同最小高度树
* 根据本题目的两个关键字：有序 & 二叉搜索树
* 可知：希望你通过中序遍历构造BST
* 众所周知：中序遍历不能完整的确认一颗树，因为每个节点都可以是根结点
* 
* 但题目要求期望BST是平衡的，那么，我们每次都讲中间的节点作为根结点即可（但依旧不唯一，这点题目也接受可以不唯一）

? 链接：https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/solution/you-xu-shu-zu-zhuan-hua-by-yang-zi-37-011g/
*/

var sortedArrayToBST = function (nums) {
    function buildTree(nums, startIdx, endIdx) {
        //* 终止条件: startIdx > endIdx 表示子数组为空
        if (startIdx > endIdx) return null;

        //* 找到中间的值
        let midIdx = Math.floor((startIdx + endIdx) / 2);
        let midVal = nums[midIdx];
        let root = new TreeNode(midVal);

        //* 左子数组[startIdx, midIdx - 1]构建左子树
        root.left = buildTree(nums, startIdx, midIdx - 1);

        //* 右子数组[midIdx + 1, endIdx]构建左子树
        root.right = buildTree(nums, midIdx + 1, endIdx);

        return root;
    }

    return buildTree(nums, 0, nums.length - 1);
};
