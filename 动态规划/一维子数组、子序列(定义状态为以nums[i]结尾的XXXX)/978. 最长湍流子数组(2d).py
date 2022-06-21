""" 
* 定义 up[i] 表示以位置 i 结尾的，并且 arr[i] > arr[i - 1] 的最长湍流子数组长度。
* 定义 down[i] 表示以位置 i 结尾的，并且 arr[i] < arr[i - 1] 的最长湍流子数组长度。

? https://leetcode.cn/problems/longest-turbulent-subarray/solution/qing-xi-yi-dong-de-dong-tai-gui-hua-jie-fa-shi-yon/
? 链接：https://leetcode.cn/problems/longest-turbulent-subarray/solution/yi-zhang-dong-tu-xiang-jie-dong-tai-gui-wrwvn/
"""
class Solution(object):
    def maxTurbulenceSize(self, arr):
        if len(arr) < 2:
            return 1
        up = [1 for _ in arr]
        down = [1 for _ in arr]
        result = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                up[i] = down[i-1] + 1
                down[i] = 1
            elif arr[i] < arr[i-1]:
                down[i] = up[i-1] + 1
                up[i] = 1
            else:
                down[i] = 1
                up[i] = 1
            result = max(up[i], down[i], result)
        return result
