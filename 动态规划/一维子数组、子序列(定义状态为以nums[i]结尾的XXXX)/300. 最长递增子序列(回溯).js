// 回溯方法同 491
var lengthOfLIS = function (nums) {
    let cur = [];
    let maxLen = 0;
    function backtracking(startIdx) {
        if (cur.length >= 1) {
            if (cur.length > maxLen) {
                maxLen = cur.length;
            }
        }
        let set = new Set();

        for (let i = startIdx; i < nums.length; i++) {
            if (cur.length > 0 && nums[i] <= cur[cur.length - 1]) {
                continue;
            }
            if (set.has(nums[i])) {
                continue;
            }
            set.add(nums[i]);
            cur.push(nums[i]);
            backtracking(i + 1);
            cur.pop();
        }
    }

    backtracking(0);
    return maxLen;
};
