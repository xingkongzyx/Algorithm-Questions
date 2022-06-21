
#? https://suanfa8.com/binary-search/solutions/find-index/0658-find-k-closest-elements/
#! 本题使用二分查找法在有序数组中定位含有 k 个元素的连续子区间的左边界，即使用二分法找“最优区间的左边界”。
class Solution(object):
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
                
        return arr[left: left + k]

