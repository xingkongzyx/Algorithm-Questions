/* 
! 与 17 题的区别:
? 如果是一个集合来求组合的话, 就需要startIndex, 例如：77.组合 , 216.组合总和III 。
? 如果是多个集合取组合, 各个集合之间相互不影响, 那么就不用startIndex, 例如：17.电话号码的字母组合
? 题解的回溯树非常好: https://leetcode.cn/problems/combination-sum/solution/shou-hua-tu-jie-zu-he-zong-he-combination-sum-by-x/
 */
var combinationSum = function (candidates, target) {
    let results = [];
    let currentPath = [];
    let sum = 0;
    function helper(candidates, target, startIdx) {
        //# 对于sum已经大于target的情况, 其实是依然进入了下一层递归, 只是下一层递归结束判断的时候, 会判断sum > target的话就返回。
        if (sum > target) return;
        if (sum === target) {
            results.push([...currentPath]);
            return;
        }
        //* 不产生重复组合怎么限制（剪枝）？通过限制「下一次选择的起点」, 让「下一次选择的起点」是基于本次的选择, 这样下一次就不会选到本次选择同层左边的数。即通过控制 for 遍历的起点, 去掉会产生重复组合的选项。
        for (let i = startIdx; i < candidates.length; i++) {
            currentPath.push(candidates[i]);
            sum += candidates[i];
            //* 基于本次的选择, 继续选择, 传i, 下次就不会选到i左边的数
            helper(candidates, target, i);
            sum -= candidates[i];
            currentPath.pop();
        }
    }

    helper(candidates, target, 0);
    return results;
};
