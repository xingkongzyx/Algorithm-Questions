/* 
/ 时间复杂度: 构造二叉搜索树的时间为T(n)，则按照递推关系式: T(n)=2T(n/2)+O(n) 
! 由 Master Theorem，这里的时间: T(n) = O(nlogn)
/ 空间复杂度：除了需要返回的构造出的树的空间外，栈的最大深度是平衡二叉树的高度，既然是平衡二叉树，那么深度为 O(logn)
? 参考: https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/solution/you-xu-lian-biao-zhuan-huan-er-cha-sou-suo-shu-1-3/

> 还有使用中序遍历的更优解法, 下次再看
*/
var sortedListToBST = function (head) {
    /// 递归函数的意义是 用链表的[head, tail)左闭右开区间内的节点构造子树，并返回根节点
    function buildTreeHelper(head, tail) {
        if (head == tail) return null;

        //# 中
        let midNode = findMidNode(head, tail);
        let rootVal = midNode.val;
        let rootNode = new TreeNode(rootVal);

        //# 左
        rootNode.left = buildTreeHelper(head, midNode);
        //# 右
        rootNode.right = buildTreeHelper(midNode.next, tail);
        return rootNode;
    }

    return buildTreeHelper(head, null);
};

var findMidNode = function (head, tail) {
    let slow = head;
    let fast = head;
    while (fast !== tail && fast.next !== tail) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
};
