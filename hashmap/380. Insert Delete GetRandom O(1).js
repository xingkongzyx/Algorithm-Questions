// ? https://leetcode.cn/problems/insert-delete-getrandom-o1/solution/o1-shi-jian-cha-ru-shan-chu-he-huo-qu-su-rlz2/

var RandomizedSet = function () {
    this.data = [];
    this.map = new Map();
};

/**
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function (val) {
    if (this.map.has(val)) return false;

    let curLen = this.data.length;
    this.map.set(val, curLen);
    this.data.push(val);
    // console.log(this.data)
    // console.log(this.map)
    return true;
};

/**
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function (val) {
    if (!this.map.has(val)) return false;

    const delIdx = this.map.get(val); // 要删除的下标
    const lastIdx = this.data.length - 1; // 最后一个下标
    const lastVal = this.data[lastIdx]; // 最后一个值

    // 如果删除的不是最后一个元素，就把最后一个元素换到 delIdx
    if (delIdx !== lastIdx) {
        this.data[delIdx] = lastVal;
        this.map.set(lastVal, delIdx); // 更新 lastVal 在 map 中的新位置
    }

    // 删掉最后一个元素（原来的 lastVal 或目标值）
    this.data.pop();
    this.map.delete(val);

    return true;
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function () {
    let randIdx = Math.floor(Math.random() * this.data.length);
    return this.data[randIdx];
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
