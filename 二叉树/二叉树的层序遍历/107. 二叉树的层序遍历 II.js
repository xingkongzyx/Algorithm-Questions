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
 * @return {number[][]}
 */
var levelOrderBottom = function (root) {
    //! 相当于102题目得到结果后再进行reverse
    let res = [];
    let queue = [];
    if (root !== null) queue.push(root);

    while (queue.length > 0) {
        let size = queue.length;
        let currentLevelNodes = [];
        while (size > 0) {
            let poppedNode = queue.shift();
            currentLevelNodes.push(poppedNode.val);
            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);
            size--;
        }
        res.push(currentLevelNodes);
    }
    // 把 res 进行reverse
    let left = 0,
        right = res.length - 1;
    while (left < right) {
        [res[left], res[right]] = [res[right], res[left]];
        left++;
        right--;
    }
    return res;
};
