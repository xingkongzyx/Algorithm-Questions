""" 
> 本题使用「滑动窗口」太难实现, 所以使用「分治 - divide and conquer」

* 分治核心思想: 如果某个字符 x 在整个字符串中出现的次数 <k, 那么 x 不可能出现在最终要求的子串中。因此, 可以将原字符串截断为: "「x 左侧字符子串」+「x」+ 「x 右侧字符子串」"
* 因此, 问题就被拆分为对左子串、右子串递归地求解这两个子问题。
? https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/solution/dong-tai-gui-hua-python-di-gui-by-jalan/


* 本题的「递归函数」 longestSubstring(s, k) 函数表示的是: 求一个最长的「子字符串」的长度, 该「子字符串」中每个字符出现的次数都「最少为 k」。
/ 时间复杂度: O(N * 26 * 26), 因为函数最多执行 26 次, for循环遍历一次是26个字符, 循环里面对 s 分割时间复杂度是O(N)。

? https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/solution/jie-ben-ti-bang-zhu-da-jia-li-jie-di-gui-obla/
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        # # 递归终止条件: 如果字符串 s 的长度少于 k, 那么一定不存在满足题意的子字符串, 返回 0；
        if len(s) < k:
            return 0

        # * 源字符串中每个字符出现的次数存入map中
        freq_map = {}

        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1

        for key in freq_map:
            # * 如果一个字符 key 在 s 中出现的次数「少于 k 次」, 那么 s 中所有的包含 key 的「子字符串」都不能满足题意。所以, 应该在 s 的所有不包含 key 的「子字符串」中继续「继续使用递归函数」寻找结果。返回其中长度最大的结果
            if freq_map[key] < k:
                res = 0
                split_str_arr = s.split(key)
                for split_str in split_str_arr:
                    res = max(res, self.longestSubstring(split_str, k))
                return res

        # * 如果 s 中的每个字符出现的次数都大于 k 次, 那么 s 就是我们要求的字符串, 直接返回该字符串的长度。
        return len(s)
