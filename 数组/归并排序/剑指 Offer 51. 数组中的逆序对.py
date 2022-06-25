
#? k神的: https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/jian-zhi-offer-51-shu-zu-zhong-de-ni-xu-pvn2h/
#? 带类似题型的: https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/4chong-jie-fa-yi-wang-da-jin-you-xu-shu-0nia5/ 
class Solution(object):
    # 先计算两个子区间内部的逆序对的个数，然后在合并的过程中计算跨越两个子区间的逆序对的个数
    def reversePairs(self, nums):
        #* 如果数组中只有1个元素或者为空，则不存在逆序对
        if len(nums) < 2:
            return 0
        tempArr = [0 for _ in nums]
        
        count = self.calculatePairs(0, len(nums) - 1, nums, tempArr)
        
        return count
    
    def calculatePairs(self, leftBound, rightBound, arr, tempArr):
        #* 当只有一个节点的时候，直接返回，退出递归
        if leftBound == rightBound:
            return 0
        left = leftBound
        right = rightBound
        mid = left + (right - left) // 2
        
        #* 分别使用递归计算两个子数组中的逆序对的数量，且顺带将左右子区间按从小到大排序好了
        leftPairs = self.calculatePairs(left, mid, arr, tempArr)
        rightPairs = self.calculatePairs(mid + 1, right, arr, tempArr)
        
        #* 用于记录两个子数组「合并排序」过程中产生的逆序对的数量，与上面的两个相加便是全部的逆序对的数量
        crossPairs = 0
        #* 先复制未合并前的 nums 数组到 tempArr 中。当然，此时的 nums 已经是左右子区间分别排序好了的
        for i in range(left, right + 1):
            tempArr[i] = arr[i]
        
        #* 分别指向两个子数组(我们通过 mid 达到分离两个子数组的目的)的起始元素
        i = left
        j = mid + 1
        insertPointer = left
        #* 合并阶段 本质上是 合并两个排序数组 的过程，而每当遇到 左子数组当前元素 > 右子数组当前元素 时，意味着 「左子数组当前元素 至 末尾元素」 与 「右子数组当前元素」 构成了若干 「逆序对」 
        while insertPointer <= right:
            #* 左子区间的元素都遍历了，剩下只要把右子区间剩下的元素加入nums即可
            if i == mid + 1:
                arr[insertPointer] = tempArr[j]
                j += 1
            #* 同上，此时右子区间的元素已经遍历完，只需要添加左子区间的元素到nums
            elif j == right + 1:
                arr[insertPointer] = tempArr[i]
                i += 1
            elif tempArr[i] <= tempArr[j]:
                arr[insertPointer] = tempArr[i]
                i += 1
            elif tempArr[i] > tempArr[j]:
                #* 此时 (tempArr[i], tempArr[j]) 是一个逆序对. 但由于左子区间已经按从小到大排好序. 所以可推断出 tempArr[i]~tempArr[mid] 都大于 tempArr[j]，这也是这个方法的巧妙之处. 也就是说，在合并左右子区间时，新引入了共「mid-i+1」对「以tempArr[j]为右元素」的逆序对
                #! 每当遇到 左子数组当前元素 > 右子数组当前元素 时，意味着 「左子数组当前元素 至 末尾元素」 与 「右子数组当前元素」 构成了若干 「逆序对」。 可以看出这个解法是针对于右子数组的每个元素看齐与多少左子数组的元素构成逆序对，在315 题中便无法使用了
                crossPairs += (mid - i + 1)
                arr[insertPointer] = tempArr[j]
                j += 1
            insertPointer += 1
   
        return crossPairs + leftPairs + rightPairs

print(Solution().reversePairs([7,5,6,4]))
