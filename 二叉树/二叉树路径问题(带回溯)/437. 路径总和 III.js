/* 
两节点间的路径和 = 两节点的前缀和之差
* 递归函数的意义: 更新以当前节点作为路径的最后一个节点时满足路径和的结果数量
/ 时间复杂度: 每个节点只遍历一次, O(N).
/ 空间复杂度: 开辟了一个hashMap, O(N).

? https://leetcode.cn/problems/path-sum-iii/solutions/596361/dui-qian-zhui-he-jie-fa-de-yi-dian-jie-s-dey6/?orderBy=most_votes
 */

function pathSum(root, targetSum) {
    if (root === null) {
        return 0;
    }
    let preSumMap = { 0: 1 };
    let count = 0;
    let currentSum = root.val;

    const traverse = (node) => {
        // * 这里使用前缀和从而判断是否有路径和满足 targetSum 的条件
        if (preSumMap[currentSum - targetSum] !== undefined) {
            // console.log(node.val, preSumMap);
            count += preSumMap[currentSum - targetSum];
        }
        // # preSumMap 必须更新. 更新的时机要不在当前(遍历到当前节点时更新), 要不在遍历左右子树时提前更新 (两个 if 中更新, 回溯也要在那里进行)
        preSumMap[currentSum] = (preSumMap[currentSum] || 0) + 1;

        // 递归的终止条件, 一旦遇到了叶子节点就不会再往下继续遍历, 因为代码中没有处理空节点的逻辑, 没有左右子节点会自动结束, 不需要加明显的停止条件
        // if (node.left === null && node.right === null) {
        //     return;
        // }

        if (node.left) {
            currentSum += node.left.val;
            traverse(node.left);
            // preSumMap[currentSum] -= 1;
            currentSum -= node.left.val;
        }

        if (node.right) {
            currentSum += node.right.val;
            traverse(node.right);
            // preSumMap[currentSum] -= 1;
            currentSum -= node.right.val;
        }

        //! 非常关键, 当我们遍历另一条路径时不希望已经遍历过的节点还储存在 preSumMap 中, 这样会导致结果错误. 所以在前面遍历完左/右子树后将最开始加入 preSumMap 的项撤回.
        preSumMap[currentSum] -= 1;
    };

    traverse(root);
    return count;
}
