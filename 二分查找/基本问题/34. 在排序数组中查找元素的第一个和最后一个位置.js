/*
? https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solution/si-lu-hen-jian-dan-xi-jie-fei-mo-gui-de-er-fen-cha/945817

! 在普通二分查找的二分查找中，当 nums[mid] == target 时，直接返回 mid，
/ 而在本题查找左边界时，则是要继续向左查找。当 nums[mid] == target 时，继续查找mid左边是否还有和 target 相等的数组元素。继续收缩搜索区间, 也就是让 right = mid - 1。
/ 而在本题查找右边界时，则是要继续向右查找，当 nums[mid] == target 时，继续查找mid右边看是否还有和 target 相等的数组元素。继续收缩搜索区间, 也就是让 left = mid + 1
! 以上两种情况，如果存在target的话，最后左右指针一定重合，指向最左/最右的一个target。脑中模拟可以发现返回left/right便会分别对应题目求的左/右边界

*/

var searchRange = function (nums, target) {
    if (
        nums.length == 0 ||
        nums[0] > target ||
        nums[nums.length - 1] < target
    ) {
        return [-1, -1];
    }
    let leftBorder = leftBound(nums, target);
    let rightBorder = rightBound(nums, target);
    return [leftBorder, rightBorder];
};

var leftBound = function (nums, target) {
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        let mid = left + Math.floor((right - left) / 2);
        if (nums[mid] === target) {
            // 原来的二分搜索中找到了target就直接返回，但在寻找边界的二分搜索中要做的是继续向左寻找
            right = mid - 1;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        }
    }
    // 此时退出while loop的情况一定是 [right, left] right = left - 1
    // 因为最后一次循环 left===right===mid,
    // 1)如果找到了target right=mid-1 退出循环,
    // 2)没找到但是nums[mid]大于target, right = mid - 1 退出循环,
    // 3)没找到但是nums[mid]小于target, left = mid + 1 退出循环
    if (nums[left] !== target || left === nums.length) return -1;
    return left;
};

var rightBound = function (nums, target) {
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        let mid = left + Math.floor((right - left) / 2);
        if (nums[mid] === target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] < target) {
            left = mid + 1;
        }
    }
    if (right < 0 || nums[right] !== target) return -1;
    return right;
};
