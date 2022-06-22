// ! 相当于 threeSum 的无缝拓展衔接
var fourSum = function (nums, target) {
    if (nums.length < 4) return [];

    nums.sort((a, b) => a - b);
    let res = [];

    for (let i = 0; i <= nums.length - 4; i++) {
        //* 注意：[-6, -5, -2, 0, 0, 1, 5] target = -11 中，如果加上下面两个注释的判断语句。-6 > -11 直接退出循环，但由于target是负数，即使-6大于-11，但后面的 -5，0，0加在一起还能凑出 -11 所以不能通过这个判断语句就跳出循环

        //! 注意: 为什么注释?  if (nums[i] > target) break;
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        for (let j = i + 1; j <= nums.length - 3; j++) {
            //! 注意: 为什么注释?  if (nums[j] > target - nums[i]) break;
            if (j > i + 1 && nums[j] === nums[j - 1]) continue;

            let remain = target - nums[i] - nums[j];
            let left = j + 1;
            let right = nums.length - 1;
            while (left < right) {
                if (nums[left] + nums[right] < remain) left++;
                else if (nums[left] + nums[right] > remain) right--;
                else if (nums[left] + nums[right] === remain) {
                    res.push([
                        nums[i],
                        nums[j],
                        nums[left],
                        nums[right],
                    ]);
                    while (nums[left] === nums[left + 1]) {
                        left++;
                    }
                    while (nums[right] === nums[right - 1]) {
                        right--;
                    }
                    left++;
                    right--;
                }
            }
        }
    }

    return res;
};
fourSum([2, 2, 2, 2, 2], 8);
