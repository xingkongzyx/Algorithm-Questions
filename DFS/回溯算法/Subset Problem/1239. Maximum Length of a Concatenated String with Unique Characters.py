""" 
* 属于子集类问题
? https://leetcode.cn/problems/maximum-length-of-a-concatenated-string-with-unique-characters/solution/chi-xiao-dou-python-po-su-de-hui-su-fa-b-yosv/
? https://leetcode.cn/problems/maximum-length-of-a-concatenated-string-with-unique-characters/solution/chuan-lian-zi-fu-chuan-de-zui-da-chang-d-ln2v/
"""


class Solution:
    def maxLength(self, arr) -> int:
        candidates = []
        # * 将 arr 中由重复字符组成的字符串元素直接丢弃，不放在 candidates 中
        for ele in arr:
            flag = True
            charSet = set()
            for char in ele:
                if char in charSet:
                    flag = False
                    break
                else:
                    charSet.add(char)

            if flag == True:
                candidates.append(ele)

        # ! 下面是子集问题
        maxLen = 0
        curPath = []
        # print("candidates: ", candidates)

        def backtracking(startIdx):
            # * 直接set()检查是否需要剪枝，每一步都存储下s最大值作为最后答案
            curStr = ''.join(curPath)
            curSet = set(curStr)
            if len(curSet) == len(curStr):
                # print(curStr)
                nonlocal maxLen
                maxLen = max(maxLen, len(curStr))
            else:
                return

            for i in range(startIdx, len(candidates)):
                curPath.append(candidates[i])
                backtracking(i + 1)
                curPath.pop()

            return

        backtracking(0)
        return maxLen
# candidates:  ['jnfbyktlrqumowxd', 'mvhgcpxnjzrdei']
