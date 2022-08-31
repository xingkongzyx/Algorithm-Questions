""" 
* 通过观察我们发现, 只有在遇到特殊情况时 - 两个字符中「左边」的字符代表的数『小于』「右边」的字符代表的数, 那么其结果等于『右边的字符代表的数「减去」左边字符代表的数』。比如 CM 等于 1000 - 100, XC 等于 100 - 10...
* 
* 因此, 我们将 「字符：数值」 存在 record 的哈希表中。然后从左到右遍历每个字符, 如果 record[s[i]] < record[s[i+1]], 就将结果减去 s[i] 代表的数字；否则, 将结果加上 s[i] 代表的数字。

? https://leetcode.cn/problems/roman-to-integer/solution/qing-xi-tu-jie-python3-by-ml-zimingmeng/

"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = {}
        record["I"] = 1
        record["V"] = 5
        record["X"] = 10
        record["L"] = 50
        record["C"] = 100
        record["D"] = 500
        record["M"] = 1000

        """ 
        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.
        """
        sum = 0
        for i in range(len(s) - 1):
            curChar = s[i]
            nextChar = s[i + 1]

            if record[curChar] < record[nextChar]:
                sum -= record[curChar]
            else:
                sum += record[curChar]

        lastChar = s[-1]
        return sum + record[lastChar]
