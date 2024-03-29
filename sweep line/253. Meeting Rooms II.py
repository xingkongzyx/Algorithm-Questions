""" 
> 题目的本质: 给你输入若干时间区间, 让你计算同一时刻「最多」有几个区间重叠。题目的关键点在于, 给你任意一个时刻, 你是否能够说出这个时刻有几个会议？如果可以做到, 那我遍历所有的时刻, 找个最大值, 就是需要申请的会议室数量。

# 整体思路: 创建一个序列记录每个会议的起止时间, 并用 1 和 -1 分别标记这个时间是开始还是结束, 这样就能确定某个时刻有几个会议室处于工作中, 然后进行会议时间升序排序, 注意相等时间的优先级按先结束后开始, 可以理解成某个会议室的上个会议刚结束, 下个会议立马开始。排序完毕进行对每个时间对应的 开始(1) 和 结束(-1) 去计算此时会议室使用数量, 并取会议时间安排中会议室使用数量最大值。
* 时间开始时间升序排序, 如果开始时间一样, 结束的在前！为什么呢? 不然要重复算的, 比如{{1, 13}, {13, 15}};, 一定是结束的13在前
* 使用 1 和 -1 进行标记的原因是这样就能知道这个时间对应的是「开始」会议还是「结束」会议
* 思路: 「所需会议室数量」等价于「要统计同一时刻进行的最多会议的数量」。
* 	a.把所有的开始时间和结束时间放在一起排序。
* 	b.用cur表示当前进行的会议数量, 遍历排序后的时间数组。
* 	c.如果是开始时间, cur加1, 如果是结束时间, cur减1。
* 	d.在遍历的过程中, cur出现的最大值就是需要的房间数。
/ 时间复杂度: O(nlog(n)) + O(n)
/ 空间复杂度: O(nlog(n)) + O(1)




? 扫描线的讲解: https://leetcode.cn/problems/meeting-rooms-ii/solutions/2081316/labuladong-sao-miao-xian-ji-qiao-an-pai-h0f5d/?orderBy=newest_to_oldest

? 图解转化为上下车问题 O(nlogn): https://leetcode.cn/problems/meeting-rooms-ii/solutions/895579/tu-jie-zhuan-hua-wei-shang-xia-che-wen-t-uy2q/

? python代码: https://leetcode.cn/problems/meeting-rooms-ii/solution/tong-ji-tong-shi-jin-xing-de-hui-yi-by-loick/
"""


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        arr = []
        for start, end in intervals:
            arr.append((start, 1))
            arr.append((end, -1))

        arr.sort()
        res = 0
        rooms = 0
        for time, val in arr:
            rooms += val
            res = max(res, rooms)

        return res
