/* 
! 与 17 题的区别:
? 如果是一个集合来求组合的话，就需要startIndex，例如：77.组合 ，216.组合总和III 。
? 如果是多个集合取组合，各个集合之间相互不影响，那么就不用startIndex，例如：17.电话号码的字母组合
 */
var combinationSum = function (candidates, target) {
    let results = [];
    let currentPath = [];
    let sum = 0;
    function helper(candidates, target, startIdx) {
        //# 对于sum已经大于target的情况，其实是依然进入了下一层递归，只是下一层递归结束判断的时候，会判断sum > target的话就返回。
        if (sum > target) return;
        if (sum === target) {
            results.push([...currentPath]);
            return;
        }

        for (let i = startIdx; i < candidates.length; i++) {
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
