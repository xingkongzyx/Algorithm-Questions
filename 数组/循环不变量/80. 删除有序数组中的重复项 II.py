""" 
# 循环不变量是[0, insertPointer), 表示 insertPointer 位置之前的数组是「有序的」且每个元素「最多出现两次」, insertPointer 指向「下一个要被赋值」的地方。nums 数组的「第0位、第1位」最坏情况就是同一个数字出现了两次。insertPointer 初始化为 2, 仍然是符合0, insertPointer) 的数组是「有序的」且每个元素「最多出现两次」的循环不变量. 所以初始遍历从数组第 3 位开始
"""
""" 
另一种通过 count 来记录单一元素重复次数的方法的方法
根据循环不变量的定义 count 最开始也是 1
var removeDuplicates = function(nums) {
    let insert = 1;
    let count = 1
    for(let traverse = 1; traverse < nums.length; traverse++) {
        if(nums[traverse] !== nums[insert - 1]) {
            nums[insert] = nums[traverse];
            insert++;
            count = 1
        } else {
            if(count === 2) {
            } else {
                count ++;
                nums[insert] = nums[traverse];
                insert++;
            }
        }
    }
    return insert
};
 """

class Solution(object):
    def removeDuplicates(self, nums):
        # * 排除特殊情况
        if len(nums) <= 2:
            return len(nums)

        insertPointer = 2
        traversePointer = 2

        while traversePointer < len(nums):
            # * 如果 traversePointer 指向的值和 insertPointer-2 指向的值不同, 说明还没有值已经出现了两次, 可以放心将 traversePointer 指向的值赋值给 insertPointer, 然后更新 insertPointer 到下一位。更新后 nums[insertPointer-1] 和 nums[insertPointer-2] 可能是相同的, 但因为我们在本轮循环中的判断条件就是比较 nums[insertPointer-3] 与 nums[traversePointer-1] 是不同的(此时出现的两个指针都是执行完if语句后的值), 所以 [0, insertPointer) 中的值最多出现了两次仍然符合题目要求
            if nums[traversePointer] != nums[insertPointer - 2]:
                nums[insertPointer] = nums[traversePointer]
                traversePointer += 1
                insertPointer += 1
            else:
                # * 如果 traversePointer 指向的值和 insertPointer-2 指向的值相同, 说明 nums[insertPointer-2] 这个值已经出现了两次(nums[insertPointer-2] 以及 nums[insertPointer-1]), 不可以继续将 traversePointer 指向的值赋给 nums[insertPointer], 那样的话同一个元素出现了三次, 不符合题目要求。只能更新 traversePointer 到下一个位置；例如 [1,1,1,2,2], 当 ip = 2, tp = 2 时只能更新 tp, 而不能进行赋值操作, 否则 ip = 3, tp = 3, 循环不变量区间变为 [0, 3) 但 nums[0], nums[1], nums[2] 三个位置已经出现3个1,  不符合题目要求
                traversePointer += 1

        return insertPointer
