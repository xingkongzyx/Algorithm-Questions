/* 
? https://leetcode.cn/problems/online-stock-span/solutions/2470527/shi-pin-yi-ge-shi-pin-jiang-tou-dan-diao-cuk7/
*/
var StockSpanner = function () {
    this.stack = [[-1, Infinity]];
    this.index = 0;
};

/**
 * @param {number} price
 * @return {number}
 */
StockSpanner.prototype.next = function (price) {
    while (this.stack[this.stack.length - 1][1] <= price) {
        this.stack.pop();
    }

    let res = this.index - this.stack[this.stack.length - 1][0];
    this.stack.push([this.index, price]);
    this.index++;
    return res;
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */
