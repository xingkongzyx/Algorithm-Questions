/* 
> 数组是有序的是使用循环不变量的关键
# 指针 traversePointer 进行数组遍历, insertPointer 指向了「下一个」将要被赋值的元素的下标。
# 这里的循环不变量是 [0..insertPointer), 说明 insertPointer 之前的所有元素是「有序的」且「无重复的」, insertPointer 指向了「下一个」将要被赋值的元素的下标。
* 因为第一个元素肯定是无重复的, 所以两个指针初始化为 1。每次 nums[traversePointer] 要与「无重复有序数组部分」的「最后一个元素」进行比较, 如果 nums[traversePointer] != nums[insertPointer-1] , 说明遇到了与 [0..insertPointer) 之间无重复的值。将 insertPointer 指向的位置进行赋值操作, 然后更新两个指针。最后返回的值就是 insertPointer
 */

var removeDuplicates = function (nums) {
    if (nums.length < 1) return 0;

    let traversePointer = 1;
    let insertPointer = 1;
    while (traversePointer < nums.length) {
        if (nums[traversePointer] === nums[insertPointer - 1]) {
            traversePointer++;
        } else {
            nums[insertPointer] = nums[traversePointer];
            traversePointer++;
            insertPointer++;
        }
    }
    return insertPointer;
};
