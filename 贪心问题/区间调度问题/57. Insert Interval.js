/* 
? https://leetcode-cn.com/problems/insert-interval/solution/57-cha-ru-qu-jian-mo-ni-cha-ru-xiang-jie-by-carlsu/
? 图片更加直观: https://leetcode.cn/problems/insert-interval/solutions/472435/shou-hua-tu-jie-57-cha-ru-qu-jian-fen-cheng-3ge-ji/?orderBy=most_votes
 */

var insert = function (intervals, newInterval) {
    let index = 0;
    let result = [];
    const len = intervals.length;
    //* 找到插入区间需要插入或者合并的位置。此时intervals[index]就需要合并的区间了
    while (index < len && intervals[index][1] < newInterval[0]) {
        result.push(intervals[index]);
        index++;
    }
    /* 
    * 这时intervals[index] 与 newInterval 重叠，我们需要进行合并。
    * 只要是intervals[index]的起始位置 <= newInterval的终止位置，就要一直合并下去.
    # 也可以从反面进行考虑, 只有在 "newInterval[1] < intervals[index][0]" 的时候说明合并结束, 所以相反的情况下(也就是 >= 时)就要持续进行合并    
    */
    while (index < len && newInterval[1] >= intervals[index][0]) {
        newInterval[0] = Math.min(
            newInterval[0],
            intervals[index][0]
        );
        newInterval[1] = Math.max(
            newInterval[1],
            intervals[index][1]
        );

        index++;
    }

    //* 合并之后，将newInterval放入result就可以了
    result.push(newInterval);

    //* 最后把合并之后的区间，依次加入result中。
    while (index < len) {
        result.push(intervals[index]);
        index++;
    }
    return result;
};
const intervals = [
    [1, 2],
    [3, 5],
    [6, 7],
    [8, 10],
    [12, 16],
];
const newInterval = [4, 8];
let res = insert(intervals, newInterval);
// console.log(res);
