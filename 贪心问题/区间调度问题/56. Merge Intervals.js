/*
! 按照左边界排序, 排序之后局部最优：每次合并都取最大的右边界, 这样就可以合并更多的区间了, 整体最优：合并所有重叠的区间。

* 只需要对所有的区间按照左端点升序排序, 然后遍历。
* ① 如果当前遍历到的区间的左端点 > 结果集中最后一个区间的右端点, 说明它们没有交集, 此时把区间添加到结果集；
* ② 如果当前遍历到的区间的左端点 <= 结果集中最后一个区间的右端点, 说明它们有交集, 此时产生合并操作, 即：对结果集中最后一个区间的右端点更新（取两个区间的最大值）。



! 当考察完最后一个区间, 后面没区间了, 遇不到不重合区间, 最后的 mergedInterval 没推入 res。要单独补上。

? https://leetcode-cn.com/problems/merge-intervals/solution/shou-hua-tu-jie-56he-bing-qu-jian-by-xiao_ben_zhu/

? 图解: https://leetcode.cn/problems/merge-intervals/solution/by-lin-shen-shi-jian-lu-k-wri9/

/ 时间复杂度：O(nlogn), 其中 n 为区间的数量。除去排序的开销, 我们只需要一次线性扫描, 所以主要的时间开销是排序的 O(nlogn)。
/ 空间复杂度：O(logn), 其中 n 为区间的数量。这里计算的是存储答案之外, 使用的额外空间。O(logn) 即为排序所需要的空间复杂度。


 */

var merge = function (intervals) {
    intervals.sort(
        (intervalA, intervalB) => intervalA[0] - intervalB[0]
    );

    let mergedResult = [];
    let mergedIntervalStart = intervals[0][0];
    let mergedIntervalEnd = intervals[0][1];

    for (let i = 1; i < intervals.length; i++) {
        let currentIntervalStart = intervals[i][0];
        let currentIntervalEnd = intervals[i][1];
        if (currentIntervalStart <= mergedIntervalEnd) {
            mergedIntervalEnd = Math.max(
                mergedIntervalEnd,
                currentIntervalEnd
            );
        } else {
            mergedResult.push([
                mergedIntervalStart,
                mergedIntervalEnd,
            ]);
            mergedIntervalStart = currentIntervalStart;
            mergedIntervalEnd = currentIntervalEnd;
        }
    }
    mergedResult.push([mergedIntervalStart, mergedIntervalEnd]);
    return mergedResult;
};

const intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18],
];
console.log(merge(intervals));
