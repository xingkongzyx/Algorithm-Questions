/*
! 如果不进行 归一化索引，直接使用 2 * index / 2 * index + 1 就会遇到下面的 js 坑点
 * JS 的坑点
 *    - JS 的 Number 是双精度浮点数：
 *    - 安全整数上限：Number.MAX_SAFE_INTEGER = 2^53 - 1
 *    - 超过 2^53 后，整数就不再精确（开始跳着表示）
 *    - 更深一点甚至会变成 Infinity
 *    - 然后你做：lastIdx - firstIdx + 1 可能出现：
 *        - Infinity - Infinity = NaN
 *        - Math.max(maxWidth, NaN) = NaN
 *        - 最终返回 NaN，判题就炸了（有的平台会直接当 Runtime Error / Wrong Answer）
 * 
? https://leetcode.cn/problems/maximum-width-of-binary-tree/solutions/1398999/by-mou-zi-ming-z-naex/
*/

var widthOfBinaryTree = function (root) {
    const queue = [[root, 0]];
    let maxLen = 1;
    while (queue.length > 0) {
        let queueLen = queue.length;
        maxLen = Math.max(
            maxLen,
            queue[queueLen - 1][1] - queue[0][1] + 1
        );

        const levelStartY = queue[0][1];
        for (let i = 0; i < queueLen; i++) {
            let [node, posY] = queue.shift();
            posY = posY - levelStartY;

            if (node.left) {
                queue.push([node.left, 2 * posY]);
            }
            if (node.right) {
                queue.push([node.right, 2 * posY + 1]);
            }
        }
    }
    return maxLen;
};
