function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

var constructMaximumBinaryTree = function (nums) {
    const map = {};

    for (let i = 0; i < nums.length; i++) {
        map[nums[i]] = i;
    }

    function buildTree(nums, startIdx, endIdx) {
        if (startIdx > endIdx) {
            return null;
        }

        let maxVal = -1;
        for (let i = startIdx; i <= endIdx; i++) {
            maxVal = Math.max(maxVal, nums[i]);
        }
        let root = new TreeNode(maxVal);
        let maxValIdx = map[maxVal];

        let leftTreeStartIdx = startIdx;
        let leftTreeEndIdx = maxValIdx - 1;
        let rightTreeStartIdx = maxValIdx + 1;
        let rightTreeEndIdx = endIdx;

        root.left = buildTree(nums, leftTreeStartIdx, leftTreeEndIdx);
        root.right = buildTree(
            nums,
            rightTreeStartIdx,
            rightTreeEndIdx
        );

        return root;
    }

    let root = buildTree(nums, 0, nums.length - 1);
    return root;
};

const nums = [3, 2, 1, 6, 0, 5];
let root = constructMaximumBinaryTree(nums);
console.log(root.val);
