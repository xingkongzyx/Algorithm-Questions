/* 
> 这道题不要看carl的题解

* 把问题转换成：最多能选取几个区间不重叠的区域
* 那答案显然变成：总区间个数 - 不重叠区间个数
* 
* ➀ 按照结束时间从小到大排序，然后对新列表遍历。
* ➁ 判断当前区间是否满足：「开始时间」晚于或等于上一次的「结束时间」
* ➂ 每次都选结束时间最早的
* ➃ 每选一次更新一下结束时间

? 参考: https://leetcode.cn/problems/non-overlapping-intervals/solution/python-tan-xin-onlogn-by-meng-jian-yue-qiu-de-mao/

? 更细致的讲解: https://leetcode.cn/problems/non-overlapping-intervals/solution/tan-xin-jie-fa-qi-shi-jiu-shi-yi-ceng-ch-i63h/
* 

*/

var eraseOverlapIntervals = function (intervals) {
    intervals.sort(
        (intervalA, intervalB) => intervalA[1] - intervalB[1]
    );
    //# 记录区间尾部的位置
    let end = intervals[0][1];
    //# 不重叠区间的数量
    let result = 1;
    console.log(intervals);
    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][0] >= end) {
            //# 如果没有重叠，result要加1，并更新尾部的位置
            end = intervals[i][1];
            result++;
        }
    }
    return intervals.length - result;
};
eraseOverlapIntervals([
    [1, 7],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
]);
