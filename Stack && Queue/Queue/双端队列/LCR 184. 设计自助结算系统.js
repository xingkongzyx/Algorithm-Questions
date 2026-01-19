/* 
? 动画: https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/solutions/136701/ru-he-jie-jue-o1-fu-za-du-de-api-she-ji-ti-by-z1m
? 图片: https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/solutions/540181/jian-zhi-offer-59-ii-dui-lie-de-zui-da-z-0pap/
*/
class MaxQueue {
    constructor() {
        // 普通队列
        this.queue = [];
        // 单调递减双端队列
        this.deque = [];
    }

    get_max() {
        return this.deque.length ? this.deque[0] : -1;
    }

    add(value) {
        // 维护单调递减队列
        while (
            this.deque.length &&
            this.deque[this.deque.length - 1] < value
        ) {
            this.deque.pop();
        }
        this.deque.push(value);
        this.queue.push(value);
    }

    remove() {
        if (!this.queue.length) return -1;

        const ans = this.queue.shift();
        if (ans === this.deque[0]) {
            this.deque.shift();
        }
        return ans;
    }
}
