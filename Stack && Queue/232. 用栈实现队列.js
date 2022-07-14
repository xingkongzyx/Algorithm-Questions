/* 
* 思路是：「输入栈」会把输入顺序颠倒；如果把「输入栈」的元素逐个弹出放到「输出栈」，再从「输出栈」弹出元素的时候，则可以负负得正，实现了先进先出。

* 具体做法：
* 可以把一个栈当做「输入栈」，把另一个栈当做「输出栈」。
* 当 push() 新元素的时候，放到「输入栈」的栈顶。
* 当 pop() 元素的时候，是从「输出栈」弹出元素。如果「输出栈」为空，则把「输入栈」的元素逐个 pop() 并且 push() 到「输出栈」中，这一步会把「输入栈」的栈底元素放到了「输出栈」的栈顶。此时负负得正，从「输出栈」的 pop() 元素的顺序与「输入序」相同。
/ 时间复杂度：push() 时间复杂度是 O(1)；peek()/pop() 均摊时间复杂度是 O(1)，单步操作的最坏时间复杂度是 O(N)。
/ 空间复杂度：空间复杂度是 O(N)，因为总的占用了 N 个元素的空间。

? 两种解法都不错: https://leetcode.cn/problems/implement-queue-using-stacks/solution/yong-zhan-shi-xian-dui-lie-by-leetcode/
? 上面的思路文字来源: https://leetcode-cn.com/problems/implement-queue-using-stacks/solution/dong-hua-jiang-jie-ru-he-shi-yong-liang-6g7ub/
? 动画: https://leetcode.cn/problems/implement-queue-using-stacks/solution/tu-jie-guan-fang-tui-jian-ti-jie-yong-zh-4hru/
*/

var MyQueue = function () {
    this.inStack = [];
    this.outStack = [];
    this.front = null;
};

/**
 * @param {number} x
 * @return {void}
 * * 新元素直接压入 inStack 的栈顶
 */
MyQueue.prototype.push = function (x) {
    this.inStack.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function () {
    //* 如果「输出栈」目前没有元素，需要把「输入栈」中的所有元素放到「输出栈」中，在这过程中「输入栈」的栈顶元素称为了「输出栈」的栈底元素，「输入栈」的栈底元素也就是 "first in" 的元素则成为了「输出栈」的栈顶元素，它会被最先弹出「输出栈」。满足了队列的「FIFO」的原则
    if (this.outStack.length === 0) {
        while (this.inStack.length > 0) {
            let num = this.inStack.pop();
            this.outStack.push(num);
        }
    }
    return this.outStack.pop();
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function () {
    //* 与 pop 方法有同样的逻辑
    if (this.outStack.length === 0) {
        while (this.inStack.length > 0) {
            let num = this.inStack.pop();
            this.outStack.push(num);
        }
    }
    return this.outStack[this.outStack.length - 1];
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function () {
    if (this.outStack.length !== 0) return false;
    if (this.inStack.length !== 0) return false;
    return true;
};
