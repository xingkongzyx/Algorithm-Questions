/* 
> 后序遍历
> 时间复杂度是 O(n)：每个结点最多遍历一次，空间复杂度是 O(n)：需要系统栈空间

* 当我们用递归去做这个题时不要被题目误导，应该要明确一点
* 这个函数的功能有三个：给定两个节点 p 和 q
* 
* 如果 p 和 q 都存在，则返回它们的公共祖先；
* 如果只存在一个，则返回存在的一个；
* 如果 p 和 q 都不存在，则返回NULL
* 
* 链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/solution/c-jing-dian-di-gui-si-lu-fei-chang-hao-li-jie-shi-/


? 1. https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/zui-jin-gong-gong-zu-xian-tong-guo-yan-shen-ding-y/
? 2. https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/jsersi-lu-hao-li-jie-by-hyj8/

*/

var lowestCommonAncestor = function (root, p, q) {
    //* 遇到null，返回null 没有LCA
    if (root === null) return null;
    //* 只要当前根节点是p和q中的任意一个，就返回（因为不能比这个更深了，再深p和q中的一个就没了）
    if (root === p || root === q) return root;

    //* 根节点不是p和q中的任意一个，那么就继续分别往左子树和右子树找p和q
    let leftCheck = lowestCommonAncestor(root.left, p, q);
    let rightCheck = lowestCommonAncestor(root.right, p, q);

    //* 根据递归的结果，决定谁是LCA
    if (leftCheck === null && rightCheck === null) {
        //* p和q都没找到，那就没有
        return null;
    } else if (rightCheck === null) {
        return leftCheck;
    } else if (leftCheck === null) {
        return rightCheck;
    } else {
        return root;
    }
};
