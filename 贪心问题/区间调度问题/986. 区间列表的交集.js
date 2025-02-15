/* 

* 关于双指针移动的时机讲解: 
* 求完一个交集区间后，较早结束的子区间，不可能再和别的子区间重叠，它的指针要移动。
* 较长的子区间还有可能和别人重叠，它的指针暂时不动。
? https://leetcode.cn/problems/interval-list-intersections/solutions/243709/jiu-pa-ni-bu-dong-shuang-zhi-zhen-by-hyj8/

* 移动指针：
* 假设 right1<right2， 因为区间列表为不相交且已经排序好的， 则 arr1 不可能与 secondList 中 arr2 以后的任何区间相交。 所以每次优先移动当前区间尾段较小的指针 (right2<right1 同理)
* 若 right1==right2， 因为列表各个区间不相交， arr1 与 arr2 都不可能与之后的区间有交集， 可以移动任意一个
?https://leetcode.cn/problems/interval-list-intersections/solutions/1061065/java-shuang-zhi-zhen-by-feilue-b0qt/


? 非常好的示意图: https://leetcode.cn/problems/interval-list-intersections/solutions/1140195/li-yong-shuang-zhi-zhen-fa-lai-jie-jue-q-vqp0/

*/

var intervalIntersection = function (firstList, secondList) {
    const res = [];
    let i = 0;
    let j = 0;

    while (i < firstList.length && j < secondList.length) {
        let mergeStart = Math.max(firstList[i][0], secondList[j][0]);
        let mergeEnd = Math.min(firstList[i][1], secondList[j][1]);

        if (mergeStart <= mergeEnd) {
            res.push([mergeStart, mergeEnd]);
        }

        if (firstList[i][1] < secondList[j][1]) {
            i++;
        } else {
            j++;
        }
    }
    return res;
};
