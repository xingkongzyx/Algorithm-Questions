/* 
* 左端升序, 贪心的思路: 左端升序下, 因为每个气球都需要射穿, 可以从第一个未爆的气球(目标气球)开始射穿,  然后考虑双响和多响的情况, (多响气球)还是因为每个气球都需要射穿至少需要耗费一箭, 『找多响时先保证排在前面的气球』, 因为如果提前多响靠后的气球, 留在前面的气球也必须花费一箭处理, 而且这个气球是孤立的, 也不可能存在再多穿的情况, 而后面的气球最差的情况也就是在那个位置再射一箭, 耗费是一样的, 而且因为不用考虑目标气球, 有可能再多击穿几个气球。

* 在这里做一个总结：
* 1. 如果新气球的左端点大于射击区间的右边界, 那么我们就需要重新开辟一个区间；
* 2. 如果新气球的左端点小于射击区间的右边界, 这里又要分为两种情况：如果右端点大于射击区间的右边界, 那么我们的射击区间的右边界无需变化；如果右端点小于射击区间的右边界, 那么我们射击区间的右边界就要向左移动, 以新气球的右端点为准, 确立新的边界。


? https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/solution/hua-tu-fen-xi-452-ti-yong-zui-shao-shu-l-g6s8/

*/
var findMinArrowShots = function (points) {
    //# 按照每个气球的左边界排序
    points.sort((pointA, pointB) => pointA[0] - pointB[0]);

    let arrows = 1;

    //# 获取排序后第一个气球右边界的位置, 我们可以认为是箭射入的位置
    let arrowPosition = points[0][1];

    for (let i = 1; i < points.length; i++) {
        //# 如果箭射入的位置小于下标为 i 这个气球的左边位置, 说明这支箭不能击爆下标为i的这个气球, 需要再拿出一支箭, 并且要更新这支箭射入的位置
        if (arrowPosition < points[i][0]) {
            arrows++;
            arrowPosition = points[i][1];
        } else {
            // # 如果大于等于, 说明这支箭可以"一箭双雕", 因为「贪心思想」, 我们要让箭射最靠左的末尾位置
            arrowPosition = Math.min(arrowPosition, points[i][1]);
        }
    }

    return arrows;
};
