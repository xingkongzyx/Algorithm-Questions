/* 
* 局部最优：删除单调坡度上的节点（不包括单调坡度两端的节点），那么这个坡度就可以有两个局部峰值。

* 整体最优：整个序列有最多的局部峰值，从而达到最长摆动序列。
*/
/* 
很关键的就是curDiff == 0的时候，不更新preDiff和result，这个很重要，这样就使得我们可以不计入右边坡为平坡的这个点，而且也保持了preDiff的坡度（无论是上坡还是平坡还是下坡）。举个例子：一个点左边是下坡，右边是平坡，那么preDiff还是< 0,如果这个点右边的点，左边是平坡，右边还是下坡，那么curDiff < 0 并且 preDiff < 0，我们还是不计入这个点，直到我们遇到curDiff > 0,即该点的右边为上坡，我们才统计这个点，这个特殊的例子理解了，这道题应该就完全理解了

https://leetcode-cn.com/problems/wiggle-subsequence/solution/python3-yi-tu-sheng-qian-yan-by-v12de-ao-72b1/
*/
var wiggleMaxLength = function (nums) {
    if (nums.length < 2) return nums.length;

    let preDiff = 0;
    let currentDiff = 0;
    let result = 1;
    let arr = [];
    let i;
    for (i = 0; i < nums.length - 1; i++) {
        currentDiff = nums[i + 1] - nums[i];
        if (preDiff >= 0 && currentDiff < 0) {
            result++;
            preDiff = currentDiff;
            arr.push(nums[i]);
        } else if (currentDiff > 0 && preDiff <= 0) {
            result++;
            preDiff = currentDiff;
            arr.push(nums[i]);
        }
    }
    arr.push(nums[i]);
    console.log(arr);
    return result;
};

const nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8];
console.log(wiggleMaxLength(nums));
