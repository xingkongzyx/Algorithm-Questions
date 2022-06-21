var MyStack = function () {
    // 用一个队列模拟栈的操作
    this.queue = [];
};

/**
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function (x) {
    this.queue.push(x);
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function () {
    // 我们将最后push元素之前的所有元素pop from front 然后 push to back, 这样最后push的element就成为了 queue head,能够pop from front并且顺序是正确的
    let len = this.queue.length;
    while (len > 1) {
        this.queue.push(this.queue.shift());
        len--;
    }
    return this.queue.shift();
};

/**
 * @return {number}
 */
MyStack.prototype.top = function () {
    //# 与 pop 思路类似: 都是想办法把最后push to queue back的element想办法移动到第一个，这样能直接获取那个元素。但是与pop不同的是，我们需要恢复成原来的顺序以便我们之后调用 pop 时能顺利运行。
    //? queue = [1,2,3,4] 进行top()操作
    //? 使得4变为第一个front element queue = [4,1,2,3]
    //? 此时 queue.pop() = 4, queue => [1,2,3]. 最后将这个元素插到队尾从而恢复了原来的顺序 queue.push(4) queue => [1,2,3,4]
    let len = this.queue.length;
    while (len > 1) {
        this.queue.push(this.queue.shift());
        len--;
    }
    let num = this.queue.shift();
    this.queue.push(num);
    return num;
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function () {
    return this.queue.length === 0;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */

var obj = new MyStack();
obj.push(3);
obj.push(4);
obj.push(5);
console.log(obj.queue);
var param_2 = obj.pop();
console.log(param_2);
var param_3 = obj.top();
console.log(param_3);
var param_4 = obj.empty();
console.log(param_4);
