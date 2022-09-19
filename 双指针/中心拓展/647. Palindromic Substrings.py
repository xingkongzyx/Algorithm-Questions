""" 
* 回文串有两种形式
* 
* 回文串长度为奇数时, 如 "aba" 以 b 为中心构成回文串, 即奇数中心是长度为 1 的子序列
* 回文串长度为偶数时, 如 "abba" 以 bb 为中心构成回文串, 即偶数中心是长度为 2 的子序列
* 所以对于每个序列的每个位置（即拓展中心）都有两种不同的拓展方式, 一种是以奇数方式拓展, 一种是以偶数方式拓展。
* 我们依次对单个字母和两个字母进行扩散出去，来算出每种情况的回文子串的个数，最后相加就可以了
? 代码参考: https://leetcode.cn/problems/palindromic-substrings/solution/c-zhong-gui-zhong-ju-de-4msjie-fa-zhong-xin-kuo-zh/
? https://leetcode.cn/problems/palindromic-substrings/solution/shu-ju-jie-gou-he-suan-fa-dong-tai-gui-h-3bms/

"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        # left 往左边跑, right 往右边跑, 判断 s[left, right]是否为回文, 是的话回文串数量加 1
        def palindromeHelper(left, right):
            nums = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                nums += 1
                left -= 1
                right += 1
            return nums
        ans = 0
        for i in range(len(s)):
            # //以单字母为中心
            ans += palindromeHelper(i, i)
            # //以双字母为中心
            ans += palindromeHelper(i, i + 1)

        return ans
