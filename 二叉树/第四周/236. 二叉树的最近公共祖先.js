/* 
> 后序遍历
> 时间复杂度是 O(n)：每个结点最多遍历一次，空间复杂度是 O(n)：需要系统栈空间
* 从根节点 root 开始往下递归遍历……
* 
* 如果遍历到 p 或 q，比方说 p，则 lowestCommonAncestor 要么是当前的 p（q 在 p 的子树中），要么是 p 之上的节点（q 不在 p 的子树中），不可能是 p 之下的节点，不用继续往下走，返回当前的 p。
* 
* 当遍历到 null 节点，空树不存在 p 和 q，没有 LCA，返回 null。
* 
* 当遍历的节点 root 不是 p 或 q 或 null，则递归搜寻 root 的左右子树：
* 
* 如果左右子树的递归都有结果，说明 p 和 q 分居 root 的左右子树，返回 root。
* 如果只是一个子树递归调用有结果，说明 p 和 q 都在这个子树，返回该子树递归结果。
* 如果两个子树递归结果都为 null，说明 p 和 q 都不在这俩子树中，返回 null。 

? 1. https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/zui-jin-gong-gong-zu-xian-tong-guo-yan-shen-ding-y/
? 2. https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/jsersi-lu-hao-li-jie-by-hyj8/
*/

var lowestCommonAncestor = function (root, p, q) {
    //> 这道题一共有两个终止条件，一个是当遇到root为null时
    if (root === null) return null; // 遇到null，返回null 没有LCA
    //> 这道题一共有两个终止条件，另一个是当遇到root为 p 或者 q时，说明此时node的LCA肯定不在root的下面，所以直接返回root
    if (root === p || root === q) return root; // 遇到p或q，直接返回当前节点
    // 非null 非q 非p，则递归左右子树
    let leftCheck = lowestCommonAncestor(root.left, p, q);
    let rightCheck = lowestCommonAncestor(root.right, p, q);
    // 根据递归的结果，决定谁是LCA
    if (leftCheck && rightCheck) return root;
    else if (leftCheck) return leftCheck;
    else if (rightCheck) return rightCheck;
    else return null;
};
