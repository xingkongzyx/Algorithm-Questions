
#? https://leetcode.cn/problems/find-k-closest-elements/solution/pai-chu-fa-shuang-zhi-zhen-er-fen-fa-python-dai-ma/
class Solution(object):
    def findClosestElements(self, arr, k, x):
        length = len(arr)
        # 确定要删除的元素的个数
        deletedCount = length - k
        left = 0
        right = len(arr) - 1
        # 每次循环都会删除一个元素，所以通过需要删除的元素的个数确定循环终止条件
        while deletedCount > 0:
            # 求得左右指针指向位置与 x 的距离，保留离得近的，通过调整index的方式达成删除操作
            leftDistance = abs(arr[left] - x)
            rightDistance = abs(arr[right] - x)
            if leftDistance < rightDistance:
                right -= 1
            elif leftDistance > rightDistance:
                left += 1
            else:
                right -= 1
            deletedCount -= 1
        
        return arr[left:right + 1]

Solution().findClosestElements([1,2,3,4,5], 4, -1)
            