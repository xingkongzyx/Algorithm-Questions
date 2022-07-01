/*
! 中序遍历
? https://leetcode.cn/problems/recover-binary-search-tree/solution/tu-jie-hui-fu-yi-ge-er-cha-sou-suo-shu-by-hyj8/

* 题目告诉我们是在一个有序的二叉搜索树中有两个节点被交换了, 那么存在两种交换情况：
* ➀ 相邻节点交换；这种情况下只有一对前后关系是错误的
* ➁ 不相邻节点交换。这种情况下, 有两对前后关系是错误的, 其中第一对错误的关系中, 一定是前面那个数错了；第二对错误关系中, 一定是后面那个数错了。
# ⒛ 大数换到前面, 肯定是比其后面的数大导致关系错, 小数换到后面肯定是比它前面的数小导致关系错误。）

/ 时间复杂度：最坏情况下（即待交换节点为二叉搜索树最右侧的叶子节点）我们需要遍历整棵树, 时间复杂度为 O(N), 其中 N 为二叉搜索树的节点个数。
/ 空间复杂度：O(H), 其中 H 为二叉搜索树的高度。中序遍历的时候栈的深度取决于二叉搜索树的高度。
 */
var recoverTree = function (root) {
    let err1Node = null;
    let err2Node = null;
    //* prev 保存上一个访问的节点, 当前访问的是 root 节点。
    let prev = null;
    /*
     * 1.确定递归函数的参数以及返回值
     * 函数作用: 在「以 node 为根节点的二叉树」中寻找被错误地交换的「两个节点」, 并将其用 err1Node, err2Node 记录
     * 输入: 「二叉搜索树」的根节点 node
     * 输出: 没有返回值
     * * 2. 确定终止条件
     * 终止条件就是遍历到节点为 null 的时候, 说明之后不会有被错误地交换的「两个节点」, 停止继续递归
     */
    function helper(node) {
        if (node === null) return;
        //# 左
        helper(node.left);

        //# 中
        if (prev) {
            //* 找到两个节点不满足『前小后大』的关系, 且此时 err1Node 为空, 就说明找到了『第一对错误关系』, 无论是〖相邻的节点〗交换出错还是〖不相邻的节点〗交换出错, 都可以确定第一个错误节点是 prev 节点
            if (prev.val >= node.val && err1Node === null)
                err1Node = prev;
            //* 找到两个节点不满足『前小后大』的关系, 且此时 err1Node 不为空, 此时处于找到了『第一对错误关系』或者『第二对错误关系』的情况. 如果是「相邻节点交换」交换出错, 那么只有一对『错误关系』, 在执行完上面的 if 后直接执行下面这个 if 能找到交换的另一个节点。
            //* 如果是〖不相邻的节点〗交换出错, 说明有两对『错误关系』. 那么在第一次执行完上面的 if 后会直接执行下面这个 if 找到了『第一对错误关系』中的第二个节点, 并将其赋值给 err2Node
            //# 但是当遍历到了『第二对错误关系』时, 此时 err1Node 不为空, 只会运行第二个 if, 代码可以找到被交换的另一个节点就是『第二对错误关系』中的第二个数, 并将其赋值给 err2Node
            if (prev.val >= node.val && err1Node !== null)
                err2Node = node;
        }

        prev = node;
        //# 右
        /* 
        另一种写法
        if(prev !== null && prev.val >= node.val) {
			if(!err1Node) {
				err1Node = prev;
				err2Node = node;
			}
			else {
				err2Node = node;
			}
		}
        https://leetcode.cn/problems/recover-binary-search-tree/solution/jian-dan-de-zhong-xu-bian-li-o1-kong-jia-8wd0/
        */

        helper(node.right);
    }

    helper(root);
    const temp = err1Node.val;
    err1Node.val = err2Node.val;
    err2Node.val = temp;
};
