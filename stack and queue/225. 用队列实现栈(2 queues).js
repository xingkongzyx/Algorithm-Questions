/* 
注意: 与232的不同之处: 
注意: 队列是先进先出的规则，把一个队列中的数据导入另一个队列中，数据的顺序并没有变，并没有变成先进后出的顺序。
! 所以用栈实现队列， 和用队列实现栈的思路还是不一样的，这取决于这两个数据结构的性质。

https://programmercarl.com/0225.%E7%94%A8%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0%E6%A0%88.html
*/
var MyStack = function () {
    this.mainQueue = [];
    this.helperQueue = [];
};

/**
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function (x) {
    this.mainQueue.push(x);
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function () {
    //* 把mainQueue中除了最后一个元素外的元素放到helperQueue中，然后pop from front得到正确结果，最后把helperQueue中的元素再放回mainQueue
    let size = this.mainQueue.length;
    while (size > 1) {
        this.helperQueue.push(this.mainQueue.shift());
        size--;
    }
    let popElement = this.mainQueue.shift();
    while (this.helperQueue.length > 0) {
        this.mainQueue.push(this.helperQueue.shift());
    }
    return popElement;
};

/**
 * @return {number}
 */
MyStack.prototype.top = function () {
    let topNum = this.pop();
    this.mainQueue.push(topNum);
    return topNum;
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function () {
    return this.mainQueue.length === 0;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
