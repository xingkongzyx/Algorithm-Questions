/* 
* 局部最优：删除单调坡度上的节点（不包括单调坡度两端的节点），那么这个坡度就可以有两个局部峰值。

* 整体最优：整个序列有最多的局部峰值，从而达到最长摆动序列。
*/

var wiggleMaxLength = function (nums) {
    if (nums.length < 2) return nums.length;

    // preState 表示摆动序列上一个状态：0代表未知（即初始状态），-1代表下降，1代表上升。
    let res = 1;
    let preState = 0;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1] && preState <= 0) {
            res += 1;
            preState = 1;
        } else if (nums[i] < nums[i - 1] && preState >= 0) {
            res += 1;
            preState = -1;
        }
    }

    return res;
};

const nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8];
console.log(wiggleMaxLength(nums));
