/* 
思路来自于 https://www.youtube.com/watch?v=RXy5RzGF5wo 基于中序遍历的迭代的思路
*/
/**
 * @param {TreeNode} root
 */
var BSTIterator = function (root) {
    this.stack = [];

    let curNode = root;
    while (curNode) {
        this.stack.push(curNode);
        curNode = curNode.left;
    }
};

/**
 * @return {number}
 */
BSTIterator.prototype.next = function () {
    let resNode = this.stack.pop();
    let curNode = resNode.right;

    while (curNode) {
        this.stack.push(curNode);
        curNode = curNode.left;
    }

    return resNode.val;
};

/**
 * @return {boolean}
 */
BSTIterator.prototype.hasNext = function () {
    return this.stack.length !== 0;
};
