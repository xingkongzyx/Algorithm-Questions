var buildTree = function (preorder, inorder) {
    let inOrderMap = {};
    for (let i = 0; i < inorder.length; i++)
        inOrderMap[inorder[i]] = i;

    function buildTreeHelper(
        preStartIdx,
        preEndIdx,
        inStartIdx,
        inEndIdx,
        preorder,
        inorder
    ) {
        if (preStartIdx > preEndIdx || inStartIdx > inEndIdx)
            return null;

        let rootVal = preorder[preStartIdx];
        let rootIdx = inOrderMap[rootVal];
        let leftNodes = rootIdx - inStartIdx;
        let leftPreStartIdx = preStartIdx + 1;
        let leftPreEndIdx = preStartIdx + leftNodes;
        let leftInStartIdx = inStartIdx;
        let leftInEndIdx = rootIdx - 1;

        let newRoot = new TreeNode(rootVal);
        newRoot.left = buildTreeHelper(
            leftPreStartIdx,
            leftPreEndIdx,
            leftInStartIdx,
            leftInEndIdx,
            preorder,
            inorder
        );

        let rightPreStartIdx = leftPreEndIdx + 1;
        let rightPreEndIdx = preEndIdx;
        let rightInStartIdx = rootIdx + 1;
        let rightInEndIdx = inEndIdx;

        newRoot.right = buildTreeHelper(
            rightPreStartIdx,
            rightPreEndIdx,
            rightInStartIdx,
            rightInEndIdx,
            preorder,
            inorder
        );

        return newRoot;
    }

    return buildTreeHelper(
        0,
        preorder.length - 1,
        0,
        inorder.length - 1,
        preorder,
        inorder
    );
};
