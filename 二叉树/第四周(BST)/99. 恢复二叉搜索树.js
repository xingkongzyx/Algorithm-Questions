/*
? https://leetcode.cn/problems/recover-binary-search-tree/solution/tu-jie-hui-fu-yi-ge-er-cha-sou-suo-shu-by-hyj8/
题目解读：
首先，题目告诉我们是在一个有序的二叉搜索树中有两个节点被交换了，那么存在两种交换情况：

相邻节点交换；
不相邻节点交换。
第1种情况下，只有一对前后关系是错误的，第2种情况下，有两对前后关系是错误的，其中第一对错误的关系中，一定是前面那个数错了，第二对错误关系中，一定是后面那个数错了。（大数换到前面，肯定是比其后面的数大导致关系错，小数换到后面肯定是比它前面的数小导致关系错误。）

 */
var recoverTree = function (root) {
    let err1 = null;
    let err2 = null;
    let prev = null;
    function helper(node) {
        if (node === null) return;
        //# 左
        helper(node.left);

        //# 中
        if (prev && prev.val >= node.val && err1 === null)
            err1 = prev;
        if (prev && prev.val >= node.val && err1 !== null)
            err2 = node;
        prev = node;
        //# 右
        /* 
        另一种写法
        if(prev !== null && prev.val >= node.val) {
			if(!err1) {
				err1 = prev;
				err2 = node;
			}
			else {
				err2 = node;
			}
		}
        https://leetcode.cn/problems/recover-binary-search-tree/solution/jian-dan-de-zhong-xu-bian-li-o1-kong-jia-8wd0/
        */

        helper(node.right);
    }

    helper(root);
    const temp = err1.val;
    err1.val = err2.val;
    err2.val = temp;
};
