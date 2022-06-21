// 属于快慢指针题目
// 26, 27 以及 283 其中283相当于27的延续

/// 这里的循环不变量是 [0, insertPointer) 之间的所有值是有序的且不等于 val 的。
/// insertPointer 指向的是下一个元素要赋值的位置
/// 不能保证第一个元素就一定不是 val, 所以两个指针都要从0开始遍历
var removeElement = function (nums, val) {
    let traversePointer = 0;
    let insertPointer = 0;
    while (traversePointer < nums.length) {
        if (nums[traversePointer] === val) {
            traversePointer++;
        } else {
            nums[insertPointer] = nums[traversePointer];
            traversePointer++;
            insertPointer++;
        }
    }
    return insertPointer;
};
