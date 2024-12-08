/* 
! 同 1343

暴力解法：来自 neetcode 
运用固定滑动窗口的思想，但是是暴力解法。
思路：针对数组中的每一项都进行遍历，针对每一项(包括最后一项，只要能形成 window 就遍历)再针对以它为开头形成的大小为 k 且两侧范围是[left, left + k]  的 window 进行遍历，看这个 window 中除了 nums[left] 外是否有跟 nums[left] 相同的元素
时间复杂度: O(n * k)
*/
var containsNearbyDuplicate = function (nums, k) {
    for (let left = 0; left < nums.length; left++) {
        for (
            let right = left + 1;
            right < Math.min(left + k + 1, nums.length);
            right++
        ) {
            // console.log('left', nums[left])
            // console.log('right', nums[right])
            if (nums[left] === nums[right]) return true;
        }
        // console.log('================')
    }

    return false;
};

// ? https://leetcode.cn/problems/contains-duplicate-ii/solutions/1219675/gong-shui-san-xie-hua-dong-chuang-kou-yu-q02i/
var containsNearbyDuplicate = function (nums, k) {
    const n = nums.length;
    // 用于记录当前 set 中的元素
    const set = new Set();
    /*
     * 滑动窗口每次操作的顺序是:
     *  1. 如果 window 大于 k，移除已经超过范围的数字(最左侧的数字)
     *  2. 检查当前遍历到的数字(也是即将添加进窗口的数字)是否已经在窗口中存在，存在则直接返回 true
     *       > 先移除再添加是为了防止即将添加的元素和即将移除的元素大小一致，影响判断结果
     *  3. 不存在的话则向窗口加入当前数字确保当前遍历结束后 window 维护当前为 k 的窗口存在的所有的值
     */

    // ! 每轮遍历结束后确保 set 维护当前为 k 的窗口存在的所有的值
    for (let i = 0; i < n; i++) {
        // 只要 i > k，说明当前窗口的最左边的值在本轮循环需要被移除
        if (i > k) {
            set.delete(nums[i - k - 1]);
        }

        // 每次再添加新的 window 的值的时候，首先检查当前窗口中是否已经存在这个 value 了
        if (set.has(nums[i])) {
            return true;
        }
        set.add(nums[i]);
    }
    return false;
};

var containsNearbyDuplicate = function (nums, k) {
    let left = 0;
    let right = 0;
    let set = new Set();
    while (right < nums.length) {
        // 与一般固定滑动窗口不同的地方在于添加当前值之前需要先检查窗口中是否已经包含了这个数字，所以此时的窗口的长度一定是保持小于 k 的；如果等于 k 就意味着用一个已经为 k 的创建判断窗口外的元素是否包含其中，不符合题目要求；如果此时长度为 k - 1，就是判断即将加入窗口的元素是否已然与窗口中的其他元素相等，然后将其加入窗口，在后面的 if 移除窗口最左边的元素，使得此时的长度又变为 k - 1，继续 while 循环
        if (set.has(nums[right])) {
            return true;
        }
        set.add(nums[right]);

        if (right - left === k) {
            set.delete(nums[left]);
            left++;
        }

        right++;
    }
    return false;
};
