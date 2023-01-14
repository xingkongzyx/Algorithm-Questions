/* 
* 要判断一个树 t 是不是树 s 的子树, 那么可以判断 t 是否和树 s 的任意子树相等。那么就转化成 100. Same Tree。
* 即, 这个题的做法就是在 s 的每个子节点上, 判断该子节点是否和 t 相等。

* 判断 t 是否为 s 的『子树』的三个条件是『或的关系』, 即: 
*   1. 当前两棵树相等；
*   2. 或者, t 是 s 的左子树；
*   3. 或者, t 是 s 的右子树。

* 判断两个树是否『相等』的三个条件是『与的关系』, 即: 
*   1. 当前两个树的根节点值相等；
*   2. 并且, s 的左子树和 t 的左子树相等；
*   3. 并且, s 的右子树和 t 的右子树相等。
 

 * 递归函数 isSameTree 的作用是: 检查「root子树」与「subRoot子树」是否是相同的子树
 * 递归函数 isSubtree 的作用是: 检查「root子树」中是否包含「subRoot子树」, 其中需要用到辅助函数 isSameTree 帮助判断两个子树是否是相等的


/ 时间复杂度: m is the number of nodes in the 1st tree and n is the number of nodes in the 2nd tree. 对于每一个 root 上的点 也就是 "O(m)", 都需要做一次深度优先搜索来和 subRoot 匹配, 而进行匹配就是调用 isSameTree 方法, 匹配一次的时间代价是 O(n), 总的时间代价就是 O(m * n). worst case: for each node in the 1st tree, we need to check if isSame(Node s, Node t). Total m nodes, isSame(...) takes O(n) worst case
/ Space complexity: O(height of 1str tree)(Or you can say: O(m) for worst case, O(logm) for average case)
*/

var isSubtree = function (root, subRoot) {
    if (root == null) return false;

    // # 中
    // # For each node during pre-order traversal of root, use a recursive function isSameTree to validate if sub-tree started with this node is the same with t.
    let cur_root_check = isSameTree(root, subRoot);
    if (cur_root_check === true) return true;

    // # 左
    let left_check = isSubtree(root.left, subRoot);
    // # 右
    let right_check = isSubtree(root.right, subRoot);

    return left_check || right_check;
};

var isSameTree = function (p, q) {
    if (p === null && q !== null) return false;
    else if (p !== null && q === null) return false;
    else if (p === null && q === null) return true;
    else if (p.val !== q.val) return false;
    else {
        let leftCheck = isSameTree(p.left, q.left);
        let rightCheck = isSameTree(p.right, q.right);
        return leftCheck && rightCheck;
    }
};

// const root = new TreeNode(1);
// const node1 = new TreeNode(1);
// root.left = node1;

// const subTree = new TreeNode(1);
// console.log(isSubtree(root, subTree));
