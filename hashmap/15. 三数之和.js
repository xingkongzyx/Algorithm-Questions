// https://www.algoexpert.io/questions/Three%20Number%20Sum
// 注意: 与algoexpert的区别是这道题数组中的元素是允许有重复的，所以需要额外的步骤检查重复元素
/* 
* 1. 首先对数组进行排序
* 2. 排序后固定一个数 作为current(也就是数组中的nums[i])，再使用左右指针指向 nums[i]后面的两端，数字分别为 nums[left] 和 nums[right]
* 3. 如果 nums[i]大于 0，则三数之和必然无法等于 0，结束循环
* 4. 当 i > 0且nums[i] == nums[i - 1]时即跳过此元素nums[i]：因为已经将 nums[i - 1] 的所有组合加入到结果中，本次双指针搜索只会得到重复组合。
* 5. 当 left < right 时循环计算 sum = current + nums[left] + nums[right]，并按照以下规则执行双指针移动：
*    1) 当 sum < 0时，left += 1
*    2) 当 sum > 0时，right -= 1
*    3) 当 sum == 0 时，记录组合[current, nums[left], nums[right]]至result. 
*       如果nums[L] == nums[L+1] 则会导致结果重复，应该跳过，所以进行L++，直至不等于
*       如果nums[R] == nums[R-1] 则会导致结果重复，应该跳过，所以进行R--，直至不等于
!时间复杂度：O(n^2)，n 为数组长度


链接：https://leetcode-cn.com/problems/3sum/solution/3sumpai-xu-shuang-zhi-zhen-yi-dong-by-jyd/
*/
var threeSum = function (nums) {
    nums.sort((a, b) => a - b);
    let result = [];
    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        if (nums[i] > 0) continue;
        let current = nums[i];
        let left = i + 1;
        let right = nums.length - 1;
        while (left < right) {
            if (nums[left] + nums[right] + current < 0) left++;
            else if (nums[left] + nums[right] + current > 0) right--;
            else if (nums[left] + nums[right] + current === 0) {
                // console.log(nums[left], nums[right], current);
                result.push([current, nums[left], nums[right]]);
                while (nums[left + 1] === nums[left]) left++;
                while (nums[right - 1] === nums[right]) right--;
                left++;
                right--;
            }
        }
        // console.log(result);
    }
    return result;
};

threeSum([-1, 0, 1, 2, -1, -4]);
