"""
* 活用任何人都认识名人, 但名人不认识任何人这一特性
* 如果 knows(i,j) 为 ture, 说明i不可能是名人
* 如果 knows(i,j) 为 false,  说明j不可能是名人
* 也就说任意两人相互比较总能淘汰一个人。
* 这样就可以在线性时间内找到名人, 最简单的方法是迭代一遍数组
* 
* 但是数组中可能不存在名人, 因此需要对第一遍得到的候选人进行校验
* 校验方法是 判断数组中每个i 如果 knows(candidate, i) 或者 knows(i, candidate) 则说明 candidate 也不是名人, 返回-1; 

? 概念: https://leetcode.cn/problems/find-the-celebrity/solution/c-148ms-93mb-by-danikarry-umhd/

? 双指针代码借鉴(必看): https://leetcode.cn/problems/find-the-celebrity/solution/c-shuang-zhi-zhen-by-qiank-06mo/
"""


class Solution:
    def findCelebrity(self, n: int) -> int:
        left = 0
        right = n - 1

        while left < right:
            if knows(left, right) == True:
                left += 1
            else:
                right -= 1

        # * 上面的循环后, left 和 right 会相遇, 这个人是潜在的名人
        # * 再遍历数组按照定义验证：
        # * case1：候选人认识其他人, 那么他不是名人
        # * case2：存在至少一个人不认识候选人, 那么他也不是名人

        candidate = left
        for i in range(n):
            if i != candidate and knows(i, candidate) == False:
                return -1

        for i in range(n):
            if i != candidate and knows(candidate, i) == True:
                return -1

        return candidate
