""" 
! 与 402 非常类似
? 讲解的好(可以看程序的执行流程的图片): https://leetcode.cn/problems/remove-duplicate-letters/solution/zhan-by-liweiwei1419/ 
? 代码来源: https://leetcode.cn/problems/remove-duplicate-letters/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-4/
* 与上面题目不同, 这道题没有一个「全局」的删除次数 k. 而是对于每一个在字符串 s 中出现的字母 c 都有一个要删除的次数 k. 这个 k 是 c 在 s 中总的出现次数 - 1(减 1 是因为题目要求在新字符串中 c 只出现一次. ). 

/ 时间复杂度: O(N), 其中 N 为字符串长度。代码中虽然有双重循环, 但是每个字符至多只会入栈、出栈各一次。
/ 空间复杂度: O(|Σ|), 其中 Σ 为字符集合, 本题中字符均为小写字母, 所以 |Σ|=26。由于栈中的字符不能重复, 因此栈中最多只能有 |Σ| 个字符.


"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remain_counter = {}
        stack = []
        for char in s:
            remain_counter[char] = remain_counter.get(char, 0) + 1
        """ 
        * 题目中有个非常重要的要求: 原字符串 s 中的「每个字符」都需要出现在「新字符串」中, 且「只能出现一次」. 为了让「新字符串」满足该要求, 算法需要进行以下两点操作
        * ➀ 在考虑字符 s[i] 时, 如果它已经存在于栈中, 则不能向栈中继续加入字符 s[i]. 为此, 『需要记录每个字符是否出现在栈中』. 这也是使用 seen 的原因
        * ➁ 在弹出「栈顶字符」时, 如果字符串在后面的位置上再也『没有』这一字符, 则不能弹出栈顶字符. 为此, 需要记录每个字符的『剩余数量』, 当这个值为 0 时, 就不能弹出「栈顶字符」了. 
        """
        charInStack = set()
        
        for char in s:
            """ 
            * 在考虑字符 s[i](也就是这里的 char) 时, 如果它已经存在于栈中, 则不能向栈中继续加入字符 s[i](也就是这里的 char).
            * 如果遍历到当前栈中已经有的字符，可以舍弃当前遍历到的字符, 为什么呢? 
            # 既然已经出现在栈中的元素，不可能是「某个单调递增段」的「最后一个元素」，因此如果丢弃之前遇到的那个相同字符，它紧挨着的下一个字符的 ASCII 值更大。ASCII 值更大的字符靠前一位，整体字典序更大。因此应该丢弃当前遇到的相同字符。例如栈中此时的「某个单调递增段」是 "abd",「最后一个元素」是 d(在 s 中只出现一次), 遍历 s 时又遇到了另一个 b, 如果选用这个 b 而弹出前一个 b, 那么新的字符串变为 "adb", 反而更大了
            ?https://leetcode.cn/problems/remove-duplicate-letters/solution/zhan-by-liweiwei1419/

            """
            if char not in charInStack:
                #* 在弹出「栈顶字符」时, 如果字符串在后面的位置上再也『不会出现』这一「栈顶字符」, 代码对应是 "remain_counter[stack[-1]] > 0", 则不能弹出「栈顶字符」, 必须保留它才能满足 "原字符串 s 中的「每个字符」都需要出现在「新字符串」中".
                while len(stack) > 0 and remain_counter[stack[-1]] > 0 and stack[-1] > char:
                    poppedChar = stack.pop()
                    charInStack.discard(poppedChar)
                stack.append(char)
                charInStack.add(char)
            
            #* 这个remain_counter无论什么情况都要更新，它是用来记录后面的字符串中各个字符剩余的出现次数
            remain_counter[char] -= 1
                
        return "".join(stack)
