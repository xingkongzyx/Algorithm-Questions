/* 
? 视频讲解 https://leetcode.cn/problems/first-missing-positive/solutions/7703/tong-pai-xu-python-dai-ma-by-liweiwei1419/
? 图片讲解 https://leetcode.cn/problems/first-missing-positive/solutions/1142914/duo-tu-yu-jing-xiang-jie-yuan-di-ha-xi-b-se25/
*/
var firstMissingPositive = function (nums) {
    let len = nums.length;
    // [1, len]
    // i -> i + 1
    for (let i = 0; i < len; i++) {
        while (
            nums[i] > 0 &&
            nums[i] <= len &&
            nums[i] !== nums[nums[i] - 1]
        ) {
            let correctPos = nums[i] - 1;
            [nums[i], nums[correctPos]] = [nums[correctPos], nums[i]];
        }
    }

    for (let i = 0; i < len; i++) {
        if (nums[i] !== i + 1) return i + 1;
    }
    return len + 1;
};
