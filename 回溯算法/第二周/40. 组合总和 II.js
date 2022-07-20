/* 
> 与 39.组合总和 的区别
* 1. 本题 candidates数组 中的每个数字在每个combination中只能使用一次。
* 2. 本题 candidates数组 中的元素是「有重复」的，而 39.组合总和 提供的是 "an array of 「distinct integers candidates」"
! 本题的难点在于区别2中：集合（数组candidates）有重复元素，但还不能有重复的组合。
! 「同一树枝」上的都是一个 combination 里的元素，不用去重。我们要去重的是「同一树层」上的〖使用过〗
*/

var combinationSum2 = function (candidates, target) {
    let currentPath = [];
    let results = [];
    let sum = 0;
    let used = new Array(candidates.length).fill(false);

    //# 非常重要，无论后面的剪枝还是对「同一树层」使用过的元素进行跳过都需要基于数组已经排序
    candidates.sort((a, b) => a - b);

    function helper(candidates, target, sum, startIdx, used) {
        if (sum === target) {
            results.push([...currentPath]);
            return;
        }

        for (let i = startIdx; i < candidates.length; i++) {
            //* 用于剪枝的判断语句
            if (sum + candidates[i] > target) break;

            /*
             * used[i - 1] == true，说明「同一树枝」上的 candidates[i - 1]使用过
             * used[i - 1] == false，说明「同一树层」上的 candidates[i - 1]使用过
             * 我们的目的就是对「同一树层」使用过的元素进行跳过
             */
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

            //# 回溯的过程
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
