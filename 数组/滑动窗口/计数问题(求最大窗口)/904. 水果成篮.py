class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ## Step 1: 
        ## 定义需要维护的变量, 本题求收集的水果的最大数目, 所以需要定义 maxLen,
        ## 该题又涉及计算水果种类, 因此还需要一个哈希表
        record = {}
        maxLen = 0
        
        ## Step 2: 定义窗口的首尾端 (left, right)， 然后滑动窗口
        left = 0
        right = 0
        
        while right < len(fruits):
        ## Step 3
        ## 更新需要维护的变量 (max_len, record)
        ## i.e. 把窗口末端元素加入哈希表，使其频率加1，并且更新最大长度
            rightFruit = fruits[right]
            record[rightFruit] = record.get(rightFruit, 0) + 1
            
            if len(record) <= 2:
                maxLen = max(maxLen, right - left + 1)

            ## Step 4: 
            ## 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            ## 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            ## 当哈希表长度时候 2 的时候(说明存在了第三种水果，两个篮子装不下)，窗口不合法
            ## 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (record)
            while len(record) > 2:
                leftFruit = fruits[left]
                record[leftFruit] = record.get(leftFruit, 0) - 1
                
                if record[leftFruit] == 0:
                    del record[leftFruit]
                    
                left += 1

            right += 1
        return maxLen
