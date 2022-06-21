var permuteUnique = function (nums) {
    nums.sort((a, b) => a - b);
    let currentPath = [];
    let totalPath = [];
    let used = new Array(nums.length).fill(false);

    function backtracking(used, nums) {
        if (currentPath.length === nums.length) {
            totalPath.push(currentPath.slice());
            return;
        }

        for (let i = 0; i < nums.length; i++) {
            // used[i - 1] == true，说明同一树枝nums[i - 1]使用过
            // used[i - 1] == false，说明同一树层nums[i - 1]使用过
            // *如果同一树层nums[i - 1]使用过则直接跳过
            if (
                i > 0 &&
                nums[i] === nums[i - 1] &&
                used[i - 1] === false
            )
                continue;
            // *如果是path里已经收录的元素，直接跳过
            if (used[i] === true) continue;

            used[i] = true;
            currentPath.push(nums[i]);
            backtracking(used, nums);
            used[i] = false;
            currentPath.pop();
        }
    }

    backtracking(used, nums);
    return totalPath;
};

// var permuteUnique = function (nums) {
//     let currentPath = [];
//     let totalPath = [];
//     let used = new Array(nums.length).fill(false);
//     let resultSet = new Set();

//     function backtracking(used, nums) {
//         if (currentPath.length === nums.length) {
//             let currentPathStr = currentPath.join(",");
//             if (resultSet.has(currentPathStr)) {
//                 return;
//             } else {
//                 totalPath.push(currentPath.slice());
//                 resultSet.add(currentPathStr);
//                 return;
//             }
//         }

//         for (let i = 0; i < nums.length; i++) {
//             if (used[i] === true) continue;

//             used[i] = true;
//             currentPath.push(nums[i]);
//             backtracking(used, nums);
//             used[i] = false;
//             currentPath.pop();
//         }
//     }

//     backtracking(used, nums);
//     return totalPath;
// };

const nums = [1, 1, 2];
let res = permuteUnique(nums);
console.log(res);
