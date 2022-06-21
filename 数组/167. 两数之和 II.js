// ! 属于左右指针题目
// 只要数组有序，就应该想到双指针技巧。这道题的解法有点类似二分查找，通过调节 left 和 right 就可以调整 sum 的大小
var twoSum = function (numbers, target) {
    let left = 0;
    let right = numbers.length - 1;
    while (left < right) {
        if (numbers[left] + numbers[right] === target)
            return [left + 1, right + 1];
        else if (numbers[left] + numbers[right] < target) left += 1;
        else right -= 1;
    }

    return [-1, -1];
};
