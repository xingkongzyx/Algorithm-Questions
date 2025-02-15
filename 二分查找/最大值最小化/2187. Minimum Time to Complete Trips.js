/* 
与 2226 思路是一致的
单调性: 给的总时间越多，那么可以完成的旅途数量也就越多，有单调性

? https://leetcode.cn/problems/minimum-time-to-complete-trips/solutions/1300957/wan-cheng-lu-tu-de-zui-shao-shi-jian-by-uxyrp/
*/
var minimumTime = function (time, totalTrips) {
    // 旅途需要花费的时间越少，能够完成旅途的数量也会越少
    let left = 1;
    let right = totalTrips * Math.max(...time);

    while (left < right) {
        let mid = Math.floor((left + right) / 2);

        let completeTrips = 0;
        for (let t of time) {
            completeTrips += Math.floor(mid / t);
        }

        if (completeTrips < totalTrips) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
};
