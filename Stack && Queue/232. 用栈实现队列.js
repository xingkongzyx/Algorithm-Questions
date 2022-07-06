/* 
* 思路是：「输入栈」会把输入顺序颠倒；如果把「输入栈」的元素逐个弹出放到「输出栈」，再从「输出栈」弹出元素的时候，则可以负负得正，实现了先进先出。

* 具体做法：
* 可以把一个栈当做「输入栈」，把另一个栈当做「输出栈」。
* 当 push() 新元素的时候，放到「输入栈」的栈顶，记此顺序为「输入序」。
* 当 pop() 元素的时候，是从「输出栈」弹出元素。如果「输出栈」为空，则把「输入栈」的元素逐个 pop() 并且 push() 到「输出栈」中，这一步会把「输入栈」的栈底元素放到了「输出栈」的栈顶。此时负负得正，从「输出栈」的 pop() 元素的顺序与「输入序」相同。
https://juejin.cn/post/7059689486787018765
https://leetcode-cn.com/problems/implement-queue-using-stacks/solution/dong-hua-jiang-jie-ru-he-shi-yong-liang-6g7ub/
*/

var MyQueue = function () {
    this.inStack = [];
    this.outStack = [];
};

/**
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function (x) {
    this.inStack.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function () {
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

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */

var obj = new MyQueue();
obj.push(1);
obj.push(2);
obj.push(3);
var param_2 = obj.pop();
param_2 = obj.pop();
var param_3 = obj.peek();
var param_4 = obj.empty();
console.log([param_2, param_3, param_4]);
