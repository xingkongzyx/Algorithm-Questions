""" 
> 这道题属于使用哈希表的贪心算法
* 贪心法则：我们每次尽可能优先使用「较大数值」对应的字符。 比如对于 1994 这个数, 如果我们每次尽量用最大的数来表示, 依次选 1000, 900, 90, 4, 会得到正确结果 MCMXCIV。

* 所以, 我们将哈希表按照从大到小的顺序排列, 然后遍历哈希表, 直到表示完整个输入。
/ 时间复杂度: O(1)。最坏条件下, 循环的次数为哈希表的长度。
/ 空间复杂度: O(1)。
? 最详细讲解: https://leetcode.cn/problems/integer-to-roman/solution/tan-xin-suan-fa-by-liweiwei1419/
? 说明2: https://leetcode.cn/problems/integer-to-roman/solution/tan-xin-ha-xi-biao-tu-jie-by-ml-zimingmeng/
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        # * 把阿拉伯数字与罗马数字可能出现的所有情况和对应关系, 放在两个数组中, 并且按照阿拉伯数字的大小降序排列
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC",
                  "L", "XL", "X", "IX", "V", "IV", "I"]
        index = 0
        res = ""
        while index < len(nums):
            curNum = nums[index]
            #! 特别注意：这里是『等号』, 因为只有最后确保 num 是 0 才能正确且完整的表示这个数
            while num >= curNum:
                num -= curNum
                res += romans[index]

            index += 1

        return res
