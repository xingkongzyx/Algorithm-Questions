

""" 
# 很关键的信息就是每艘船最多可同时载两人, 意味着不可能「三个体重之和小于limit的人」一起登船, 两个人的一起登船话最轻与最重一起组队登船是最划算的
* 贪心的简单说明: 观察这么一件事儿，越重的人，越容易自己独占一条船。如果想尽可能地利用空间，就尽可能往它们上面塞人。
* 如果最重的，重到连最轻的都加不上去，那它只能自己一个人一条船。剩下的问题就是一个递归的解了;
! 如果最重的可以带上最轻的，那它们俩一艘船是最优的。因为最轻的能和任一个人一起，但其他人不一定能和最重的人一起。
* 我们猜想这样「最重匹配最轻、次重匹配次轻」的做法能使双人船的数量最大化。

? 证明(可忽略): https://leetcode.cn/problems/boats-to-save-people/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-hosg8/

"""
class Solution(object):
    def numRescueBoats(self, people, limit):
  
        people.sort()
        count = 0
        left = 0
        right = len(people) - 1
        
        while left <= right:
            if people[left] + people[right] > limit:
                count += 1
                right -= 1
            else:
                left += 1
                right -= 1
                count += 1
        return count

print(Solution().numRescueBoats(people = [3,2,2,1], limit = 3))
