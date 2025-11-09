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
 * @return {number}
 */
var widthOfBinaryTree = function(root) {
    const queue = [[root, 0]]
    let maxLen = 1
    while(queue.length > 0) {
        let queueLen = queue.length;
        maxLen = Math.max(maxLen, queue[queueLen - 1][1] - queue[0][1] + 1)

        const levelStartY = queue[0][1]
        for(let i = 0; i < queueLen; i++) {
            let [node, posY] = queue.shift();
            posY = posY - levelStartY

            if(node.left) {
                queue.push([node.left, 2 * posY])
            }
            if(node.right) {
                queue.push([node.right, 2 * posY + 1])
            }
        }

    }
    return maxLen
};