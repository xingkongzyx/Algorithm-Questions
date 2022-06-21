class Solution:
    """ 
    *因为待查找的是极大值点，所以我们可以根据mid中点的情况来判断极大值的情况
    *若中点值比右方值大，说明极值点在中点左侧(包括中点)
    *若中点值比右方小，说明极值点在中点右侧(不包括中点)
    ! 实际二分需要查找的下标ans是数组中满足 array[i] > array[i+1] 的最小下标


    * 在 arr[mid] < arr[mid + 1] 的时候，mid 以及 mid 的左边一定不存在山脉数组的「峰顶」，封顶只可能存在于下标区间 [mid + 1..right] ，此时设置 left = mid + 1； * 否则，就在下标区间 [left..mid] 里查找答案，此时设置 right = mid。
    Link: https://suanfa8.com/binary-search/solutions/find-index/0852-peak-index-in-a-mountain-array/
    """
    def peakIndexInMountainArray(self, arr) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
