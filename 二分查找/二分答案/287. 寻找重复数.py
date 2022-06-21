""" 
? https://leetcode.cn/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/

* 为何没有经过排序的数组也可以用二分查找呢？
* 因为 1-n 这个范围是有序的, 对这个范围进行二分查找, 然后选取 1-n 中的 mid 去原数组(也就是输入数组 nums)中统计小于等于它的有多少个数, 直到left==right

! 这个问题使用「二分查找」是在数组 [1, 2,.., n] 中查找一个整数，而 并非在输入数组中使用二分查找查找一个整数。在输入数组中是根据本轮二分查找的mid进行线性统计

/ 时间复杂度: O(NlogN)，二分法的时间复杂度为 O(logN)，在二分法的内部，执行了一次 for 循环，时间复杂度为 O(N)，故时间复杂度为 O(NlogN)。
/ 空间复杂度: O(1)，使用了一个 cnt 变量，因此空间复杂度为 O(1)。
 """
class Solution:
    def findDuplicate(self, nums) -> int:
        left = 1
        right = len(nums)
        #* 在数组 [1, 2,.., n] 中使用二分查找，找到中间数 mid, 然后在输入数组中查看小于等于 mid 的元素的数量记为 count, 如果 count 大于 mid (例如 mid 是 3，输入数组的所有元素在 [1..3] 这个区间中没有重复的数字的话的话应该有3个数，如果输入数组在这个范围中有重复数字的话，则 "小于等于 mid 的元素的数量 count" 肯定大于3，就可以判断重复的数字发生在 [left, mid] 这个范围中)
        
        while left < right:
            mid = left + (right - left) // 2
            
            count = self.getCount(nums, mid)
            
            if count > mid:
                #* 下一轮搜索区间 [left, mid]
                right = mid
            else:
                #* 下一轮搜索区间 [mid + 1, right]
                left = mid + 1
        return left
    
    def getCount(self, nums, target):
        count = 0
        for num in nums:
            if num <= target:
                count += 1
        return count
        
 
print(Solution().findDuplicate([1,3,4,2,2]))
