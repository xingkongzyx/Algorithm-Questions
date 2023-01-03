/*
! 按照左边界排序, 排序之后局部最优：每次合并都取最大的右边界, 这样就可以合并更多的区间了, 整体最优：合并所有重叠的区间. 

* 只需要对所有的区间按照左端点升序排序, 然后遍历. 
* ① 如果当前区间的左端点 > prevIntervalEnd, 那么它们不会重合, 我们可以直接将 prevInterval 加入数组 res 的末尾；并更新 prevInterval 为当前 interval
* ② 如果当前遍历到的区间的左端点 <= prevIntervalEnd, 说明它们有交集, 此时产生合并操作, 即：对prevIntervalEnd 更新（取两个区间的最大值）. 

# 注意: 我们是「先合并」, 遇到不重合的区间「再推入」 prevInterval. 当考察完最后一个区间, 后面没区间了, 遇不到不重合区间, 最后的 prevInterval 没推入 res, 要单独补上. 

? https://leetcode-cn.com/problems/merge-intervals/solution/shou-hua-tu-jie-56he-bing-qu-jian-by-xiao_ben_zhu/
? 也很好: https://leetcode.cn/problems/merge-intervals/solution/56-he-bing-qu-jian-jian-dan-yi-dong-liao-uxbo/
? 图解: https://leetcode.cn/problems/merge-intervals/solution/by-lin-shen-shi-jian-lu-k-wri9/

/ 时间复杂度：O(nlogn), 其中 n 为区间的数量. 除去排序的开销, 我们只需要一次线性扫描, 所以主要的时间开销是排序的 O(nlogn). 
/ 空间复杂度：O(logn), 其中 n 为区间的数量. 这里计算的是存储答案之外, 使用的额外空间. O(logn) 即为排序所需要的空间复杂度. 


 */

var merge = function (intervals) {
    intervals.sort(
        (intervalA, intervalB) => intervalA[0] - intervalB[0]
    );

    let res = [];
    let prevIntervalStart = intervals[0][0];
    let prevIntervalEnd = intervals[0][1];

    for (let i = 1; i < intervals.length; i++) {
        let curIntervalStart = intervals[i][0];
        let curIntervalEnd = intervals[i][1];
        if (curIntervalStart <= prevIntervalEnd) {
            // / 原则上要更新的 prev 区间的两端, 但因为最开始是按区间的左端升序排序, 就能保证 prev[0] < cur[0]
            prevIntervalEnd = Math.max(
                prevIntervalEnd,
                curIntervalEnd
            );
        } else {
            res.push([prevIntervalStart, prevIntervalEnd]);
            prevIntervalStart = curIntervalStart;
            prevIntervalEnd = curIntervalEnd;
        }
    }
    res.push([prevIntervalStart, prevIntervalEnd]);
    return res;
};

const intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18],
];
console.log(merge(intervals));
