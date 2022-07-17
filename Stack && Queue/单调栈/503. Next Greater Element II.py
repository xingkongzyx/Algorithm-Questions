""" 
* 遍历一次数组, 如果数组中的元素是「单调递减」的(则这些数字的「下一个更大元素」相同), 我们就把这些元素保存在一个「单调递减栈」中, 直到在接下来的数组遍历中找到一个较大的元素; 把该较大元素逐一跟保存在「单调递减栈」中的元素比较, 如果该元素更大, 那么它就是前面元素的「下一个更大元素」
? 可以理解的动图: https://leetcode.cn/problems/next-greater-element-ii/solution/dong-hua-jiang-jie-dan-diao-zhan-by-fuxu-4z2g/
? 与 497 一脉相承: https://leetcode.cn/problems/next-greater-element-ii/solution/dong-hua-jiang-jie-dan-diao-zhan-by-fuxu-4z2g/
/ 时间复杂度: O(N)，遍历了两次数组；
/ 空间复杂度: O(N)，使用了额外空间「单调栈」，最坏情况下，栈内会保存数组的所有元素。

"""
class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        resArr = [-1 for _ in nums]
        numLen = len(nums)
        for i in range(2 * numLen):
            modIdx = i % numLen
            #* 如果栈为空，则将当前元素的索引取余后的结果入栈，看后面是否有其「下一个更大元素」
            if len(stack) == 0:
                stack.append(modIdx)
            else:
                #* ➀ 如果当前元素比「栈顶元素」大：说明当前元素是「单调递减栈」中储存的一些元素的「下一个更大元素」，则逐个弹出「栈顶元素」，直到当前元素比「栈顶元素」小为止。
                #* ➁ 如果当前元素比「栈顶元素」小：说明当前元素的「下一个更大元素」与「栈顶元素」相同，则把当前元素入栈。
                while len(stack) > 0 and nums[stack[-1]] < nums[modIdx]:
                    resArr[stack[-1]] = nums[modIdx]
                    stack.pop()
                
                #* 最后, 将当前元素的索引取余后的结果入栈，看后面是否有其下一个更大元素
                stack.append(modIdx)

        return resArr
                

Solution().nextGreaterElements(nums = [1,2,3,4,3])
