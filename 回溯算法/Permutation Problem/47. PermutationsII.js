//* 与 46 的区别在于给定的数组包含了「重复数字」，但返回的结果是要求「不重复」的。例如 nums = [1,2,1]. 返回的「正确结果」应是: [[1,1,2],[1,2,1],[2,1,1]].
//* 没有去重的「错误结果」是: [[1,1,2],[1,2,1],[2,1,1],[1,1,2],[1,2,1],[2,1,1]]。得到它的原因就是 nums 中「第一个 1」与「第二个 1」是重复的，程序如果不能正确识别，两个1将产生「完全一样」的结果，如上。
var permuteUnique = function (nums) {
    //! 去重一定要对元素进行排序
    nums.sort((a, b) => a - b);
    let currentPath = [];
    let totalPath = [];
    let used = new Array(nums.length).fill(false);

    function backtracking(used, nums) {
        if (currentPath.length === nums.length) {
            totalPath.push(currentPath.slice());
            return;
        }

        for (let i = 0; i < nums.length; i++) {
            // used[i - 1] == true，说明同一树枝nums[i - 1]使用过
            // used[i - 1] == false，说明同一树层nums[i - 1]使用过
            // *如果同一树层nums[i - 1]使用过则直接跳过
            if (
                i > 0 &&
                nums[i] === nums[i - 1] &&
                used[i - 1] === false
            )
                continue;
            // *如果是path里已经收录的元素，直接跳过
            if (used[i] === true) continue;

            used[i] = true;
            currentPath.push(nums[i]);
            backtracking(used, nums);
            used[i] = false;
            currentPath.pop();
        }
    }

    backtracking(used, nums);
    return totalPath;
};
