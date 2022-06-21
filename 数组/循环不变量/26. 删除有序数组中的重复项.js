/**
首先注意数组是有序的

1. 令索引 i 为慢指针，索引 j 为快指针，快指针正常遍历数组，一次走一步
2. 如果快指针和慢指针所指的元素不相同，证明慢指针所指元素的重复已结束(注意这句话)，索引 i = i + 1，并把新的元素赋给更新后的索引 i 处. 
3. 也就是说，慢指针记录的是非重复元素的索引，最后返回非重复元素个数为 i + 1

https://leetcode.cn/problems/remove-duplicates-from-sorted-array/solution/26-shan-chu-pai-xu-shu-zu-zhong-de-zhong-fle5/
 */

var removeDuplicates = function (nums) {
    if (nums.length < 1) return 0;

    // > 数组是有序的是使用循环不变量的关键
    // # 指针 traversePointer 进行数组遍历，insertPointer 指向了下一个将要被赋值的元素的下标。
    // # 这里的循环不变量是 [0..insertPointer), 说明 insertPointer 之前的元素是有序的且无重复的，insertPointer 指向了下一个将要被赋值的元素的下标。因为第一个元素肯定是无重复的，所以两个指针初始化为 1. 每次 nums[traversePointer] 要与有序数组部分的最后一个元素进行比较，如果 nums[traversePointer] != nums[insertPointer-1] 说明遇到了与 [0..insertPointer) 之间无重复的值。将 insertPointer 指向的位置进行赋值操作，然后更新两个指针。最后返回的值就是 insertPointer

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
