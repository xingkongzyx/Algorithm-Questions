/* 
题目要求偶数下标放偶数，奇数下标放奇数。我们可以用两个指针：
even 从下标 0 开始，只走偶数下标（每次 +2），专门检查偶数下标是否正确。
odd 从下标 1 开始，只走奇数下标（每次 +2），专门检查奇数下标是否正确。

在扫描过程中：
如果 even 指向的偶数下标位置已经是偶数，就跳到下一个偶数下标。
如果 odd 指向的奇数下标位置已经是奇数，就跳到下一个奇数下标。
如果 even 位置是奇数且 odd 位置是偶数，说明它们互换即可让两个位置都正确，交换后两个指针各前进一格（+2）。

循环直到两个指针有一个越界为止。
*/
var sortArrayByParityII = function (nums) {
    let odd = 1; // 从第一个奇数下标开始
    let even = 0; // 从第一个偶数下标开始

    // 当两个指针都还在数组范围内时继续处理
    while (odd < nums.length && even < nums.length) {
        // 如果偶数下标位置是偶数，则跳到下一个偶数下标
        if (nums[even] % 2 === 0) {
            even += 2;
        }
        // 如果奇数下标位置是奇数，则跳到下一个奇数下标
        else if (nums[odd] % 2 === 1) {
            odd += 2;
        }
        // 否则，偶数下标放了奇数，奇数下标放了偶数
        // 两个位置互换即可同时修正
        else {
            let temp = nums[even];
            nums[even] = nums[odd];
            nums[odd] = temp;
            even += 2;
            odd += 2;
        }
    }
    return nums;
};
