/* 
! 注意：由于连接孩子结点需要用到父节点的 next 指针, 所以这里的 dfs 只能采用树中的 “先序遍历” 的方法：先将父结点的 next 指向设置好才能递归的处理孩子结点
? 原因的来源: https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/solution/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-3f7ak/

# 最关键的点是可以通过上一层递归 搭出来的线，进行本次搭线
? 来源代码随想录: https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/solution/116-di-gui-yu-die-dai-xiang-jie-by-carls-k8od/ 

? 猪猪爆破组的整体解释: https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/solution/shou-hua-tu-jie-dfs-di-gui-yi-yu-li-jie-by-xiao_be/ 
*/

var connect = function (root) {
    //* 递归终止条件, 因为需要用到父节点来操作其左子节点 .next 指向其右子节点。当到达叶子节点后无法没有子节点, 自然无法进行这样的操作。所以最后一次的递归的执行是在叶子结点的上一层然后对叶子结点进行操作
    if (root == null) return null;
    function traverse(node) {
        if (node.left == null && node.right == null) return;
        //* 因为到达叶子节点就直接返回了, 又因为是 perfect tree, 所以 node 的左孩子肯定有右邻居
        node.left.next = node.right;
        //* 如果父亲节点有右邻居(也就是 next 不为空), 那么父节点的右孩子(node.right)一定也有右邻居(node.next.left), 通过 next 进行连接
        if (node.next) {
            node.right.next = node.next.left;
        }
        //* 前序遍历
        connect(node.left);
        connect(node.right);
    }

    traverse(root);
    return root;
};
