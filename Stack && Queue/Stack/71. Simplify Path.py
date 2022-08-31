""" 
* 使用栈进行模拟即可。
* 具体的, 先把字符串以 "/" 为分隔符分割成数组 pathArr, 此时数组有「路径」,「..」,「」,「.」 这四种情况;
* 然后从前往后处理 pathArr, 每次以 item 为单位进行处理（有效的文件名）, 根据 item 为何值进行分情况讨论: 
* ➀ item 为「路径」: 存入栈中；
* ➁ item 为 「..」: 因为 「..」表示上级路径，因此如果栈顶有元素的话，要将其弹出，表示切换到上级目录
* ➂ item 为 「」或者「.」: 不作处理。

? 链接: https://leetcode.cn/problems/simplify-path/solution/gong-shui-san-xie-jian-dan-zi-fu-chuan-m-w7xi/
? https://leetcode.cn/problems/simplify-path/solution/jian-hua-lu-jing-by-leetcode-solution-aucq/
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathArr = path.split("/")
        stack = []

        for ele in pathArr:
            # * 对应情况 ➂
            if ele == "." or ele == "":
                continue
            # * 对应情况 ➁
            if ele == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                # * 对应情况 ➀
                stack.append(ele)

        # * 如果栈是空的, 返回 "/". 否则, 我们将从栈底到栈顶的字符串用 / 进行连接，再在最前面加上 / 表示根目录，就可以得到简化后的规范路径。
        return "/" + "/".join(stack)


print(Solution().simplifyPath("/..."))
