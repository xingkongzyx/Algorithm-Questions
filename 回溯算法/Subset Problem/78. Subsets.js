//? https://leetcode.cn/problems/subsets/solution/shou-hua-tu-jie-zi-ji-hui-su-fa-xiang-jie-wei-yun-/
var subsets = function (nums) {
    let currentPath = [];
    let totalPath = [];

    function backtracking(nums, startIdx) {
        //* 这句话确保子集是收集树形结构中树的所有节点的结果。
        //* 也确保了最开始调用function时 [] 也被加入了子集
        totalPath.push(currentPath.slice());

        //# 可要可不要
        if (startIdx >= nums.length) return;

        for (let i = startIdx; i < nums.length; i++) {
            currentPath.push(nums[i]); //* 子集收集元素
            backtracking(nums, i + 1); //* 注意从i+1开始，元素不重复取
            currentPath.pop(); //* 回溯
        }
    }

    backtracking(nums, 0);
    return totalPath;
};
