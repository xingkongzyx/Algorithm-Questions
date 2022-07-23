var combinationSum = function (candidates, target) {
    let results = [];
    let currentPath = [];
    let sum = 0;

    //! 为了后面for loop中的剪枝操作, candidates array必须先sort
    candidates.sort((a, b) => a - b);
    function helper(candidates, target, startIdx) {
        if (sum === target) {
            results.push([...currentPath]);
            return;
        }

        for (let i = startIdx; i < candidates.length; i++) {
            // # 对总集合排序之后，如果下一层的sum（就是本层的 sum + candidates[i]）已经大于target，因为candidates是经过排序后是有序的，所以candidates[i]后面的值也一定不满足条件，所以就可以结束本轮for循环的遍历。
            if (sum + candidates[i] > target) break;

            currentPath.push(candidates[i]);
            sum += candidates[i];
            helper(candidates, target, i);
            sum -= candidates[i];
            currentPath.pop();
        }
    }

    helper(candidates, target, 0);
    return results;
};
