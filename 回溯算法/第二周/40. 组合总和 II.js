/* 
* 1. 本题candidates 中的每个数字在每个组合中只能使用一次。
* 2. 本题数组candidates的元素是有重复的，而39.组合总和 (opens new window)是无重复元素的数组candidates 
! 本题的难点在于区别2中：集合（数组candidates）有重复元素，但还不能有重复的组合。
*/

var combinationSum2 = function (candidates, target) {
    let currentPath = [];
    let results = [];
    let sum = 0;
    let used = new Array(candidates.length).fill(false);

    //# 非常重要，无论后面的剪枝还是对同一树层使用过的元素进行跳过都需要基于数组已经排序
    candidates.sort((a, b) => a - b);

    function helper(candidates, target, sum, startIdx, used) {
        if (sum === target) {
            results.push([...currentPath]);
            return;
        }

        for (let i = startIdx; i < candidates.length; i++) {
            //* 用于剪枝的判断语句
            if (sum + candidates[i] > target) break;

            //* used[i - 1] == true，说明同一树枝candidates[i - 1]使用过
            //* used[i - 1] == false，说明同一树层candidates[i - 1]使用过
            //* 要对同一树层使用过的元素进行跳过
            if (
                i > 0 &&
                candidates[i] == candidates[i - 1] &&
                used[i - 1] === false
            ) {
                continue;
            }

            currentPath.push(candidates[i]);
            sum += candidates[i];
            used[i] = true;
            helper(candidates, target, sum, i + 1, used);
            // ! 回溯的过程
            currentPath.pop();
            sum -= candidates[i];
            used[i] = false;
        }
    }

    helper(candidates, target, sum, 0, used);
    return results;
};

let candidates = [2, 5, 2, 1, 2];
let target = 5;
combinationSum2(candidates, target);
