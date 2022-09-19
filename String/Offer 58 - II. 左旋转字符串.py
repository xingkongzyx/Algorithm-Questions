
""" 
* 算法流程:
* 1. 新建一个 list(Python)、StringBuilder(Java) ，记为 res 
* 2. 先向 res 添加 "第 n + 1 位至末位的字符"
* 3. 再向 res 添加 "首位至第 n 位的字符"
* 4. 将 res 转化为字符串并返回。
* 复杂度分析:
* 时间复杂度 O(N): 线性遍历 s 并添加，使用线性时间
* 空间复杂度 O(N): 新建的辅助 res 使用 O(N) 大小的额外空间。
? 链接:https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/solution/mian-shi-ti-58-ii-zuo-xuan-zhuan-zi-fu-chuan-qie-p/
"""


class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """

        resArr = []
        for i in range(n, len(s)):
            resArr.append(s[i])

        for i in range(n):
            resArr.append(s[i])

        # print(resArr)
        return "".join(resArr)


Solution().reverseLeftWords(s="lrloseumgh", n=6)
