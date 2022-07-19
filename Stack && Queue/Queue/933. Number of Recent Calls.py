""" 
#? 理解问题的图片: https://leetcode.cn/problems/number-of-recent-calls/solution/by-nehzil-9het/
! 核心：先请求, 先过期, 对应队列：先进, 先出, 因此用队列数据结构解决问题。
* 由于每次收到的请求的时间都比之前的大, 因此从队首到队尾的时间值是单调递增的。当在时间 t 收到请求时, 为了求出 [t-3000,t] 内发生的请求数, 我们可以不断从队首弹出早于 t-3000 的时间。循环结束后队列的长度就是 [t-3000,t] 内发生的请求数。
? https://leetcode.cn/problems/number-of-recent-calls/solution/zui-jin-de-qing-qiu-ci-shu-by-leetcode-s-ncm1/

"""
class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        
        # calculate how many requests within [t-3000, t]
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
            
        return len(self.queue)
