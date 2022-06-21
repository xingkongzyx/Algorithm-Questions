/*
/ 解法2: 题目让我们将所有 0 移到最后，其实就相当于移除 nums 中的所有 0，然后再把后面的元素都赋值为 0 即可。所以我们可以复用 lc80 的 removeElement 函数：
 */

var moveZeroes = function (nums) {
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
    //* 因为循环不变量的定义是 [0, insertPointer) 之间的数组是不为 0 的，所以从 insertPointer 开始(也包括它) 指向的位置经过上面的while循环都是不为0的，在这里要进行设置成 0 的操作
    for (; insertPointer < nums.length; insertPointer++) {
        nums[insertPointer] = 0;
    }
};
