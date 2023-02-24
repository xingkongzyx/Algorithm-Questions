/* 
/ 递归函数 buildTreeHelper 的意义是: 用 preorder数组 [preorderStartIdx, preorderEndIdx] 左闭右闭区间内的节点 和 inorder数组 [inorderStartIdx, inorderEndIdx] 左闭右闭区间内的节点构造子树，并返回根节点
/ 单层递归的逻辑：
/ 1. 首先在前序遍历序列中找到根节点(第一个元素)
/ 2. 根据根节点在中序遍历序列中找到根节点的位置
/ 3. 根据根节点的位置将中序遍历序列分为左子树和右子树
/ 4. 根据根节点的位置确定左子树和右子树在前序数组和中序数组中的左右边界位置
/ 5. 递归构造左子树和右子树
/ 6. 返回根节点结束
? https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/88557/si-lu-qing-xi-dai-ma-jian-ji-he-105ti-si-lu-yi-z-2/
*/
var buildTree = function (preorder, inorder) {
    let map = {};
    for (let i = 0; i < inorder.length; i++) {
        map[inorder[i]] = i;
    }

    return buildTreeHelper(
        preorder,
        inorder,
        map,
        0,
        preorder.length - 1,
        0,
        inorder.length - 1
    );
};

function buildTreeHelper(
    preorder,
    inorder,
    map,
    preorderStartIdx,
    preorderEndIdx,
    inorderStartIdx,
    inorderEndIdx
) {
    if (
        preorderStartIdx > preorderEndIdx ||
        inorderStartIdx > inorderEndIdx
    ) {
        return null;
    }

    let rootVal = preorder[preorderStartIdx];
    let rootNode = new TreeNode(rootVal);

    let midIdx = map[rootVal];
    let leftSubtreeNodesNum = midIdx - inorderStartIdx;

    let inorderLeftSubtreeStartIdx = inorderStartIdx;
    let inorderLeftSubtreeEndIdx = midIdx - 1;
    let preorderLeftSubtreeStartIdx = preorderStartIdx + 1;
    // ! 注意这里 endIdx的算法，它的起始位置并不是 preorderStartIdx，因为preorderStartIdx是root idx, 它真正是起始位置是 preorderStartIdx + 1 也就是preorderLeftSubtreeStartIdx
    let preorderLeftSubtreeEndIdx =
        preorderLeftSubtreeStartIdx + leftSubtreeNodesNum - 1;

    rootNode.left = buildTreeHelper(
        preorder,
        inorder,
        map,
        preorderLeftSubtreeStartIdx,
        preorderLeftSubtreeEndIdx,
        inorderLeftSubtreeStartIdx,
        inorderLeftSubtreeEndIdx
    );

    let inorderRightSubtreeStartIdx = midIdx + 1;
    let inorderRightSubtreeEndIdx = inorderEndIdx;
    //! 与上面的注意原理一致，它的起始位置并不是 preorderStartIdx，因为preorderStartIdx是root idx, 它真正是起始位置是 preorderStartIdx + 1 也就是preorderLeftSubtreeStartIdx
    let preorderRightSubtreeStartIdx =
        preorderLeftSubtreeStartIdx + leftSubtreeNodesNum;
    let preorderRightSubtreeEndIdx = preorderEndIdx;

    rootNode.right = buildTreeHelper(
        preorder,
        inorder,
        map,
        preorderRightSubtreeStartIdx,
        preorderRightSubtreeEndIdx,
        inorderRightSubtreeStartIdx,
        inorderRightSubtreeEndIdx
    );

    return rootNode;
}
