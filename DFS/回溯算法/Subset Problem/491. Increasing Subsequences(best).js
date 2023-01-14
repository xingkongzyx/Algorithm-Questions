/* 
> 在 90. Subsets II 中我们是通过排序, 再加一个标记数组来达到去重的目的。而本题求递增「子序列」, 是不能对原数组进行排序的, 排序完的数组无法满足「子序列」的要求
# 这道题就是因为没有办法排序才不能像 lc 90 那样使用一个全局的 used 数组进行去重; 重复的元素在没有排序的情况下不一定是相邻的，可能隔着几位才出现。所以每一层得用一个 set 过滤重复元素
? 通过同一数层出现重复元素进行去重操作: https://programmercarl.com/0491.%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97.html#%E6%80%9D%E8%B7%AF
*/
var findSubsequences = function (nums) {
    let currentPath = [];
    let totalPath = [];

    function backtracking(nums, startIdx) {
        if (currentPath.length > 1) {
            totalPath.push(currentPath.slice());
        }
        //! 使用set来对本层元素进行去重, 要确保「同一父节点」下的「同层上使用过的元素」就不能再使用了
        let levelSet = new Set();
        for (let i = startIdx; i < nums.length; i++) {
            /*
             * 将当前的数字 nums[i] 加入 currentPath 的条件有三个(➀ && (➁ || ➂)):
             * ➀ 这个方法独有的: 这个数字在「同一父节点」下的同层子节点中还没有被使用过(同层子节点指的就是 for 循环中遍历的数字)
             * ➁ 满足➀的前提下，如果 currentPath 为空,
             * ➂ 满足➀的前提下，或者 path 数组中的最后一个数与「当前要加入的数」满足「递增」关系, 则可选择当前的数字 nums[i] 加入 currentPath. */
            if (
                levelSet.has(nums[i]) == false &&
                (currentPath.length == 0 ||
                    currentPath[currentPath.length - 1] <= nums[i])
            ) {
                levelSet.add(nums[i]);
                currentPath.push(nums[i]);
                //* 继续往下递归, 注意传的是i+1
                backtracking(nums, i + 1);
                //* 撤销选择当前数字, 选择别的数字
                currentPath.pop();
            }
        }
    }

    backtracking(nums, 0);
    // console.log(set);
    return totalPath;
};
