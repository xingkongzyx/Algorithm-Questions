var canPartition = function (nums) {
    let sum = 0;
    for (let num of nums) {
        sum += num;
    }

    let targetSum = sum / 2;
    let currentPath = [];
    let totalPath = [];
    function backtracking(startIdx, targetSum) {
        if (targetSum === 0) {
            totalPath.push(currentPath.slice());
            return true;
        }

        for (let i = startIdx; i < nums.length; i++) {
            currentPath.push(nums[i]);
            targetSum -= nums[i];
            let res = backtracking(i + 1, targetSum);
            if (res === true) return true;
            targetSum += nums[i];
            currentPath.pop();
        }

        return false;
    }

    backtracking(0, targetSum);
    console.log(totalPath);
};

var canPartition_optimize = function (nums) {
    let sum = 0;
    nums.sort((a, b) => a - b);

    for (let num of nums) {
        sum += num;
    }

    let targetSum = sum / 2;

    function backtracking(startIdx, targetSum) {
        if (targetSum === 0) {
            return true;
        }

        for (let i = startIdx; i < nums.length; i++) {
            targetSum -= nums[i];
            if (targetSum < 0) break;
            let res = backtracking(i + 1, targetSum);
            if (res === true) return true;
            targetSum += nums[i];
        }

        return false;
    }

    let res = backtracking(0, targetSum);
    return res;
};

const nums = [
    100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    100, 100, 100, 100, 100, 100, 100, 99, 97,
];
console.log(canPartition_optimize(nums));
