/*
 * 那么二叉搜索树采用中序遍历，其实就是一个有序数组。
 *
 * 在一个有序数组上求两个数最小差值，这是不是就是一道送分题了。
 *
 * 最直观的想法，就是把二叉搜索树转换成有序数组，然后遍历一遍数组，就统计出来最小差值了。
 */

var getMinimumDifference = function (root) {
    let traverseResults = [];

    let traverse = function (node) {
        if (node === null) return;
        traverse(node.left);
        traverseResults.push(node.val);
        traverse(node.right);
    };

    traverse(root);
    let minVal = Infinity;
    if (traverseResults.length < 2) return 0;
    for (let i = 1; i < traverseResults.length; i++) {
        let diff = Math.abs(
            traverseResults[i] - traverseResults[i - 1]
        );

        if (diff < minVal) minVal = diff;
    }

    return minVal;
};
