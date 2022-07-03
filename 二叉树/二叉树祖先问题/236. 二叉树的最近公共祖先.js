/* 
! 后序遍历
/ 时间复杂度是 O(n): 每个结点最多遍历一次, 空间复杂度是 O(n): 需要系统栈空间

* 
! 本题比较关键的地方是递归函数不能直接设计成『找 p 和 q 节点的最近公共祖先』. 这么设计的话 leftRes 或者 rightRes 就不可能有都不为 null 的情况. 如果这两个的值都不为 null, 意思就是 root 的左子树里面可以找到 『p 和 q 节点的最近公共祖先』, root 的右子树里面也可以找到『p 和 q 节点的最近公共祖先』。既然在递归左右子树后就已经获得了『p 和 q 节点的最近公共祖先』, 为什么还需要后面针对当前节点进行判断呢, 逻辑无法说通, 所以将递归函数的功能理解为〖帮 p 和 q 找到一个最近的祖先〛就行. 更具体地说函数功能分为三个更加符合逻辑. 

*.这个函数的功能是有三个: 
*  ➀ 如果 p 和 q 都存在, 则返回它们的公共祖先；
*  ➁ 如果只存在一个, 则返回存在的一个；
*  ➂ 如果 p 和 q 都不存在, 则返回 null
* 输入: 该树的根节点, 两个指定节点
* 输出: 函数功能三种情况之一
# 核心在于两点 （1）递归函数的多种功能 （2）当 p, q 存在时, 确实能返回 lca

/ 这样理解可能更加清楚一点: lowestCommonAncestor 这个函数不要理解为「找最近公共祖先」, 而就理解为帮两个节点「找最近的祖先」. 传入的值是 root, p, q, 在「以 root 为根节点的子树中」帮 p 和 q 找到一个祖先就行, 找到两个就更好了, 如果找不到祖先就返回 null. 在「以 root->left 为根节点的子树」里面找一次, 在「以 root->right 为根节点的子树」里面再找一次. 如果某一边返回值是 null, 那么说明「p 的祖先」和「q 的祖先」都在另一边. 由于找的时候, 一定是找的「最近的祖先」返回, 所以这里直接返回前面的返回值就行了, 可以保证是最近的公共祖先. 如果左右的返回值都不是null, 那说明「p 的祖先」和「q 的祖先」分别在两边, 则当前节点就是「最近公共祖先」. 左右都找不到就直接返回 null
? https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/solution/c-jing-dian-di-gui-si-lu-fei-chang-hao-li-jie-shi-/486473


? 对于函数的作用说的很明白: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/solution/c-jing-dian-di-gui-si-lu-fei-chang-hao-li-jie-shi-/


? 来自笨猪爆破组: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/jsersi-lu-hao-li-jie-by-hyj8/



*/

var lowestCommonAncestor = function (root, p, q) {
    //* 当遍历到 null 节点, 空树不存在 p 和 q, 没有 LCA, 返回 null.
    if (root === null) return null;
    //* 只要当前根节点是 p 和 q 中的任意一个, 就返回（因为不能比这个更深了, 再深 p 和 q 中的一个就没了）符合函数的功能 ➁
    if (root === p || root === q) return root;

    //* 根节点不是p和q中的任意一个, 那么就继续分别往左子树和右子树找p和q
    let leftRes = lowestCommonAncestor(root.left, p, q);
    let rightRes = lowestCommonAncestor(root.right, p, q);

    //* 根据递归的结果, 决定谁是LCA
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
        //* 如果左右子树的递归都有结果, 说明 p 和 q 分居 root 的左右子树, 返回 root.
        return root;
    }
};
