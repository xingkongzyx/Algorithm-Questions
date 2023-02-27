""" 
* 为什么不能使用 "word长度 + word" 的形式进行encode 呢? 因为如果 word 本身的第一个字符也是数字, 就无法在 decode 过程中区分这个 word 的长度是多少了。例如 ["Hello","World"] => "5Hello5World" ✅, ["5Hello","World"] => "65Hello5World" ❎, 可以看到第二种情况无法区分第一个单词 "5hello" 的长度. 
# 所以采用 "word长度 + #(任意特殊字符都可以) + word" 的形式进行 encode, 这样在 decode 的遍历过程中只有遇到 # 才能够确定前面的数字是当前word的长度

? https://www.youtube.com/watch?v=B1k_sxOSgv8
"""


class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """
        res_arr = []
        for word in strs:
            word_len = len(word)
            res_arr.append(str(word_len))
            res_arr.append("#")
            res_arr.append(word)
        return ''.join(res_arr)

    def decode(self, s: str):
        """Decodes a single string to a list of strings.
        """
        print(s)
        preword_start = 0
        wordLen = 0
        res = []
        while preword_start < len(s):
            preword_end = preword_start
            while s[preword_end] != "#":
                preword_end += 1
            # * 到达这行时, preword_end 的值是 "#" 的位置, preword_end + 1 则是单词真正的第一个字符的位置
            wordLen = int(s[preword_start: preword_end])
            realWordStartIdx = preword_end + 1
            realWordEndIdx = realWordStartIdx + wordLen - 1
            # * [realWordStartIdx, realWordEndIdx - 1] 左闭右闭是这个单词所在的位置区间
            curWord = s[realWordStartIdx: realWordEndIdx + 1]
            res.append(curWord)
            
            # * update preword_start to the beginning of the next word, preword_start 更新到下个单词的前面的代表单词长度的位置
            preword_start = realWordEndIdx + 1
        return res


# Your Codec object will be instantiated and called as such:
codec = Codec()
res = codec.decode(codec.encode(
    ["63/Rc", "h", "BmI3FS~J9#vmk", "7uBZ?7*/", "24h+X", "O "]))

print(res)
