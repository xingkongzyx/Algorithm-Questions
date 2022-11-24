/* 
! 注意：当我们遍历到「当前节点」的具体操作是连接「当前节点」的两个孩子节点以及「当前节点的右孩子节点」和「当前节点的 next 节点的左孩子节点」。由于连接「当前节点」的孩子结点需要用到「当前节点」的 next 指针, 只有「从顶向下」的前序遍历才能在上一层将「当前节点」的 next 指向设置好。所以这里的 dfs 只能采用树中的 『前序遍历』 的方法：
? 原因的来源: https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/solution/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-3f7ak/

# 最关键的点是可以通过上一层递归 搭出来的线，进行本次搭线
? 来源代码随想录: https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/solution/116-di-gui-yu-die-dai-xiang-jie-by-carls-k8od/ 

? 猪猪爆破组的整体解释: https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/solution/shou-hua-tu-jie-dfs-di-gui-yi-yu-li-jie-by-xiao_be/ 

*/

var connect = function (root) {
    if (root == null) return null;
    function traverse(node) {
        //* 递归终止条件, 因为需要用到父节点来操作其「左子节点 .next」 指向其「右子节点」。当到达叶子节点后因为没有子节点, 自然无法进行这样的操作。所以最后一次的递归的执行是在叶子结点的上一层对最后一层的叶子结点进行操作
        if (node.left == null && node.right == null) return;
        //# 中
        //* 因为到达叶子节点就直接返回了, 所以遍历到这里的时候「当前节点」一定有子节点。又因为是 perfect tree, 所以 「当前节点」 的左孩子肯定有右邻居
        node.left.next = node.right;

        //* 如果「当前节点」有右邻居(也就是 node.next 不为空, next指针是是通过上一层遍历被赋值的), 那么「当前节点」的右孩子(node.right) 一定也有属于它的右邻居(node.next.left), 「node.right」与「node.next.left」通过 next 进行连接
        if (node.next) {
            node.right.next = node.next.left;
        }
        //# 左
        //! 虽然递归函数有返回值，但因为在递归过程中没有改变 left, right 的指向，所以即使有返回值也不需要使用 node.left 以及 node.right 来承接
        connect(node.left);
        //# 右
        connect(node.right);
    }

    traverse(root);
    return root;
};
