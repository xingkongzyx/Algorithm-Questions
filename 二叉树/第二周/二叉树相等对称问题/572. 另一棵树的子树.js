/* 
* 要判断一个树 t 是不是树 s 的子树，那么可以判断 t 是否和树 s 的任意子树相等。那么就转化成 100. Same Tree。
* 即，这个题的做法就是在 s 的每个子节点上，判断该子节点是否和 t 相等。
* 
* 判断两个树是否相等的三个条件是与的关系，即：
*   1. 当前两个树的根节点值相等；
*   2. 并且，s 的左子树和 t 的左子树相等；
*   3. 并且，s 的右子树和 t 的右子树相等。
 

* 而判断 t 是否为 s 的子树的三个条件是或的关系，即：
*   1. 当前两棵树相等；
*   2. 或者，t 是 s 的左子树；
*   3. 或者，t 是 s 的右子树。

/ 时间复杂度: 对于每一个 root 上的点 也就是 "O(root)"，都需要做一次深度优先搜索来和 subRoot 匹配, 而进行匹配就是调用 isSameTree 方法, 匹配一次的时间代价是 O(subRoot), 总的时间代价就是 O(root * subRoot)

*/

var isSubtree = function (root, subRoot) {
    if (root === null && subRoot === null) return true;
    else if (root === null || subRoot === null) return false;
    else {
        return (
            isSameTree(root, subRoot) ||
            isSubtree(root.left, subRoot) ||
            isSubtree(root.right, subRoot)
        );
    }
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

const root = new TreeNode(1);
const node1 = new TreeNode(1);
root.left = node1;

const subTree = new TreeNode(1);
console.log(isSubtree(root, subTree));
