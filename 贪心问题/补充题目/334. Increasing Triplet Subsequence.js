/* 
https://leetcode.cn/problems/increasing-triplet-subsequence/solutions/535725/pou-xi-ben-zhi-yi-wen-bang-ni-kan-qing-t-3ye2/?envType=study-plan-v2&envId=leetcode-75
*/
var increasingTriplet = function (nums) {
    let one = Infinity;
    let two = Infinity;

    /* 
        分为三种情况:
        1. 当前数字大于 two, 已经找到满足要求的三个数字并且 one < two < three
        2. 当前数字在 one 和 two 之间(one < nums[i] <= two), 更新 two
        3. 当前数字比 one 小, 更新 one, 但是不更新 two, 后续遍历如果有第三个数大于 two, 此时 [oldOne, two, three] 还是能够满足要求
           或者后续也会更新 two, 然后新的 one two three 组成满足的数组 
    */
    for (let i = 0; i < nums.length; i++) {
        let three = nums[i];

        if (three <= one) {
            // three 所在区间为 (-, one]
            one = three;
        } else if (three <= two) {
            // three 所在区间为 (one, two]
            two = three;
        } else if (three > two) {
            // three 所在区间为 (two, -)
            return true;
        }
    }

    return false;
};
