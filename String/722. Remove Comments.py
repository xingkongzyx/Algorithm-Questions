""" 
* 「行注释」的影响范围不超过一行, 「块注释」的影响范围可能有多行, 因此在遍历源代码的过程中需要重点记录是否位于「块注释」中。遇到「块注释」时, 「块注释」中的每个字符都应跳过。遇到「行注释」时, 跳过该行的剩余部分即可。
* 如果不在块注释中, 即 inBlock = False
* ① 遇到 "/*" 时, 进入一个块注释, 将标识符设为 true, 跳过这两个字符; 
* ② 遇到 "//" 时, 进入「行注释」, 跳过该行的剩余字符; 将前面记录在 newLine 的字符加入 res 中
* ③ 遇到其他字符时, 该字符为需要保留的字符, 将字符拼接到 newLine; 

? https://leetcode.cn/problems/remove-comments/solution/722-shan-chu-zhu-shi-by-stormsunshine-4u76/
"""


class Solution:
    def removeComments(self, source):
        # * 标识符用于记录当前是否在在注释中
        inBlock = False
        res = []
        for line in source:
            # * newLine 用于储存当前行删除注释之后的代码
            if not inBlock:
                # / 为什么只有不在「块注释」状态时才创建新的当前行代码呢？如果「块注释」是多行的并且头尾两行 "/**/" 块注释外还有其他有效代码, 不能将其舍弃, 而应该记录在一起
                newLine = []
            charIdx = 0
            while charIdx < len(line):
                # * 如果在「块注释」中, 即 inBlock = True。遇到 "*/" 时, 上一个块注释结束, 将标识符设为 False, 跳过这两个字符; 遇到其他字符时, 则继续遍历。
                if inBlock:
                    if charIdx + 1 < len(line) and line[charIdx:charIdx + 2] == "*/":
                        inBlock = False
                        # * 继续找下去,这里实际要+2, 但是charIdx在后面有 +1 的代码
                        charIdx += 1
                else:
                    """ 
                    * 如果不在「块注释」中, 即 inBlock = False
                    * ① 遇到 "/*" 时, 进入一个「块注释」, 将标识符设为 true, 跳过这两个字符; 
                    * ② 遇到 "//" 时, 进入「行注释」, 跳过该行的剩余字符; 将前面记录在 newLine 的字符加入 res 中
                    * ③ 遇到其他字符时, 该字符为需要保留的字符, 将字符拼接到 newLine; 
                    """
                    if charIdx + 1 < len(line) and line[charIdx:charIdx + 2] == "/*":
                        inBlock = True
                        # * 继续找下去,这里实际要+2, 但是charIdx在后面有 +1 的代码
                        charIdx += 1
                    elif charIdx + 1 < len(line) and line[charIdx:charIdx + 2] == "//":
                        break
                    else:
                        newLine.append(line[charIdx])
                        # print(newLine)
                charIdx += 1

            # ! 为什么只有在 not inBlock 时才能够加入 newLine 呢, 防止 source = ["a/*comment", "line", "more_comment*/b"] 的情况, 如果不判断此时是否在「块注释」中, 那么在第一次第二次遍历的时候即使处于「块注释」中仍旧会把 newLine = "a" 加入到 res 中, 导致 res 的结果变为 ["a", "a", "ab"] 而不是正确的 ["ab"]
            if len(newLine) > 0 and inBlock == False:
                res.append(''.join(newLine))

        return res
