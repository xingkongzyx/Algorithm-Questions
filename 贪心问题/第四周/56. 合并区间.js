/*
 * 按照左边界排序，排序之后局部最优：每次合并都取最大的右边界，这样就可以合并更多的区间了，整体最优：合并所有重叠的区间。

* [mergedIntervalStart, mergedIntervalEnd] 初始为第一个区间，
* [currentIntervalStart, currentIntervalEnd] 表示当前的区间，
* mergedResult 表示结果数组

* 开启遍历，尝试合并 mergedIntervalEnd 和 currentIntervalEnd, 合并后更新到 mergedIntervalEnd
* 合并后的新区间还可能和后面的区间重合，继续尝试合并新的 currentIntervalEnd，更新给 mergedIntervalEnd
* 直到不能合并 —— currentIntervalStart > mergedIntervalEnd，此时将 [mergedIntervalStart, mergedIntervalEnd] 区间推入 mergedResult 数组

# 合并时原则上要更新 mergedIntervalStart 和 mergedIntervalEnd, 即左右端 
# 但因为先按区间的左端进行了升序排序，就能保证 mergedIntervalStart < currentIntervalStart
# 所以合并只需 mergedIntervalEnd = Math.max(
#                mergedIntervalEnd,
#                currentIntervalEnd
#            );

! 当考察完最后一个区间，后面没区间了，遇不到不重合区间，最后的 mergedInterval 没推入 res。要单独补上。

? https://leetcode-cn.com/problems/merge-intervals/solution/shou-hua-tu-jie-56he-bing-qu-jian-by-xiao_ben_zhu/
 */

var merge = function (intervals) {
    intervals.sort((intervalA, intervalB) => {
        if (intervalA[0] > intervalB[0]) return 1;
        else if (intervalB[0] > intervalA[0]) return -1;
        else return intervalA[1] - intervalB[1];
    });

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
