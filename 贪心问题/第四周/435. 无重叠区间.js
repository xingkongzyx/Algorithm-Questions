/* 
> 这道题不要看carl的题解
? https://leetcode-cn.com/problems/non-overlapping-intervals/solution/wu-zhong-die-qu-jian-ji-bai-liao-100de-y-kkzr/
* 首先要对区间进行排序，这里先以区间的头来排序，然后在遍历区间。
* 1，如果后面区间的头小于当前区间的尾，
* 比如当前区间是[3,6]，后面的区间是[4,5]，再然后是[5,9]
* 说明这两个区间有重复，必须要移除一个，那么要移除哪个呢，
! 为了防止在下一个区间和现有区间有重叠，我们应该让现有区间越短越好，所以应该移除尾部比较大的，保留尾部比较小的。
# 以上面的例子来说，当我们在[4,5]时，发现与[3,6]重叠，如果我们移除[4,5],那么后面的[5,9]还是与[3,6]重叠，所以我们应该让现有区间越短越好，应该移除尾部比较大的，也就是[3,6]
* 2，如果后面区间的头不小于当前区间的尾，说明他们没有重合，不需要移除
* 

*/

var eraseOverlapIntervals = function (intervals) {
    intervals.sort((intervalA, intervalB) => {
        if (intervalA[0] > intervalB[0]) return 1;
        else if (intervalB[0] > intervalA[0]) return -1;
        else return intervalA[1] - intervalB[1];
    });
    //# 记录区间尾部的位置
    let end = intervals[0][1];
    //# 需要移除的数量
    let result = 0;

    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][0] < end) {
            //# 如果重叠了，必须要移除一个，所以result要加1，
            //# 然后更新尾部的位置，我们取尾部比较小的
            result++;
            //# 如果两个区间有重复，我们应该让现有区间越短越好，应该移除尾部比较大的
            if (intervals[i][1] < end) {
                end = intervals[i][1];
            }
        } else {
            //# 如果没有重叠，就不需要移除，只需要更新尾部的位置即可
            end = intervals[i][1];
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
