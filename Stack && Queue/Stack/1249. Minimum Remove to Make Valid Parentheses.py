
#? 对应解法: https://leetcode.cn/problems/minimum-remove-to-make-valid-parentheses/solution/yi-chu-wu-xiao-de-gua-hao-zhan-by-97wgl/
#/ 时间复杂度：O(n) 空间复杂度：O(N)
class Solution(object):
    def minRemoveToMakeValid(self, s):
        #* 「标记数组」, 这个数组用于标记 s 中「无效括号」的位置. 默认数组所有位置都是有效的(都是 True). 通过遍历将出现「无效括号」的位置变为 False
        validArr = [True for _ in s]
        #* 模拟一个栈存放所有遍历到的「左括号」左括号的索引, 
        stack = []
        
        for i in range(len(s)):
            char = s[i]
            #* 若为「左括号」, 先进栈（栈中存的是下标）, 并且在「标记数组」中将其对应的位置标记为 False
            if char == "(":
                stack.append(i)
                validArr[i] = False
            elif char == ")":
            #* 若为「右括号」, 先判断栈是否为空：
            #* ➊ 若为空, 说明「右括号」在「左括号」之前出现了, 那显然是「无效括号」. 在「标记数组」中标记他的位置
            #* ➋ 若不为空, 说明「右括号」在前面有对应的「左括号」, 那显然不是「无效括号」. 将对应的「左括号」的下标从栈中弹出, 并在「标记数组」中将下标对应的位置重新变为 True
                if len(stack) == 0:
                    validArr[i] = False
                else:
                    idx = stack.pop()
                    validArr[idx] = True
                            
        resArr = []
        for i in range(len(s)):
            if validArr[i] == True:
                resArr.append(s[i])
                
        return "".join(resArr)

