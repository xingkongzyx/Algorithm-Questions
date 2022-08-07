""" 
「」
# * 如果 s 中有连续的「左括号」我们删除其中哪一个都是一样的, 如 "(()" 删除第一个 "(" 或删除第二个 "(" 得到的结果都是 "()", 需要去重. 我们直接用一个 set 进行结果去重.
? 要与不要的回溯代码: https://leetcode.cn/problems/remove-invalid-parentheses/solution/tong-ge-lai-shua-ti-la-yi-bu-bu-shen-du-jvrgz/
? 比官解思路更清晰: https://leetcode.cn/problems/remove-invalid-parentheses/solution/luo-ji-chai-jie-yi-ge-dfsde-xin-lu-li-ch-j97y/

? 代码借鉴: https://leetcode.cn/problems/remove-invalid-parentheses/solution/shan-chu-wu-xiao-de-gua-hao-by-leetcode-9w8au/
? 代码借鉴2: https://leetcode.cn/problems/remove-invalid-parentheses/solution/dfsjie-ti-by-hw_wt/
"""


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # * 「左括号」和「右括号」各自最少应该删除的数量。
        delLeftBrackets = 0
        delRightBrackets = 0

        for char in s:
            if char == "(":
                # # 遇到「左括号」直接更新需要删除的左括号数量；
                delLeftBrackets += 1
            elif char == ")":
                # # 如果此时需要删除的「左括号」数量为 0, 说明没有多余的「左括号」, 此时遇到「右括号」一定是匹配不了的, 也是需要删除的, 所以需要删除的「左括号」的数量减 1
                if delLeftBrackets == 0:
                    delRightBrackets += 1
                # # 如果此时需要删除的「左括号」数量不为 0, 说明有多余的左括号, 此时遇到「右括号」是可以匹配的, 所以需要删除的「左括号」的数量减 1, 减去的 1 用于匹配目前遇到的「右括号」
                else:
                    delLeftBrackets -= 1

        resSet = set()
        # * 用于满足题目中的「示例3」: s = ")(", res = [""]
        sArr = list(s) + [""]

        def backtracking(leftCount, rightCount, start):
            # * 递归终止条件: 需要删除的左右括号数量都为 0 时, 检查此时的字符数组 sArr 是否是合法的
            if leftCount == 0 and rightCount == 0:

                if self.checkValid(sArr):
                    resSet.add("".join(sArr))
                return

            # * 在原始字符串上面进行删除操作, 遍历可以删除的字符位置 [start,  len(s) - 1], 对应字符为「左右括号」时, 分别删除并进行递归, 直到不合法个数为0
            for i in range(start, len(sArr)):
                #! 剪枝操作: 在循环删除的时候, 如果下一个字符和上一次回溯结束后的字符一样时, 不需要再重复处理
                if i > 0 and sArr[i] == sArr[i - 1]:
                    continue
                delChar = sArr[i]
                if sArr[i] == "(" and leftCount > 0:
                    leftCount -= 1
                    sArr.pop(i)
                    # * 因为上面删除了 sArr[i], 所以此时的 i 就直接成为下一轮递归的起始位置, 而不用传入 i + 1
                    backtracking(leftCount, rightCount, i)
                    # * 回溯
                    sArr.insert(i, delChar)
                    leftCount += 1
                elif delChar == ")" and rightCount > 0:
                    rightCount -= 1
                    sArr.pop(i)
                    # * 因为上面删除了 sArr[i], 所以此时的 i 就直接成为下一轮递归的起始位置, 而不用传入 i + 1
                    backtracking(leftCount, rightCount, i)
                    # * 回溯
                    sArr.insert(i, delChar)
                    rightCount += 1

        backtracking(delLeftBrackets, delRightBrackets, 0)

        resList = list(resSet)

        return resList

    def checkValid(self, arr):
        stack = []
        for ele in arr:
            if "a" <= ele <= "z":
                continue
            if ele == "(":
                stack.append(ele)
            elif ele == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                stack.pop()

        return len(stack) == 0
