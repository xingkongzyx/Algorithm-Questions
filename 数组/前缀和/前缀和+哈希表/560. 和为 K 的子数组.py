# https://leetcode.cn/problems/subarray-sum-equals-k/solution/de-liao-yi-wen-jiang-qian-zhui-he-an-pai-yhyf/


""" 
# 为什么不能使用滑动窗口:
# 因为nums[i]可以小于0. 也就是说右指针 i 向后移 1 位不能保证区间会增大. 左指针 j 向后移 1 位也不能保证区间和会减小。给定j. i的位置没有二段性
? https://leetcode.cn/problems/subarray-sum-equals-k/solution/qian-zhui-he-ha-xi-biao-by-pleviumtan-hgh2/

* 1. 假如存在区间 [left,right]，使得在 [left,right] 这个区间的子数组的和为 k。换句话说, 就是『前right项和』减去『前left-1项和』等于『k』, 即『前left-1项和』等于『前right项和』减去『k』。
* 2. 可以这样做, 在扫描数组的同时, 假设当前扫到第i位, 记录它的前 i 项和 preSum, 用该和减去 k, 即 preSum - k, 判断 preSum - k 是否为某个位置的前 n 项和, 若是, 更新统计量。
? 链接：https://leetcode.cn/problems/subarray-sum-equals-k/solution/qian-zhui-he-shi-xian-jian-dan-by-jarvis1890/


// 为什么要边遍历存储前缀和一边看当前前缀和 - k 是否在map中. 而不能得到前缀和数组再对每一项进行 presum[i] - k 计算的操作?
边存边查看 map, 如果 map 中存在 key 为「当前前缀和 - k」, 说明这个之前出现的前缀和, 满足「当前前缀和 - 该前缀和 == k」, 它出现的次数, 累加给 count。
因为我们要看的是在这个元素之前的前缀和, 至于它之后的我们遍历到之后的元素的时候会累加给 count的, 如果在当前位置都进行了相加, 总结果会是重复的结果。

"""
class Solution(object):
    def subarraySum(self, nums, k):
        from collections import defaultdict

        #* 这里定义的前缀和变量指的是到nums[i]为止(包含当前元素)的前缀和是多少, 而不是一个数组。这个变量可以理解为与 nums 数组一一对应, 不是像平常定义前缀和数组时多定义一个位置
        preSum = 0
        
        #* map 存储某 "前缀和" 出现的次数，这里用collections.defaultdict来定义它
        #* 如果某前缀不在此字典中，那么它对应的次数为0
        map = defaultdict(int)
        
        #* 为什么这里要多声明 1 步 map[0] = 1? 这样是因为，最一开始的时候(0个元素)，和为0。这样，🌜当我们首次从左到右一直累加出k时，才能得出正确的结果🌛
        #? 更加详细的解释 https://leetcode.cn/problems/subarray-sum-equals-k/solution/he-wei-kde-zi-shu-zu-by-leetcode-solution/1066017
        map[0] = 1

        count = 0
        
        #* 我们要在 nums 中找到 "当前下标的前缀和"(对应着上面说的『前right项和』) 与 "当前下标之前的数的前缀和"(对应着上面说的『前left-1项和』) 的差有没有等于k的. 
        #! 注意因为是要找"当前下标之前的数的前缀和", 所以不能够先遍历 preSum, 将其中各个元素出现的次数存储在 map 中, 这样再遍历得到的结果就不是"当前下标之前的数的前缀和"出现次数
        for i in range(len(nums)):
            #* 计算到当前元素为止的前缀和
            preSum += nums[i]  
           
           
            if (preSum - k) in map:
                count += map[preSum - k]

            #* 下面的代码实际上对应两种情况，一种是某 preSum 之前在map中出现过（直接在原来出现的次数上 +1 即可），另一种是某 preSum 没出现过（理论上应该设为1，但是因为此处用defaultdict存储，如果 preSum 这个key不存在将返回默认的int，也就是0）返回0加上1和直接将其置为1是一样的效果。所以这里统一用一句话包含上述两种情况
            map[preSum] += 1
        return count


s = Solution()
res = s.subarraySum(nums=[1], k=0)
print(res)
