/*
我们可以将该问题形式化地描述为：给定若干个数字，将其组合为一个整数。如何将这些数字重新排列，以得到下一个更大的整数。如 123 下一个更大的数为 132。如果没有更大的整数，则输出最小的整数。

? https://leetcode.cn/problems/next-permutation/

/ 时间复杂度：O(N)，其中 N 为给定序列的长度。我们至多只需要扫描两次序列，以及进行一次反转操作。
/ 空间复杂度：O(1)，只需要常数的空间存放若干变量。

? https://leetcode.cn/problems/next-permutation/
*/
var nextPermutation = function (nums) {
    let length = nums.length;

    let smallNumPointer = length - 2;

    // 首先从后向前查找第一个顺序对 (smallNumPointer, smallNumPointer+1)，满足 a[smallNumPointer] < a[smallNumPointer + 1]。这样「较小数」即为 a[smallNumPointer]。此时 [smallNumPointer + 1, length) 必然是下降序列。

    while (
        smallNumPointer >= 0 &&
        nums[smallNumPointer] >= nums[smallNumPointer + 1]
    ) {
        smallNumPointer--;
    }

    if (smallNumPointer === -1) {
        reverse(0, length - 1, nums);
        return;
    }

    let bigNumPointer = length - 1;
    // 如果找到了顺序对，那么在区间 [smallNumPointer + 1,length) 中从后向前查找第一个元素 bigNumPointer 满足 a[smallNumPointer] < a[bigNumPointer]。这样「较大数」即为 a[bigNumPointer]。
    while (
        bigNumPointer > smallNumPointer &&
        nums[bigNumPointer] <= nums[smallNumPointer]
    ) {
        bigNumPointer--;
    }

    // 交换 a[smallNumPointer] 与 a[bigNumPointer]，此时可以证明区间 [smallNumPointer + 1,length) 必为降序。我们可以直接使用双指针反转区间 [smallNumPointer + 1, length) 使其变为升序，而无需对该区间进行排序。
    swap(smallNumPointer, bigNumPointer, nums);
    reverse(smallNumPointer + 1, length - 1, nums);
};

var swap = function (idx1, idx2, nums) {
    let temp = nums[idx1];
    nums[idx1] = nums[idx2];
    nums[idx2] = temp;
};

var reverse = function (left, right, nums) {
    while (left < right) {
        swap(left, right, nums);
        left++;
        right--;
    }
};
