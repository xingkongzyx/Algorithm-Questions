/*
 * 针对数组 [[1,4],[2,6],[2,8]]的情况，我们应该让 [2,8] 放在 [2,6] 的前面，否在 [[2,6][2,8]] 这样 loop 的话 [2,6] 无法被算在被覆盖区间中（8 !<= 6)
 * https://leetcode.cn/problems/remove-covered-intervals/solutions/55399/sao-miao-xian-fa-by-liweiwei1419/
 */
var removeCoveredIntervals = function (intervals) {
    intervals.sort((a, b) => {
        if (a[0] !== b[0]) {
            return a[0] - b[0]; // 按第一个数字升序排列
        } else {
            return b[1] - a[1]; // 当第一个数字相同时，按第二个数字降序排列
        }
    });
    console.log(intervals);
    let prevStart = intervals[0][0];
    let prevEnd = intervals[0][1];
    let remove = 0;
    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][1] <= prevEnd) {
            remove++;
        } else {
            prevStart = intervals[i][0];
            prevEnd = intervals[i][1];
        }
    }

    return intervals.length - remove;
};
