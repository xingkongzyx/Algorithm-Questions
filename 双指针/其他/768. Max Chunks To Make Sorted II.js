/*
 * 怎样才能实现分块排序得到升序呢？由于块与块的相对位置不会改变，只要保证了排序前后某个块内容相同，就可以分出来，再加上内部排序，就能得到升序
? https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/solution/shi-fen-by-heren1229-pai2/
 * 原数组进行分块后, 每一个分块和排序后的数组中对应的分块数字是一样的, 只是排序不同。
 * 原数组: [0, | 3,0,2, | 3]
 * 排序后: [0, | 0,2,3, | 3]
 
 * 原数组: [4, | 6,5, | 7, | 8]
 * 排序后: [4, | 5,6, | 7, | 8]
 * 同时遍历两个数组(原数组和排序后的数组), 如果在某个位置他们的和是相同的则说明可以在这里切块
 > 由于问的是能分成的『最多的块』，所以我们的分块过程应当『贪心』地进行，在两个和相等的时候，立即分出一块。
 / 时间复杂度：O(NlogN), N 为数组长度, 数组排序时间认为是 NlogN, 滑动窗口遍历数组时间为 N。
 / 空间复杂度：O(N), N 为数组长度。
 ? https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/solution/768-zui-duo-neng-wan-cheng-pai-xu-de-kuai-iihua-do/
 */
var maxChunksToSorted = function (arr) {
    let sortedArr = arr.slice().sort((a, b) => a - b);
    let sum1 = 0;
    let sum2 = 0;
    let result = 0;
    for (let i = 0; i < arr.length; i++) {
        sum1 += arr[i];
        sum2 += sortedArr[i];
        if (sum1 === sum2) {
            result++;
            sum1 = 0;
            sum2 = 0;
        }
    }
    return result === 0 ? 1 : result;
};

// console.log(maxChunksToSorted([5, 4, 3, 2, 1]));
console.log(maxChunksToSorted([2, 1, 3, 4, 4]));
/// [2, 1, 3, 4, 4]
/// [1, 2, 3, 4, 4];
