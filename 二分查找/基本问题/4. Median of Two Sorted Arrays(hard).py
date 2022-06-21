
# ? https://leetcode.cn/problems/median-of-two-sorted-arrays/solution/he-bing-yi-hou-zhao-gui-bing-guo-cheng-zhong-zhao-/ 
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        size_left_total = (m + n + 1) // 2
        # 数组是奇数时,中位数就是中位数,size左 = size右 + 1(包括进去中位数) size右最小索引 为i
        # 数组为偶数时,中位数分左右中位数,size左 = size右 size 右最小索引为i
        left = 0
        right = m    

        # find i and j
        while left < right:
            i = (left + right) // 2 # 得到的是中位数的索引,或者是右中位数的索引
            j = size_left_total - i
            #print('i,j:', i, j)
            if nums2[j - 1] > nums1[i]:       
               # nums2 的左边最大的数比 num1 右边最小的数要大,说明边界线i需要右移
               # left 需要变大,i在[left ,right ]里面选择
                left = i + 1    # i+1 如果进入死循环,则选i+1 否则 i
            else:
                right= i   #i 或者 i -1

        # i and j have been found
        i = right
        j = size_left_total - i

        nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
        nums1_right_min = float('inf') if i == m else nums1[i]
        
        nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
        nums2_right_min = float('inf') if j == n else nums2[j]

        if (m + n) & 1:  # 数组总和数量为奇数
            return max(nums1_left_max, nums2_left_max)
        else:
            return float((max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2)
