"""
「」
* 使用滑动窗口
? https://leetcode.cn/problems/string-compression/solution/443ya-suo-zi-fu-chuan-zhi-zhen-hua-dong-nryir/
? 另一种写法: https://leetcode.cn/problems/string-compression/solution/gong-shui-san-xie-shuang-zhi-zhen-yuan-d-bppu/
? 代码借鉴: https://leetcode.cn/problems/string-compression/solution/hua-dong-chuang-kou-fa-ya-suo-zi-fu-chuan-java-by-/
"""


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        left = 0
        right = 0
        write = 0

        strLen = len(chars)
        #! 这里使用『等号』的原因: 遍历到 chars数组「最后一个字符」时也需要结算，因此将右指针的终点设为数组之外一格。这样当右指针移到终点时也能够更新数组。
        while right <= strLen:
            # * 不断移动「右指针」，直到「左指针」指向的字符与「右指针」指向的字符不同时，说明度过了一个/一段相同的字符(这个相同的字符是「左字符」)。此时计算「左字符」出现的次数并通过第三个指针「写指针」将其写入原数组
            if right == strLen or chars[left] != chars[right]:
                # # 「写指针」指向的是下一个在原数组中写入的位置
                chars[write] = chars[left]
                write += 1

                compressLen = right - left
                # * 只有当「左字符」出现次数大于 1 时才需要写入原数组
                if compressLen > 1:
                    for char in str(compressLen):
                        chars[write] = char
                        write += 1
                left = right

            right += 1
        # print(chars)
        return write


Solution().compress(chars=["a", "b", "b"])
