/* 
//! 这个代码是错的，因为JavaScript没有数组越界的问题，所以即使代码如下
* while (nums[left] === nums[left + 1]) {
*     left++;
* }
* while (nums[right] === nums[right - 1]) {
*     right--;
* }
! 面对test case [0,0,0,0] 也不会出现 left 出现越界错误的问题，但是实际上在python代码中会直接报错
*/

var threeSum = function (nums) {
    nums.sort((a, b) => a - b);
    let res = [];

    if (nums.length < 3) return res;

    for (let i = 0; i <= nums.length - 3; i++) {
        if (nums[i] > 0) break;
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let left = i + 1;
        let right = nums.length - 1;
        let remain = 0 - nums[i];
        while (left < right) {
            if (nums[left] + nums[right] < remain) {
                left++;
            } else if (nums[left] + nums[right] > remain) {
                right--;
            } else if (nums[left] + nums[right] == remain) {
                res.push([nums[i], nums[left], nums[right]]);

                while (nums[left] === nums[left + 1]) {
                    left++;
                }
                while (nums[right] === nums[right - 1]) {
                    right--;
                }

                left++;
                right--;
            }
        }
    }
    return res;
};
