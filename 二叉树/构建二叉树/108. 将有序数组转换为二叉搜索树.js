/* 
//! 前序遍历 同最小高度树

? 非常好的链接: https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/solution/tu-jie-er-cha-sou-suo-shu-gou-zao-di-gui-python-go/

 
/ 递归函数的意义是 用有序数组 [startIdx, endIdx] 左闭右闭区间内的节点构造子树，并返回根节点
/ 单层递归的逻辑：
/ 在有序数组 [startIdx, endIdx] 范围内选取要构造关系的中心节点并创建它作为该子树的根节点
/ 调用该函数递归构造该节点的左子树
/ 调用该函数递归构造该节点的右子树

/ 数组中的元素都使用1次，时间复杂度为O(n).
/ 递归使用栈辅助空间，空间复杂度O(log(n)).
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
