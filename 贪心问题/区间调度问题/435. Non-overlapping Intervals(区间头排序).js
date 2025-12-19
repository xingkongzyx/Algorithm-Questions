/* 
正确的思路既能够按照区间左端点排序，也能够按照区间右端点排序。

1.对于按照区间左端点排序，当两个比较的区间存在重叠时，再比较区间右端点的大小，保留右端点小的区间（对应结束时间早的区间)，这样能够满足剩余非重叠区间的个数最多。

2.对于按照区间右端点排序，当两个比较的区间存在重叠时，无需比较右端点的大小, 因为按照右端点排序, 后者肯定大于前者，因此只需保留右端点(前者)小的区间(对应结束时间早的区间)。

综上所述：按照左区间排序比按照右区间排序多了一步比较两区间右端点大小，选出右端点小的区间的步骤罢了。整体思路还是贪心。

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
