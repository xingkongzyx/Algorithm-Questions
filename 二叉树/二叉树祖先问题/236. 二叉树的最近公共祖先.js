/* 
! 后序遍历

* 本题比较关键的地方是递归函数不能直接理解成『找 p 和 q 节点的最近公共祖先』. 这么设计的话 leftRes 或者 rightRes 就不可能有都不为 null 的情况. 如果这两个的值都不为 null, 意思就是『root 的左子树』里面可以找到 『p 和 q 节点的最近公共祖先』,『root 的右子树』里面也可以找到『p 和 q 节点的最近公共祖先』。既然在递归左右子树后就已经获得了『p 和 q 节点的最近公共祖先』, 为什么还需要后面针对当前节点进行判断呢, 逻辑无法说通, 所以将递归函数的功能理解为〖帮 p 或者 q 找到一个最近的祖先〛就行

# 注意两种定义的区别: 「公共祖先」是两个节点的祖先，「祖先」是可以一个节点的

/ lowestCommonAncestor 这个函数不要理解为「找最近公共祖先」, 而就理解为帮两个节点「找最近的祖先」. 传入的值是 root, p, q, 在「以 root 为根节点的子树中」帮 p 和 q 找到一个祖先就行, 找到两个就更好了, 如果找不到祖先就返回 null. 在以 root->left 为根节点的子树里面找一次, 在以 root->right 为根节点的子树里面再找一次. 如果某一边返回值是 null, 那么说明「p 的祖先」和「q 的祖先」都在另一边. 由于找的时候, 一定是找的「最近的祖先」返回, 所以这里直接返回前面的返回值就行了, 可以保证是最近的公共祖先. 如果左右的返回值都不是null, 那说明「p 的祖先」和「q 的祖先」分别在两边, 则当前节点就是「最近公共祖先」. 左右都找不到就直接返回 null
? https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/solution/c-jing-dian-di-gui-si-lu-fei-chang-hao-li-jie-shi-/486473

? 来自笨猪爆破组: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/jsersi-lu-hao-li-jie-by-hyj8/

/ 时间复杂度是 O(n): 每个结点最多遍历一次
/ 空间复杂度是 O(n): 需要系统栈空间
*/

var lowestCommonAncestor = function (root, p, q) {
    //* 当遍历到 null 节点, 空树不存在 p 和 q, 没有「最近的祖先」, 返回 null.
    if (root === null) return null;

    //* 如果遍历到 p 或 q, 比方说 p, 则「最近的祖先」 要么是当前的 p(q 在 p 的子树中), 要么是 p 之上的节点(q 不在 p 的子树中), 不可能是 p 之下的节点, 不用继续往下走, 返回当前的 p。
    if (root === p || root === q) return root;

    //* 根节点不是 p 和 q 中的任意一个, 那么就继续分别往左子树和右子树找 p 和 q 的「最近的祖先」, 找到一个就可以返回
    let leftRes = lowestCommonAncestor(root.left, p, q);
    let rightRes = lowestCommonAncestor(root.right, p, q);

    //* 根据递归的结果, 决定谁是 p 和 q 的「最近的祖先」
    if (leftRes === null && rightRes === null) {
        //* 如果两个子树递归结果都为 null, 说明 p 和 q 都不在这俩子树中, 返回 null.
        return null;
    } else if (rightRes === null) {
        //* 如果只是一个子树递归调用有结果, 说明 p 和 q 都在这个子树, 返回该子树递归结果.
        return leftRes;
    } else if (leftRes === null) {
        //* 如果只是一个子树递归调用有结果, 说明 p 和 q 都在这个子树, 返回该子树递归结果.
        return rightRes;
    } else {
        //* 如果左右子树的递归都有结果, 说明 p 和 q 的「最近的祖先」分居 root 的左右子树, 那他们两个总体的「最近的祖先」就是 root
        return root;
    }
};
