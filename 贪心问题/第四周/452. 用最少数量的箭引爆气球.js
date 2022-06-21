/* 
* 参考1: https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/solution/hua-tu-fen-xi-452-ti-yong-zui-shao-shu-l-g6s8/

* 参考2: 主要思路是如果两个区间完全不挨着，那肯定得多用一根箭；如果两个区间挨着就不用多加一根，但3个及以上区间挨着时(例如 [[0,6],[0,9],[7,8]]) 就一定要注意挨着的这些区间的最小end，如果下一个区间的start大于这个最小end，那即使区间挨着也得多加一根箭。两个区间挨着的话肯定一根箭就够了，3个及以上挨着可就不一定了。

?          Λ
?  [-------|]
?     [----|------] //这俩哥们一个箭够了
?        [-|---------] //如果第三个是这样的，一根箭也是够的
?          |  [-------]  //如果第四个如图，不行了，因为这个的start小于第一行那个end(也就是上述挨着的最小的end而不是第三个区间的end)了，所以得再加一根




链接：https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/solution/tan-xin-an-endpai-xu-bi-an-startpai-xu-yao-hao-by-/

*/
var findMinArrowShots = function (points) {
    points.sort((pointA, pointB) => pointA[0] - pointB[0]);
    if (points.length === 0) return 0;
    let arrows = 1;
    let commonMinEnd = points[0][1];
    for (let i = 1; i < points.length; i++) {
        if (points[i][0] > commonMinEnd) {
            arrows++;
            commonMinEnd = points[i][1];
        } else {
            commonMinEnd = Math.min(commonMinEnd, points[i][1]);
        }
    }

    return arrows;
};
