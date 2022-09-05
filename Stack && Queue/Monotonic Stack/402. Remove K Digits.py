""" 
! 与 316 非常类似
#? https://leetcode.cn/problems/remove-k-digits/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-5/
#? 官方的动画非常好: https://leetcode.cn/problems/remove-k-digits/solution/yi-diao-kwei-shu-zi-by-leetcode-solution/

* 对于两个「相同长度」的数字序列, 『最左边不同』的数字决定了这两个数字的大小, 例如, 对于 A = 1axxx, B = 1bxxx, 如果 a > b 则 A > B。
! 若要使得剩下的数字最小, 需要保证靠前的数字尽可能小。
# 给定一个长度为 n 的数字序列 [D0, D1, D2, D3 ... Dn-1], 从左往右找到『第一个』位置 i(i>0) 使得 Di < Di-1, 并删去 Di-1; 如果不存在, 说明整个数字序列单调不降, 删去最后一个数字即可。

/ 时间复杂度: 虽然内层还有一个 while 循环, 但是由于每个数字最多仅会入栈出栈一次, 因此时间复杂度仍然为 O(N), 其中 N 为数字长度。
/ 空间复杂度: 我们使用了额外的栈来存储数字, 因此空间复杂度为 O(N), 其中 N 为数字长度。

"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        neededDigits = len(num) - k
        #* 栈中的元素代表截止到当前位置, 删除不超过 k 次个数字后, 所能得到的最小整数。根据之前的讨论：在使用 k 个删除次数之前, 栈中的序列从栈底到栈顶「单调不降」。
        stack = []
        
        for digit in num:
            #* 对于 num 数组中的每个数字, 如果该数字小于「栈顶元素」, 我们就不断地弹出「栈顶元素」, 直到下列三种情况任一情况不被满足: ➀ 栈为空, ➁ 新的栈顶元素不大于当前数字, ➂ 我们已经删除了 k 位数字
            while len(stack) > 0 and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
  
            stack.append(digit)

        # print(stack, k)
        
        #* 如果原数组本身就是「单调不降」的, 那么我们最后删除的数字个数「肯定小于」k 个, 这种情况,「单调栈」中的元素个数大于想要的 neededDigits 个, 可以选择直接舍弃最后面的「经过上面 k-= 1 减少后」的 k 个元素, 或者说是保留前面的 neededDigits 个元素
        stack = stack[:neededDigits]
        
        #* 去除 stack 中的 前导0, 如10200, k = 1
        while stack and stack[0] == "0":
            stack.pop(0)
                
        if len(stack) == 0:
            return "0"
        else:
            return ''.join(stack)           
        
        
print(Solution().removeKdigits(num = "10001", k = 4))
# print(Solution().removeKdigits(num = "123456", k = 4))
