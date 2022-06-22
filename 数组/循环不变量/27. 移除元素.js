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

/// 这里的循环不变量是 [0, insertPointer] 之间的所有值是有序的且不等于 val 的。
/// insertPointer 指向的是上一个元素被赋值的位置，insertPointer + 1 指向的是下一个元素被赋值的位置
/// 不能保证数组第一个元素一定不是 val, 因为循环不变量的定义是左闭右闭区间, 所以 insertPointer 初始值为 -1, 代表最开始不能确认 nums[0] 是不为 val的
var removeElementS2 = function (nums, val) {
    let traversePointer = 0;
    let insertPointer = -1;
    while (traversePointer < nums.length) {
        if (nums[traversePointer] === val) {
            traversePointer++;
        } else {
            insertPointer++;
            nums[insertPointer] = nums[traversePointer];
            traversePointer++;
        }
    }
    return insertPointer + 1;
};
