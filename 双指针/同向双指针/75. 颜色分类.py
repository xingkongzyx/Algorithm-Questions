
#? https://leetcode.cn/problems/sort-colors/solution/fei-chang-jian-ji-de-xie-fa-by-tchj-z9fp/

class Solution(object):
    def sortColors(self, nums):
        
        #* [0, redPointer) 左闭又开区间内的元素都是0
        redPointer = 0
        #* [bluePointer, len(nums)-1] 左开右闭区间内的元素都是2
        bluePointer = len(nums) - 1
        
        index = 0
        
        while index <= bluePointer:
            if nums[index] == 1:
                index += 1
                continue
            elif nums[index] == 0:
                """ 
                * 当 index 位置上的数字是 0 时, 需要将其与 redPointer 指向的数字进行交换。我们可以分成两种情况来讨论：
                * 1. redPointer 和 index 和重合：那么就相当于 index 和 index 自己交换, 此时 index 位置上的数字就处理完了, index 和 redPointer 都可以推进。
                * 2. index 和 redPointer 不重合：那么index所在的位置一定是在 redPointer 前面的, 这之间如果包含 2 已经被交换处理过了. 那么 redPointer 对应的数字一定是 1(例子: 0110), 如果不是 1 的话,  redPointer 和 index 一定是重合的(包含一种特殊情况, 数组中只有0和2的时候)。此时交换完以后, index 位置上就会是1, 那么也可以直接 +1 推进。 
                """
                nums[redPointer], nums[index] = nums[index], nums[redPointer]
                redPointer += 1 
                index += 1
            elif nums[index] == 2:
                #* 当 index 位置上的数字是 2 时, 我们进行交换后是不能继续推进 index 的. 因为 index 这个指针的遍历顺序是从左到右的, 我们确定 index 左边的数字要不是 1 要不是 0. 但目前 index 这个位置刚刚进行交换, 交换过的数字是没有进行处理的, 这个数字是一个全新的(0,1,2都有可能), 如果交换过来数字是 0 或者是 2, 我们推进 index 的话, 就会出错。此时只能更新 bluePointer, 因为它原来的位置已经能确定在交换后是 2
                nums[bluePointer], nums[index] = nums[index], nums[bluePointer]
                bluePointer -= 1
        return nums

print(Solution().sortColors(nums = [2,0,1]) )            
        
        