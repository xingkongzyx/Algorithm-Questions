""" 
? https://leetcode.cn/problems/next-greater-element-i/solution/zhan-xia-yi-ge-geng-da-yuan-su-i-by-demi-cumj/
* 从左到右维护『单调递减栈』, 找元素右侧区域中「next greater element」
* 本质上我们需要记录的是后出现的比前出现的数字「第一次大」的位置和数值；显然和单调栈的特性相符. 
* 栈内维护「递减序列」. 正序遍历数组nums2, 对于当前考察的元素 nums2[i] 来说：
* ➀ 如果栈不为空且其值大于栈顶元素, 由于是「正序遍历」所以当前考察的元素 nums2[i] 是「栈顶元素」的「next greater element」也就是「下一个更大元素」。所以, 「栈顶元素」出栈作为 key, nums2[i] 作为 value 存入 map。随后, 将 nums2[i] 入栈, 看后面考察的元素会不会有大于 nums2[i] 的。
* ➁ 如果栈为空, 则将 nums2[i] 入栈, 看后面考察的元素会不会有大于 nums2[i] 的。
* 最后, 当数组 nums2 中所有元素都考察完毕时, 如果栈不为空, 说明栈中的剩余的元素没有找到「下一个更大元素」, 原因在于我们是正序遍历数组, 如果有其「下一个更大元素」, 在上面的判断中已经将其出栈了。所以对于栈中的元素来说, 不存在「下一个更大的元素」, 根据题意其对应的 value 为 -1。
? https://leetcode.cn/problems/next-greater-element-i/solution/dong-hua-yan-shi-dan-diao-zhan-496xia-yi-ql65/

/ 时间复杂度: 维护单调栈, 每个元素最多入栈出栈一次, 复杂度为 O(m)；构造答案复杂度为 O(n). 整体复杂度为 O(n + m)
/ 空间复杂度: O(m)

"""
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        record = {}
        stack = []
        for num in nums2:
            if len(stack) == 0:
                stack.append(num)
            else:
                while len(stack) > 0 and stack[-1] < num:
                    lastEle = stack[-1]
                    record[lastEle] = num
                    stack.pop()
                stack.append(num)
        
        for ele in stack:
            record[ele] = -1        
        
        resArr = []
        
        for num in nums1:
            resArr.append(record[num])
        
        return resArr
        
print(Solution().nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]))
