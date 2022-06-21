 
#? https://leetcode.cn/problems/regular-expression-matching/solution/by-flix-musv/
#* dp[i][j] 表示 s 的前 i 个字符和 p 的前 j 个字符能否匹配。

class Solution(object):
    def isMatch(self, s, p):

        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j-1] == "*":
                #* 如果 p[j-1] 是 *，为了匹配此时 s 为空字符串的情况，我们使用p[j-1]来消去p[j-2](因为p[j-1]是*，可以代表0个p[j-2]). 消去后看 空字符串 能否与 p[0: j-3] 匹配，对应dp[0][j-2]
                #! 因为题目中说了 "保证每次出现字符 * 时，前面都匹配到有效的字符" 所以 p[0] 不会是 *, 下面的代码不会出现越界情况
                dp[0][j] = dp[0][j-2]

            
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                #* 如果 p[j-1] 与 s[i-1]相等(意味着p[j]也是一个小写字母a-z) 或者 p[j-1]== '.'(.意味着可以匹配s中的任意任意字符)。则说明 p[j-1] 与 s[i-1] 这两个字符配对成功
                if p[j-1] == s[i-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                #* 当 p[j-1] == * 时，意味着我们要看它的前一位也就是 p[j-2] 与 s[i-1] 的匹配情况，如果他们都是字母(通过使用 p[j-2] != '.'得到)且不相等说明他们俩无法匹配，使用 p[j-1] 也就是 * 来消去 p[j-2]，相当于 p[j-1] = *(代表0个), 然后使用0个p[j-2]相当于消去了它，也就是说 p[j-1] and p[j-2] 一起被消去了。此时我们需要看 s[0: i-1] 与 p[0: j-3] 的匹配情况，也就是 dp[i][j-2] 记住: dp数组的两个维度的大小都是多定义了一位
                    if p[j-2] != "." and s[i-1] != p[j-2]:
                        dp[i][j] = dp[i][j-2]
                    else:
                        #* 这里是指 s[i-1] == p[j-2], 根据上面的公式推导 dp[i][j] = dp[i][j-2] or dp[i-1][j]
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                        
        return dp[-1][-1]
