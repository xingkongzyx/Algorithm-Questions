// 解释的图 https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/di-106ti-ti-jie-er-cha-shu-zhi-shi-gou-z-wngj/

/* 
# 树的还原过程描述
* 根据中序遍历和后续遍历的特性我们进行树的还原过程分析
* 
* 1. 首先在后序遍历序列中找到根节点(最后一个元素)
* 2. 根据根节点在中序遍历序列中找到根节点的位置
* 3. 根据根节点的位置将中序遍历序列分为左子树和右子树
* 4. 根据根节点的位置确定左子树和右子树在中序数组和后续数组中的左右边界位置
* 5. 递归构造左子树和右子树
* 6. 返回根节点结束

# 需要定义几个变量帮助我们进行树的还原
* 1. HashMap map 需要一个哈希表来保存中序遍历序列中,元素和索引的位置关系.因为从后序序列中拿到根节点后，要在中序序列中查找对应的位置,从而将数组分为左子树和右子树
* 2. midIdx: 后续遍历元素中的最后意味(也就是根节点)在中序遍历数组中的索引位置
* 3. 中序遍历数组的两个位置标记 [inorderStartIdx, inorderEndIdx]，inorderStartIdx 是起始位置，inorderEndIdx 是结束位置
* 4. 后序遍历数组的两个位置标记 [postorderStartIdx, postorderEndIdx] postorderStartIdx 是起始位置，postorderEndIdx 是结束位置

*/

var buildTree = function (inorder, postorder) {
    let map = {};
    for (let i = 0; i < inorder.length; i++) {
        map[inorder[i]] = i;
    }

    return buildTreeHelper(
        inorder,
        postorder,
        map,
        0,
        inorder.length - 1,
        0,
        postorder.length - 1
    );
};

function buildTreeHelper(
    inorder,
    postorder,
    map,
    inorderStartIdx,
    inorderEndIdx,
    postorderStartIdx,
    postorderEndIdx
) {
    // 直到：无法形成 postOrder 和 inorder 数组，就构建不出子树了，即来到树的底部了，返回 null 节点。通过startIdx和endIdx的大小进行判断
    if (
        inorderStartIdx > inorderEndIdx ||
        postorderStartIdx > postorderEndIdx
    ) {
        return null;
    }

    let rootVal = postorder[postorderEndIdx];
    let rootNode = new TreeNode(rootVal);

    //* 找到后序数组最后一个元素在中序数组的位置，作为切割点
    let midIdx = map[rootVal];
    //* 用于记录在中序数组中左子树一共有多少elements，以便于正确分割后序数组
    const leftSubtreeNodesNum = midIdx - inorderStartIdx;

    //* 确定这个下标midIdx和左子树总共的nodes后，将中序数组分成两部分，后序数组分成两部
    //* 递归处理中序数组左边，后序数组左边

    // ! 此时应该注意确定切割的标准，是左闭右开，还有左开又闭，还是左闭又闭，这个就是不变量，要在递归中保持这个不变量。在切割的过程中会产生四个区间，把握不好不变量的话，一会左闭右开，一会左闭又闭，必然乱套！
    // > 如下代码中我坚持左闭右闭的原则
    let inorderLeftSubtreeStartIdx = inorderStartIdx;
    let inorderLeftSubtreeEndIdx = midIdx - 1;
    let postorderLeftSubtreeStartIdx = postorderStartIdx;
    let postorderLeftSubtreeEndIdx =
        postorderStartIdx + leftSubtreeNodesNum - 1;
    rootNode.left = buildTreeHelper(
        inorder,
        postorder,
        map,
        inorderLeftSubtreeStartIdx,
        inorderLeftSubtreeEndIdx,
        postorderLeftSubtreeStartIdx,
        postorderLeftSubtreeEndIdx
    );
    //* 递归处理中序数组右边，后序数组右边
    let inorderRightSubtreeStartIdx = midIdx + 1;
    let inorderRightSubtreeEndIdx = inorderEndIdx;
    let postorderRightSubtreeStartIdx =
        postorderStartIdx + leftSubtreeNodesNum;
    let postorderRightSubtreeEndIdx = postorderEndIdx - 1;
    postorderStartIdx + leftSubtreeNodesNum - 1;
    rootNode.right = buildTreeHelper(
        inorder,
        postorder,
        map,
        inorderRightSubtreeStartIdx,
        inorderRightSubtreeEndIdx,
        postorderRightSubtreeStartIdx,
        postorderRightSubtreeEndIdx
    );

    return rootNode;
}
