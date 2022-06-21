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
