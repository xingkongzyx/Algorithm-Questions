""" 
> 更加纯正的双指针解法
? https://leetcode.cn/problems/string-compression/solution/tong-ge-lai-shua-ti-la-du-xie-zhi-zhen-m-n0gt/

* write 指针永远指向下一个要写入的位置
* 每次外层的 while 循环结束后 read 都指向下一段待处理字符的起始位置
* 在 while 循环内部设定一个辅助的 readLeftIdx 指针用于确定当前这一段待处理字符的左边界。因为 write指针 跟不上 read指针, 所以无法用于记录当前要处理的字符，write pointer 只能记录写入位置。 而 read指针 在经历内部的 while 循环后, 指向了一段相同字符的最后一个位置。此时当前待处理字符是 "curChar = chars[readLeftIdx]", 当前待处理字符的出现次数是 "curCharFreq = read - readLeftIdx + 1". 
* curChar 无论什么情况都得写入 chars, 而 curCharFreq 只有在大于 1 的时候才需要写入。
"""


class Solution(object):
    def compress(self, chars):
        read = 0
        write = 0

        while read < len(chars):
            readStart = read

            while read + 1 < len(chars) and chars[read + 1] == chars[read]:
                read += 1

            curChar = chars[readStart]
            curCharFreq = read - readStart + 1

            chars[write] = curChar
            write += 1
            if curCharFreq > 1:
                for num in str(curCharFreq):
                    chars[write] = num
                    write += 1

            read += 1

        # * 返回写指针的位置即结果
        return write
