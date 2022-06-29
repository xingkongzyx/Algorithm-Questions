/* 
? 题目: https://leetcode.cn/problems/minimum-height-tree-lcci/ 
? 解析: https://leetcode.cn/problems/minimum-height-tree-lcci/solution/by-nehzil-mj6r/
* 构造最小高度树的思路: 选取中间位置的数赋给根节点，然后前一半递归构建左子树，后一半递归构建右子树。
/ 数组中的元素都使用1次，时间复杂度为O(n).
/ 递归使用栈辅助空间，空间复杂度O(log(n)).

*/
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}
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
