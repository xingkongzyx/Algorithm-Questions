/* 
* once we sort based on start values of the intervals, we just need to consider the min end among the 2 intervals as this can lead to less number of overlaps with upcoming intervals. Hands down.
* 贪心思想: 在依照区间头元素排序的情况下, 对于有重叠的区间, 优先选择右区间end更小的区间, 移除end较大的区间。从而减小与后面区间重叠的可能
? https://leetcode.com/problems/non-overlapping-intervals/solutions/481758/easy-to-understand-java-solution/?orderBy=most_votes
? https://leetcode.cn/problems/non-overlapping-intervals/solution/python-by-ljiajie-tjdi/
*/

var eraseOverlapIntervals = function (intervals) {
    intervals.sort((a, b) => a[0] - b[0]);
    prevEnd = intervals[0][1];
    res = 0;
    for (let i = 1; i < intervals.length; i++) {
        if (prevEnd <= intervals[i][0]) {
            prevEnd = intervals[i][1];
        } else if (prevEnd > intervals[i][0]) {
            res += 1;
            prevEnd = Math.min(prevEnd, intervals[i][1]);
        }
    }
    return res;
};
