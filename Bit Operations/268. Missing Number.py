""" 
simplifying a^b^b =a: 
① (anything ^ anything) = 0, and (anything ^ 0) remains same thing
② b^b -> 0
③ a^0 -> a
* We know that a^b^b =a, which means two xor operations with the same number will eliminate the number and reveal the original number.
* In this solution, I apply XOR operation to both the index and value of the array. In a complete array with no missing numbers, the index and value should be perfectly corresponding(nums[index] = index), so in a missing array, what left finally is the missing number. 

/ Time Complexity: O(N)
/ Space Complexity : O(1)
? https://leetcode.com/problems/missing-number/solutions/69791/4-line-simple-java-bit-manipulate-solution-with-explaination/?orderBy=most_votes
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0

        for i in range(len(nums)):
            # 先和 i 进行异或操作
            xor = xor ^ i
            # 再和 nums[i] 进行异或操作
            xor = xor ^ nums[i]
        # 因为检查的区间是 [0, len(nums)], 所以最后还要再进行一次 xor
        res = xor ^ len(nums)
        return res
