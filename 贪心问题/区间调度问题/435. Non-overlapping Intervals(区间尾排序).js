/* 
> 这道题不要看carl的题解
# key concept : pick interval with smallest end, because smallest end can hold most intervals. keep track of current element end. if next start is smaller than previous end, remove that next element
* we can sort interval by ending time and key track of current earliest end time. Once next interval's start time is earlier than current end time, then we have to remove one interval. Otherwise, we update earliest end time.
? https://leetcode.com/problems/non-overlapping-intervals/solutions/276056/python-greedy-interval-scheduling/?orderBy=most_votes
* 

*/

var eraseOverlapIntervals = function (intervals) {
    intervals.sort(
        (intervalA, intervalB) => intervalA[1] - intervalB[1]
    );
    //# 记录区间尾部的位置
    let prev_end = intervals[0][1];
    //# 重叠区间的数量(也就是需要移除的区间的数量)
    let result = 0;
    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][0] < prev_end) {
            //# 如果有重叠, 根据贪心的思想, 选取两个区间中尾部元素更小的那个区间, 也就是 prev_end 代表的那个区间, 而移除当前区间. result要加1
            result++;
        } else {
            prev_end = intervals[i][1];
        }
    }
    return result;
};

eraseOverlapIntervals([
    [1, 7],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
]);
