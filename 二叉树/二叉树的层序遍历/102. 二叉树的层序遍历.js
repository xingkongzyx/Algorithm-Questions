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

/* 
* 层序遍历一个二叉树。就是从左到右一层一层的去遍历二叉树。这种遍历的方式和我们之前讲过的都不太一样。

* 需要借用一个辅助数据结构即队列来实现，队列先进先出，符合一层一层遍历的逻辑


*/

var levelOrder = function (root) {
    let queue = [];
    if (root !== null) queue.push(root);
    let res = [];
    while (queue.length > 0) {
        let currentLevelSize = queue.length;
        let currentLevelNodes = [];
        while (currentLevelSize > 0) {
            let poppedNode = queue.shift();
            currentLevelNodes.push(poppedNode);
            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);
            currentLevelSize--;
        }
        res.push(currentLevelNodes);
    }
    return res;
};
