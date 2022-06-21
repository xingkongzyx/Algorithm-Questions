//* dp数组（dp table）以及下标的含义：下标为0记录不偷该节点所得到的的最大金钱，下标为1记录偷该节点所得到的的最大金钱。
//? leetcode.cn/problems/house-robber-iii/solution/shu-xing-dp-ru-men-wen-ti-by-liweiwei1419/
var rob = function (root) {
    function robTreeDP(node) {
        if (node === null) return [0, 0];
        /// 树的后序遍历
        //* 左
        let leftSubtreeResult = robTreeDP(node.left);
        //* 右
        let rightSubtreeResult = robTreeDP(node.right);

        //* 中
        //# val1: 以当前 node 为根结点的子树能够偷取的最大价值，规定 node 结点偷. 如果是偷当前节点，那么左右孩子就不能偷
        let val1 =
            node.val + leftSubtreeResult[0] + rightSubtreeResult[0];

        //# val2: 以当前 node 为根结点的子树能够偷取的最大价值，规定 node 结点不偷. 如果不偷当前节点，那么左右孩子就可以考虑偷，偷与不偷通过对比储存在数组中偷和不偷两种情况哪个值更大得出
        let val2 =
            Math.max(leftSubtreeResult[0], leftSubtreeResult[1]) +
            Math.max(rightSubtreeResult[0], rightSubtreeResult[1]);

        return [val1, val2];
    }

    let [RobCurrentNode, NotRobCurrentNode] = robTreeDP(root);

    return Math.max(NotRobCurrentNode, RobCurrentNode);
};
