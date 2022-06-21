""" 
# https://leetcode.cn/problems/h-index-ii/solution/jian-er-zhi-zhi-er-fen-cha-zhao-by-liweiwei1419-2/

! h 指数是论文数量，不是引用次数。
* 题目希望我们找一条分割线(也就是下面代码中的mid), 这条分割线的分割点是从 0 到 "len(citations)- 1", 分割线右边的论文数量是 len(citations) - mid, 这样定义能保证分割线右边最少有一篇论文. 
* 从这条分割线到结尾, 引用数量的数组元素包含 [mid, len(citations)-1]。 假设论文数量设为 h, 这 h 篇论文中的最小的引用次数 nums[mid](因为是升序排列所以mid代表最小的引用次数) 大于等于 h。精炼的说法是: 分割线右边的最少引用次数 >= 分割线右边的论文篇数。

> N 篇论文中总共有 h 篇论文分别被引用了至少 h 次 等价于 分割线右边的最少引用次数 >= 分割线右边的论文篇数

/ 分割线越靠近左边，那么右边的论文数量就越多，因为分割线满足的条件是 "分割线右边的最少引用次数 >= 分割线右边的论文篇数"，所以对citations[mid]的要求就越大

* 然后返回所取的区间的长度 - (totalCitations - mid) 而我们选取的区间要满足区间中的数大于等于所在区间的长度

"""


class Solution(object):
    def hIndex(self, citations):
        if citations[-1] == 0:
            return 0
        totalCitations = len(citations)
        left = 0
        right = totalCitations - 1

        while left < right:
            #* mid代表的就是上面说的分割线
            mid = left + (right - left) // 2
            h = totalCitations - mid
            #* 使用一直讲解的排除法，如果分割线右边的最少引用次数 < 分割线右边的论文篇数。
            #* 举例说明就是 [0 | 1(mid), 3, 5, 6] h=4, citations[mid]=1. 这种情况下继续往左边取值, h会变大, 但是 citations[mid]会变小, 更不会满足要求, 所以要取 mid + 1, 这时候 "分割线右边的最少引用次数" 变大, "分割线右边的论文篇数" 变小, 有可能满足 "分割线右边的最少引用次数 >= 分割线右边的论文篇数" 的条件
            if citations[mid] < h:
                # 下一轮搜索区间 [mid + 1, right]
                left = mid + 1
            else:
                # 下一轮搜索区间 [left, mid]
                #* "分割线右边的最少引用次数 >= 分割线右边的论文篇数" 是满足的，题目希望我们寻找h指数最大的情况。
                #* 我们应该继续让mid往左走去尝试看有没有更小的mid值，可以满足mid对应的值大于等于从[mid,length-1]的长度。
                right = mid

        
        return totalCitations - left

Solution().hIndex(citations = [0,1,3,5,6])
