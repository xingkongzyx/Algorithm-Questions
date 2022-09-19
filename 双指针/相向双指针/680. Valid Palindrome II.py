""" 
* 从左右两端使用双指针验证是否是回文串, 若某一刻, 左右两边对应的字符不相等的, 选择跳过左边或者右边的一个字符, 再去验证一遍。这两种跳过情况只要有一种满足回文串, 就返回 True
? 图解: https://leetcode.cn/problems/valid-palindrome-ii/solution/shuang-zhi-zhen-on-shi-jian-fu-za-du-by-cyc2018-2/
? 代码借鉴: https://leetcode.cn/problems/valid-palindrome-ii/solution/shan-chu-zuo-zhi-huo-you-zhi-zhen-zi-fu-pan-duan-s/   
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def checkPal(s, left, right):
            while left < right:
                # * 在删掉一个字符后的第二次判断中, 如果指向的字符不一样, 就不是回文串, 返回 False
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1

        while left < right:
            # * 主函数中, 如果指向的字符不一样, 还不能死刑。转为判断删掉(左边或者右边)一个字符后, 剩下没检查的字符是否满足回文要求
            if s[left] != s[right]:
                delLeftCharRes = checkPal(s, left + 1, right)
                delRightCharRes = checkPal(s, left, right - 1)

                return delLeftCharRes or delRightCharRes

            left += 1
            right -= 1

        return True
