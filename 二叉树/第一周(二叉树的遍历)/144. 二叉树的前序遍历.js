/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function (root) {
    let res = [];
    traverseHelper(root, res);
    return res;
};

function traverseHelper(current, res) {
    if (current === null) return;
    res.push(current.val);
    traverseHelper(current.left, res);
    traverseHelper(current.right, res);
}
