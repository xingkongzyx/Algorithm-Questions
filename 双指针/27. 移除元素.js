var removeElement = function (nums, val) {
    let slow = 0;
    let fast = 0;
    while (fast < nums.length) {
        if (nums[fast] === val) {
            fast++;
        } else {
            nums[slow] = nums[fast];
            slow++;
            fast++;
        }
    }
    return slow;
};
