""" 
? https://leetcode.cn/problems/longest-palindrome/solution/409-zui-chang-hui-wen-chuan-by-jyd-ne80/
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 统计字符次数
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        res = 0
        odd = 0
        # 统计构造回文串的最大长度
        for count in dic.values():
            # 【count%2】的目的是, 区分奇数和偶数
            # 符合题目要求中的回文组合中, 总结起来就是【偶数都要, 奇数只计算1次】
            # 如果count是奇数, 【count%2】就会得1, 那【count-rem】就会变成偶数
            # 如果count是偶数, 【count%2】就会得0, 那【count-rem】就还是偶数
            # 按照我们需要【把偶数都要】的结论来说, res里面就计算了【所有字母偶数个的数量】
            # 注意, 奇数的偶数个, 也是算在这里面的, 比如说3算了2进去, 5算了4进去
            remainder = count % 2
            res += count - remainder
        # 再按照我们需要【把奇数只算1次】的结论来说,
        # 当取余数 remainder 为1时, 说明i是奇数, 要算1次奇数, 那就给最后的结果中补偿一个 1
        # 注意, 这条语句会重复执行, 但 odd 始终都为1且不管有几个奇数, odd 都只算进去一次
            if remainder == 1:
                odd = 1
        # 最后返回res和odd的和就是答案
        return res + odd
