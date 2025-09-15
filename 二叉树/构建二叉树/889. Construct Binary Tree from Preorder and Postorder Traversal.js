/* 
! 为什么其他构造题目例如 "中序 + 后序" 就不需要 `preStart === preEnd` 这种叶子判断?
## 关键区别

* **前序 + 后序**
  为了切分左右子树，你需要读取**左子树根**：`preorder[preStart + 1]`。
  当当前区间只剩 **1 个节点** 时（叶子），`preStart + 1` 会**越界**，从而把 `postOrderNodePos` 搞成 `undefined`，区间计算变成 `NaN`，递归失控 → 栈溢出。
  所以这里**必须**在叶子处提前返回：`if (preStart === preEnd) return newNode;`。

* **中序 + 后序**
  切分左右子树完全依赖：

  * 根：`postorder[postorderEnd]`（当前区间非空时一定存在）
  * 根在中序的位置：`inorderMap.get(rootVal)`（也一定存在）

  当只有 **1 个节点** 时：

  * `midNodeVal = postorder[postorderEnd]` 正常
  * `midNodeInInorderPos = inorderStart = inorderEnd`
  * `numNodes = 0`
  * 递归调用区间会变成**空区间**：

    * 左：`[inorderStart, mid-1]` → 空
    * 右：`[mid+1, inorderEnd]` → 空
  * 这两次都会直接命中你的**空区间终止条件**：
    `if (inorderStart > inorderEnd || postorderStart > postorderEnd) return null;`

  全程**没有访问到“下一个元素”**这种可能越界的操作，因此**不需要**额外的“单节点返回”判断（当然，作为性能小优化加上也可以）。

## 一句话总结

* **前序+后序**：需要访问 `preorder[preStart + 1]` 来找左根 → 叶子时会越界 → **必须**加 `preStart === preEnd` 的叶子判断来提前返回。
* **中序+后序**：切分只用当前根和其中序位置，**不会访问相邻元素**，单节点时两边都自然变成空区间，由空区间的基准条件兜底 → **可以不加**叶子判断。

## 额外补充

* 中序+后序在“值唯一”的前提下能唯一确定二叉树；但前序+后序一般**不唯一**，我们常用“取 `preStart+1` 作为左根”来选择一种可行划分，这正是需要叶子判断的那步。
* 实际写法里，给中序+后序也加个 `if (inL===inR) return node;` 只是**优化**（少一次或两次空递归），不是**正确性**所必需。

*/

var constructFromPrePost = function (preorder, postorder) {
    const postorderMap = new Map();
    for (let i = 0; i < postorder.length; i++) {
        postorderMap.set(postorder[i], i);
    }

    // post: left right cur
    // pre: cur left right
    function buildTree(postStart, postEnd, preStart, preEnd) {
        if (postStart > postEnd || preStart > preEnd) return null;

        let nodeVal = preorder[preStart];
        let newNode = new TreeNode(nodeVal);

        // 只有一个节点（叶子），直接返回，避免访问 preorder[preStart + 1]
        if (preStart === preEnd) return newNode;

        // 左子树根在前序中的位置是 preStart + 1
        let postOrderNodePos = postorderMap.get(
            preorder[preStart + 1]
        );

        // 左子树节点数
        let leftNodes = postOrderNodePos - postStart + 1;

        // 切分区间：
        // 前序: [根][左子树 leftNodes][右子树 ...]
        // 后序: [左子树 leftNodes][右子树 ...][根]
        newNode.left = buildTree(
            postStart,
            postOrderNodePos,
            preStart + 1,
            preStart + leftNodes
        );
        newNode.right = buildTree(
            postOrderNodePos + 1,
            postEnd - 1,
            preStart + leftNodes + 1,
            preEnd
        );

        return newNode;
    }

    return buildTree(0, postorder.length - 1, 0, preorder.length - 1);
};
