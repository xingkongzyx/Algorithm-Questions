var combinationSum3 = function (k, n) {
    let results = [];
    let currentNums = [];

    function helper(targetSum, sum, k, startNum) {
        //* 剪枝的操作: 已选元素总和 sum 如果已经大于 targetSum了，那么往后遍历就没有意义了，直接剪掉。
        if (sum > targetSum) return;
        if (currentNums.length === k) {
            if (sum === targetSum) {
                results.push([...currentNums]);
            } else {
                return;
            }
        }

        for (let i = startNum; i <= 9; i++) {
            currentNums.push(i);
            sum += i;
            helper(targetSum, sum, k, i + 1);
            sum -= i;
            currentNums.pop();
        }
    }

    let startNum = 1;
    let sum = 0;
    helper(n, sum, k, startNum);
    // console.log(results);
    return results;
};
console.log(combinationSum3(4, 1));
