var findSubsequences = function (nums) {
    let currentPath = [];
    let totalPath = [];

    // # 我们用一个 set 存储每个合格的 path，下次遇到重复的，不让它加入解集即可。
    const set = new Set();

    function backtracking(nums, startIdx) {
        if (currentPath.length > 1) {
            //* path数组 转成字符串, 因为set中无法判断一个array是否出现重复，必须得转换成 string 再进行判断
            //! 注意数组中的元素在转换成string时必须用","分割，否则[13,14] 用单独的join("") 会变成 "1314" 可能会与一位数出现重复
            let pathToStr = currentPath.join(",");
            if (!set.has(pathToStr)) {
                set.add(pathToStr);
                totalPath.push(currentPath.slice());
            }
        }

        for (let i = startIdx; i < nums.length; i++) {
            if (
                currentPath.length == 0 ||
                currentPath[currentPath.length - 1] <= nums[i]
            ) {
                // 如果path为空，或满足递增关系，则可选择
                currentPath.push(nums[i]); // 选择当前的数字
            } else {
                continue;
            }
            backtracking(nums, i + 1); // 继续往下递归，注意传的是i+1
            currentPath.pop(); // 撤销选择当前数字，选择别的数字
        }
    }

    backtracking(nums, 0);
    // console.log(set);
    return totalPath;
};

let res = findSubsequences([1, 2, 3, 4, 5]);
console.log(res);
