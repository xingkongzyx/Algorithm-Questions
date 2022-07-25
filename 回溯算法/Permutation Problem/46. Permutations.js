/* 
* 1. 递归函数参数
* 排列问题需要一个used数组，标记已经选择的元素.

* 2. 递归终止条件
* 当收集元素的数组 currentPath 的大小达到和 nums 数组一样大的时候，说明找到了一个全排列，也表示到达了叶子节点。

* 3. 单层搜索的逻辑
* 因为是排列问题，每次都要从头开始搜索。所以在for-loop中每次都是从i开始进行递归，通过used 数组告诉程序在本次排列递归中哪个数字已经被使用过了
> used数组，其实就是记录此时path里都有哪些元素使用了，一个排列里一个元素只能使用一次。
*/

var permute = function (nums) {
    let currentPath = [];
    let totalPath = [];
    let used = new Array(nums.length).fill(false);

    function backtracking(used, nums) {
        if (currentPath.length === nums.length) {
            totalPath.push(currentPath.slice());
            return;
        }

        for (let i = 0; i < nums.length; i++) {
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
