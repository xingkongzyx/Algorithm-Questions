""" 
* 直观的一种想法就是按照 z 字形遍历 s; 根据 z 字形的特点, 将每个字母放到对应的行。
* 思路就是通过两个变量, 一个变量flag 记录当前的前进方向是向上还是向下, 另一个变量 rowIdx 记录当前在第几行的索引, 循环往复就行了. 
* 具体体现在代码中每次通过 += flag 更新行索引; 触底时向相反方向移动, 通过反转 flag 变量(flag = -flag) 实现

? flix 的解: https://leetcode.cn/problems/zigzag-conversion/solution/zhu-zi-bian-li-zhu-xing-bian-li-zzi-xing-5p7e/
? k神 的解: https://leetcode.cn/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/
"""


class Solution(object):
    def convert(self, s, numRows):
        # * 给定行数为 1 时结果与原字符串一样
        # ! 此时绝对不能进入下边的循环, 否则会出现 "list index out of change", 因为 rowIdx 无论如何都会进入等于1的情况，导致超出界限
        if numRows < 2:
            return s

        # * 创建 res 保存每行结果
        res = ["" for _ in range(numRows)]

        # * 往上走还是往下走的标志
        flag = -1

        # * 代表向 res 中的哪一行添加字符
        rowIdx = 0
        for charIdx in range(len(s)):
            curChar = s[charIdx]
            # print(f"rowIdx is {rowIdx}, flag is {flag}, curChar is {curChar}")
            res[rowIdx] += curChar
            if rowIdx == numRows - 1 or rowIdx == 0:
                flag = -flag
            rowIdx += flag

        # * 将每行接起来就是结果
        return "".join(res)


Solution().convert(s="leetcode", numRows=3)
