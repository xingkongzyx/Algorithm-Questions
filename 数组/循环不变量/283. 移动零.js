/*
/ 解法: 题目让我们将所有 0 移到最后，其实就相当于移除 nums 中的所有 0，然后再把后面的元素都赋值为 0 即可。所以我们可以复用 lc80 的 removeElement 函数：
 */

var moveZeroesS1 = function (nums) {
    //* 定义两个指针traversePointer用于遍历数组，insertPointer用于放置遍历过程中不为0的元素。
    //* 这道题的循环不变量是 [0, insertPointer) 之间的数组是不为 0 的, insertPointer 指向的是下一个元素要赋值的位置
    let traversePointer = 0;
    let insertPointer = 0;
    while (traversePointer < nums.length) {
        if (nums[traversePointer] === 0) {
            traversePointer++;
        } else {
            nums[insertPointer] = nums[traversePointer];
            traversePointer++;
            insertPointer++;
        }
    }
    //* 因为循环不变量的定义是 [0, insertPointer) 之间的数组是不为 0 的，所以 insertPointer 之前的位置经过上面的 while 循环都是不为0的，从它开始的位置要进行设置成 0 的操作
    // for (; insertPointer < nums.length; insertPointer++) {
    //     nums[insertPointer] = 0;
    // }
};

var moveZeroesS2 = function (nums) {
    //* 定义两个指针traversePointer用于遍历数组，insertPointer用于放置遍历过程中不为0的元素。
    //* 这道题的循环不变量是 [0, insertPointer] 之间的数组是不为 0 的, insertPointer 指向的是上一个元素被赋值的位置(也就是 insertPointer 及其之前的元素都是不为0的), insertPointer + 1 才是下一个要被赋值的位置
    let traversePointer = 0;
    //! 因为循环不变量的定义，所以 初始的循环不变量 [0, -1] 说明最开始没有位置是不为 0 的，所以下一个要被赋值的位置是 ｢insertPointer + 1｣ => ｢-1 + 1｣ => 0
    let insertPointer = -1;
    while (traversePointer < nums.length) {
        if (nums[traversePointer] === 0) {
            traversePointer++;
        } else {
            //* 先更新 insertPointer 到要赋值的位置
            insertPointer++;
            nums[insertPointer] = nums[traversePointer];
            traversePointer++;
        }
    }
    //* 因为循环不变量的定义是 [0, insertPointer] 之间的数组是不为 0 的，所以从 insertPointer 开始(也包括它) 指向的位置经过上面的while循环都是不为0的，从 insertPointer 的下一位要进行设置成 0 的操作
    for (let i = insertPointer + 1; i < nums.length; i++) {
        nums[i] = 0;
    }
};
