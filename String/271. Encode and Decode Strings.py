""" 
* 为什么不能使用 "word长度 + word" 的形式进行encode 呢? 因为这样的话一旦 word 本身的第一个字符也是数字, 就无法在 decode 过程中区分这个word 的长度是多少了。例如 ["Hello","World"] => "5Hello5World"✅, ["5Hello","World"] => "65Hello5World"❎, 可以看到第二种情况无法区分word的长度. 
# 所以采用 "word长度 + # + word" 的形式进行 encode, 这样在 decode 的遍历过程中只有遇到 # 才能够确定前面的数字是当前word的长度

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
        start = 0
        wordLen = 0
        res = []
        while start < len(s):
            endIdx = start
            while s[endIdx] != "#":
                endIdx += 1
            wordLen = int(s[start: endIdx])
            wordStartIdx = endIdx + 1
            curWord = s[wordStartIdx: wordStartIdx + wordLen]
            res.append(curWord)
            # update startIdx to the beginning of the next word
            start = wordStartIdx + wordLen
        return res


# Your Codec object will be instantiated and called as such:
codec = Codec()
res = codec.decode(codec.encode(
    ["63/Rc", "h", "BmI3FS~J9#vmk", "7uBZ?7*/", "24h+X", "O "]))

print(res)
