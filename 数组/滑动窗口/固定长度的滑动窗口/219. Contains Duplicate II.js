// ? https://leetcode.cn/problems/contains-duplicate-ii/solutions/1219675/gong-shui-san-xie-hua-dong-chuang-kou-yu-q02i/
var containsNearbyDuplicate = function (nums, k) {
    const n = nums.length;
    const set = new Set();
    /*
     * 滑动窗口操作的顺序是:
     *  1. 移除已经超过范围的数字
     *  2. 检查当前遍历到的数字是否已经在窗口中存在，存在则直接返回 true
     *  3. 不存在的话则向窗口加入当前数组
     */
    for (let i = 0; i < n; i++) {
        // 只要 i > k，说明当前窗口的最左边的值在本轮循环需要被移除
        if (i > k) {
            set.delete(nums[i - k - 1]);
        }
        if (set.has(nums[i])) {
            return true;
        }
        set.add(nums[i]);
    }
    return false;
};
