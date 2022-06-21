var sortedSquares = function (nums) {
    let result = new Array(nums.length);
    let start = 0;
    let end = nums.length - 1;
    // 因为是非递减顺序 排序的整数数组 nums，有正数有负数，所以平方后的排序就是第一个数和最后一个数平方结果的比较。然后根据比较结果调整指针
    for (let p = nums.length - 1; p >= 0; p--) {
        if (nums[start] * nums[start] > nums[end] * nums[end]) {
            result[p] = nums[start] * nums[start];
            start += 1;
        } else {
            result[p] = nums[end] * nums[end];
            end -= 1;
        }
    }
    return result;
};
