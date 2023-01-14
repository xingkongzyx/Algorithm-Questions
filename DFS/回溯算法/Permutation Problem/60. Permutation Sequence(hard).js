/* 
* 与一般的「permutation 问题」相比, 我们使用 count 和 res 来辅助进行剪枝操作. 通过使用 count 记录生成的排列的个数从而确保当数量满足要求时退出回溯过程。而在一般「permutation 问题」中使用的 total 则不再需要, 因为题目只要求得到 "kth permutation sequence."

? 思路来源: https://leetcode.cn/problems/permutation-sequence/solution/shou-hua-tu-jie-jing-dian-de-dfshui-su-shu-xue-gui/
? permutation的代码来自于「代码随想录」的全排列专题

*/
var getPermutation = function (n, k) {
    let curPath = [];
    let used = new Array(n).fill(false);
    let count = 0;
    let result = null;
    function backtracking() {
        //* 当 curPath 长度等于 n 的时候, 说明生成了一个满足条件的 permutation, count += 1
        if (curPath.length === n) {
            count += 1;
            //* 如果此时正好是第 k 个, 则更新记录最终结果的变量 result
            if (count === k) result = curPath.join("");
            return;
        }
        for (let i = 1; i <= n; i++) {
            if (used[i] === true) continue;
            used[i] = true;
            curPath.push(i);
            backtracking();
            //! 剪枝操作
            //* 如果 result 不为 null, 说明找到了 kth permutation sequence, 返回, 不用再继续递归
            if (result !== null) return;
            curPath.pop();
            used[i] = false;
        }
    }
    backtracking();
    return result;
};
