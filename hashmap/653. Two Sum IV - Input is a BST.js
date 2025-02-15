/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/* 
* 在递归搜索过程中记录下相应的节点值（使用 Set 集合），如果在遍历某个节点 x 时发现集合中存在 k−x.val，说明存在两个节点之和等于 k，返回 True，若搜索完整棵树都没有则返回 False。
? https://leetcode.cn/problems/two-sum-iv-input-is-a-bst/solutions/1354976/by-ac_oier-zr4o/

*/
var findTarget = function (root, k) {
    const set = new Set();

    const findNode = function (node) {
        if (node === null) return false;
        let target = k - node.val;
        if (set.has(target)) return true;

        set.add(node.val);
        return findNode(node.left) || findNode(node.right);
    };

    return findNode(root);
};
