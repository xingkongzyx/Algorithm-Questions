var subsetsWithDup = function (nums) {
    nums.sort((a, b) => a - b);

    let currentPath = [];
    let totalPath = [];
    let used = new Array(nums.length).fill(false);
    function backtracking(nums, startIdx) {
        totalPath.push(currentPath.slice());
        if (startIdx >= nums.length) return;

        for (let i = startIdx; i < nums.length; i++) {
            if (
                i > 0 &&
                nums[i] === nums[i - 1] &&
                used[i - 1] === false
            ) {
                continue;
            }
            used[i] = true;
            currentPath.push(nums[i]);
            backtracking(nums, i + 1);
            used[i] = false;
            currentPath.pop();
        }
    }
    backtracking(nums, 0);

    return totalPath;
};

let res = subsetsWithDup([1, 2, 2]);
console.log(res);
