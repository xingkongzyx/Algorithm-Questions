/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

// https://leetcode-cn.com/problems/sliding-window-maximum/solution/acm-xuan-shou-tu-jie-leetcode-hua-dong-c-i3wj/
class MyQueue {
    constructor() {
        this.data = [];
    }
    //# 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    //# 这样就保持了队列里的数值是单调从大到小的了。
    push(val) {
        while (
            this.data.length > 0 &&
            this.data[this.data.length - 1] < val
        ) {
            this.data.pop();
        }
        this.data.push(val);
    }
    pop(value) {
        //# 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
        //# 同时pop之前判断队列当前是否为空。
        if (this.data.length > 0 && value === this.maxVal())
            this.data.shift();
    }
    maxVal() {
        return this.data[0];
    }
}

var maxSlidingWindow = function (nums, k) {
    if (nums.length <= k) return [Math.max(...nums)];
    let arr = [];
    let queue = new MyQueue();
    //# 先将前k的元素放进队列
    for (let i = 0; i < k; i++) {
        queue.push(nums[i]);
    }
    //# 并记录前k元素的最大值
    arr.push(queue.maxVal());
    for (let right = k; right < nums.length; right++) {
        let leftNum = nums[right - k];
        let rightNum = nums[right];
        // console.log(
        //     `left idx is ${left} num is ${leftNum}, right idx is ${right} num is ${rightNum}`
        // );
        // console.log(queue);
        //# 滑动窗口移除最前面元素
        queue.pop(leftNum);
        //# 滑动窗口前加入最后面的元素
        queue.push(rightNum);
        //# 记录当前窗口对应的最大值
        arr.push(queue.maxVal());
    }
    return arr;
};
