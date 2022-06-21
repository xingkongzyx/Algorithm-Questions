// 矮个子插队，高个子看不见；所以我们可以先安排高个子的位置，再通过插队的方式安排矮个子的位置
var reconstructQueue = function (people) {
    /*
     * If the result is negative a is sorted before b.
     * If the result is positive b is sorted before a.
     * If the result is 0 no changes are done with the sort order of the two values.
     */
    //# 将people按身高从大到小排序，如果身高一样则将前面高于自己人数小的人放在前面
    people.sort((a, b) => {
        if (a[0] < b[0]) return 1;
        else if (a[0] > b[0]) return -1;
        else return a[1] - b[1];
    });
    let queue = [];

    //# 挨个根据前面高于自己人数插入到ans里
    //# 因为people已按照身高排序，所以某个人被插入到ans里时，所有比他高的都已经在ans里了
    //# 而身高比他矮的人怎样插入到ans里都不影响前面高于他的人数
    //# 所以这样得到的数组就是符合我们要求的队列

    for (let i = 0; i < people.length; i++) {
        let [, location] = people[i];
        queue.splice(location, 0, people[i]);
    }

    return queue;
};

const people = [
    [7, 0],
    [4, 4],
    [7, 1],
    [5, 0],
    [6, 1],
    [5, 2],
];
let res = reconstructQueue(people);
console.log(res);
