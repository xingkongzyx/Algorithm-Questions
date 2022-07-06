""" 
* 可以使用滑动窗口的原因：如果一个连续子数组的和 ≥ target ，又因为题目中给出的数组是正整数数组，左端点固定长度更长的子串一定满足 和 ≥ target ，相当于是左端 l=x 的所有情况都被考虑到了，接下来要考虑 l=x+1 的情况了。并且题目也要求找最短子数组，此时左端点需要右移。符合滑动窗口性质：向右边扩散得到和越来越大，向左边界扩散得到和越来越小。
> 与 76 相似
! 循环不变量是 [left, right) 之间的数字和 < target
/ 时间复杂度：右指针遍历了数组一次、左指针还没有遍历到数组的末尾就停了下来，因此时间复杂度为 O(N)。
? https://suanfa8.com/sliding-window/01/0209-minimum-size-subarray-sum/#
"""
class Solution(object):
    def minSubArrayLen(self, target, nums):
        ## Step 1: 定义需要维护的变量, 本题求最小长度，所以需要定义 minLen, 本题又涉及求和，因此还需要一个sum变量
        sum = 0
        minLen = float('inf')
        
        ## Step 2: 定义窗口的首尾端 (left, right)， 然后滑动窗口
        left = 0
        right = 0
        
        while right < len(nums):
            rightNum = nums[right]
            sum += rightNum
                        
            ## Step 4
            ## 这一题这里稍微有一点特别: sum >= target其实是合法的，但由于我们要求的是最小长度，
            ## 所以当 sum 已经大于等于 target 的时候继续移动右指针没有意义，因此还是需要移动左指针慢慢逼近答案. 由于左指针的移动可能影响 minLen 和 sum 的值，因此需要在移动前将它们更新
            while sum >= target:  
                minLen = min(minLen, (right- left + 1))             
                leftNum = nums[left]
                sum -= leftNum
                left += 1
                
            right += 1
        return 0 if minLen == float('inf') else minLen
            
