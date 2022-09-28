""" 
* 计算分数到小数, 我们将问题拆解为:
* 
* 如何计算小数的正负号。
* 如何计算小数的小数点前的整数。
* 如何计算小数的小数点后的有限小数 或者 无限循环小数。
* 第一个问题, 如何正负号判断, 分子和分母相乘, 结果如果小于0, 则需要加 − 号。
* 第二个问题, 如何计算小数的小数点前的整数。分子/分母 整数相除得到的结果就是小数点前的整数, 结果可能为0。
* 第三个问题, 如何计算小数的小数点后的有限小数 或者 无限循环小数。模拟除法运算, 即余数*10, 然后 余数 // 分母。注意整除的情况, 即没有小数点后的数字。
* 
* 如果是有限小数, 会在某一步, 出现 分子/分母 整除的情况。
* 如果是无限循环小数, 会在某一步, 出现 分子/分母 的余数等于之前的一步的分子。因此我们可以借助哈希表, 存储之前出现过的分子, 并记录他们的下标。


? 思路: https://leetcode.cn/problems/fraction-to-recurring-decimal/solution/acmjin-pai-ti-jie-mo-ni-chu-fa-yun-suan-p96vg/


? 代码: https://leetcode.cn/problems/fraction-to-recurring-decimal/solution/ji-lu-yu-shu-by-powcai/


   分数  => 商.. 余数  处于结果字符串中的第几位?
   1/7   => 0 .. 1    index=2 (res开头已有0.)      
   10/7  => 1 .. 3      
   30/7  => 4 .. 2      
   20/7  => 2 .. 6      
   60/7  => 8 .. 4      
   40/7  => 5 .. 5      
   50/7  => 7 .. 1    , 发现第一个第2次出现的余数

   """


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return "0"

        res = []

        # * 如果两个数有一个为 "负数", 则最终答案为“负数”, 因此可以起始先判断两数相乘是否小于 0, 如果是, 先往答案头部追加一个负号 -；
        if numerator * denominator < 0:
            res.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        quotient, remainder = divmod(numerator, denominator)
        res.append(str(quotient))

        # * 如果本身两数能够整除, 直接返回即可
        if remainder == 0:
            return "".join(res)

        res.append(".")

        # * 使用「哈希表」记录某个余数最早在什么位置出现过, 一旦出现相同余数, 则在「出现位置」补上 (, 然后在末尾补上 )
        dic = {remainder: len(res)}

        while remainder != 0:

            remainder *= 10
            quotient, remainder = divmod(remainder, denominator)
            res.append(str(quotient))
            # print(remainder)
            # 余数前面出现过, 说明开始循环了, 加左右括号, 并退出循环
            if remainder in dic:
                leftBracketPos = dic[remainder]
                res.insert(leftBracketPos, "(")
                res.append(")")
                break

            dic[remainder] = len(res)

        return "".join(res)
