/*
 * 关于 for 循环中 if 判断条件为什么是 "used[i - 1] === false" 的理解: 表面上, 使用 continue 的判断条件应该是「前一个元素」被使用过, 这里跟正常逻辑相悖; 仔细想想, 如果 used[i - 1] 被标记为 True,  说明该元素刚被使用过且未回溯, 也就是同一树枝出现了重复元素. 那么就算第 i 个元素和第 i-1 个元素相等, 也可以放心大胆地加到 currentPath 里面, 因为加入以后一定比之前元素多一个, 不会重复; 相反, 如果 used[i - 1] 被标记为 false, 说明现在已经访问到之后的元素了, 之前元素一定是「被访问过」的, 那么被标 false 只有一种可能, 就是该元素已经「被回溯过」了, 此时必须跳过当前元素, 否则会重复, 因为 totalPath 里面已经有相同的 currentPath.
 */

var subsetsWithDup = function (nums) {
    //! 去重一定要先对集合排序
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
