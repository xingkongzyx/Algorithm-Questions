var threeSum = function (nums) {
    nums.sort((a, b) => a - b);
    let res = [];
    // # special case: nums中根本没有三个elements
    if (nums.length < 3) return res;
    // # 同样到最后需要遍历的element就是倒数第三个元素，后面的element已经凑不齐三个数字了
    for (let i = 0; i <= nums.length - 3; i++) {
        // # special case: 如果三个数中的第一个数已经大于0，则不可能满足要求(因为数组正序排列)，直接退出循环
        if (nums[i] > 0) break;
        // # special case: 当前的 nums[i] 与前一个element相同，我们得到了前面的数字的所有满足要求的组合自然也就囊括了现在的 nums[i] 所有的组合，直接跳过
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let left = i + 1;
        let right = nums.length - 1;
        let remain = 0 - nums[i];
        while (left < right) {
            if (nums[left] + nums[right] < remain) {
                left++;
            } else if (nums[left] + nums[right] > remain) {
                right--;
            } else if (nums[left] + nums[right] == remain) {
                res.push([nums[i], nums[left], nums[right]]);
                while (nums[left] === nums[left + 1]) {
                    left++;
                }
                while (nums[right] === nums[right - 1]) {
                    right--;
                }
                //# 如果上述两个while loop都没进入的话就正常更新 left && right pointers. 如果进入的话 他们都到达了相等的最后一个元素. 像下面的left从 index 0 最后到达了最后一个1所在的位置，然后再使用下面的更新语句对pointers进行更新
                //# [1,  1,  1,    2]
                //# [0,  1,  left, right]
                left++;
                right--;
            }
        }
    }
    return res;
};
