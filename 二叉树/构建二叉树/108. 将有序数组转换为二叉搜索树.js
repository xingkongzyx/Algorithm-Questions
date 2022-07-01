/* 
//! 前序遍历 同最小高度树


? 链接：https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/solution/by-nehzil-t9v2/
? https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/solution/tu-jie-er-cha-sou-suo-shu-gou-zao-di-gui-python-go/
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
