/* 
! 注意类似用数组构造二叉树的题目，每次分隔尽量不要定义新的数组，而是通过下标索引直接在原数组上操作，这样可以节约时间和空间上的开销。
* 递归的方法只需按照题意模拟即可
* 
* 1. 二叉树的根是数组 nums 中的最大元素。
* 2. 左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
* 3. 右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
* 
> 区间方面使用的是左闭右闭的区间

? 时间复杂度：O(n^2)，最坏情况是数组单调有序，那么每次查找都需要O(n)，递归深度O(n)
? 空间复杂度：O(n)，数组单调有序递归深度会达到O(n)
*/

var constructMaximumBinaryTree = function (nums) {
    let root = buildTreeHelper(nums, 0, nums.length - 1);
    return root;
};

function buildTreeHelper(nums, startIdx, endIdx) {
    if (startIdx > endIdx) return null;
    let maxVal = nums[startIdx];
    let maxIdx = startIdx;
    for (let i = startIdx; i <= endIdx; i++) {
        if (nums[i] > maxVal) {
            maxVal = nums[i];
            maxIdx = i;
        }
    }

    let rootNode = new TreeNode(maxVal);
    rootNode.left = buildTreeHelper(nums, startIdx, maxIdx - 1);
    rootNode.right = buildTreeHelper(nums, maxIdx + 1, endIdx);
    return rootNode;
}
