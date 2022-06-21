var fourSum = function (nums, target) {
    if (nums.length < 4) return [];
    nums.sort((a, b) => a - b);
    let result = [];
    for (let firstIdx = 0; firstIdx < nums.length - 2; firstIdx++) {
        // 注意 最难理解的两个判断之第一
        // * 如果下次遍历选择的firstidx对应的数与firstidx - 1对应的数一致，那么直接跳过，为什么呢？因为在对 firstIdx-1 进行枚举时我们已经得到了所有能够构成 target 的并且包含 nums[firstIdx-1] 结果数组. 所以如果对 nums[firstIdx] 再次进行枚举，能够够成target的结果数组还是一致的。
        // * 这里有一个问题 如果构成 target 我们既用到了 nums[firstIdx-1] 又用到了 nums[firstIdx]怎么理解呢？那么在 遍历到firstIdx-1时用到了它的后一个数才构成了target，现在到了firstIdx 没有了后一个数自然就不可能得到结果，我们进行continue也是正确的。
        // ! 下面的第二个判断也可以如此理解
        if (firstIdx > 0 && nums[firstIdx] === nums[firstIdx - 1])
            continue;
        let firstNum = nums[firstIdx];
        for (
            let secondIdx = firstIdx + 1;
            secondIdx < nums.length - 1;
            secondIdx++
        ) {
            let secondNum = nums[secondIdx];
            // 注意 最难理解的两个判断之第二
            if (
                secondIdx > firstIdx + 1 &&
                nums[secondIdx] === nums[secondIdx - 1]
            ) {
                continue;
            }
            let left = secondIdx + 1;
            let right = nums.length - 1;
            while (left < right) {
                let sum =
                    nums[left] + nums[right] + firstNum + secondNum;
                if (sum > target) right--;
                else if (sum < target) left++;
                else {
                    result.push([
                        firstNum,
                        secondNum,
                        nums[left],
                        nums[right],
                    ]);
                    while (
                        left < right &&
                        nums[left] === nums[left + 1]
                    )
                        left++;
                    while (
                        left < right &&
                        nums[right] === nums[right - 1]
                    )
                        right--;

                    left++;
                    right--;
                }
            }
        }
    }
    return result;
};
let nums = [-2, -1, -1, 1, 1, 2, 2];
// -2 -1 -1 1 1 2 2
let target = 0;

console.log(fourSum(nums, target));
