// https://leetcode.cn/problems/contains-duplicate-ii/solutions/13564/hua-jie-suan-fa-219-cun-zai-zhong-fu-yuan-su-ii-by/?envType=study-plan-v2&envId=top-interview-150
var containsNearbyDuplicate = function (nums, k) {
    let right = 0;
    let set = new Set();

    while (right < nums.length) {
        let rightNum = nums[right];

        if (set.has(rightNum)) return true;

        set.add(rightNum);

        if (set.size > k) {
            set.delete(nums[right - k]);
        }

        right++;
    }

    return false;
};
