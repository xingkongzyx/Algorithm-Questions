var findLengthOfLCIS = function (nums) {
    let res = 1;
    let count = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            count++;
        } else {
            count = 1;
        }
        res = Math.max(res, count);
    }
    return res;
};
