/* 
! 前序遍历
* 从根节点递归到叶子节点，计算这一条路径上的深度，并更新维护最大深度。
* 这个是正儿八经的求深度。每次先维护根节点的深度，再递归左子树、右子树。
*/
var maxDepth = function (root) {
    let depth = 0;
    let res = 0;
    let traverse = (root) => {
        if (root == null) {
            //* 到了最底部我们要更新深度
            res = Math.max(res, depth);
            return;
        }
        /// 中
        depth++;
        /// 左
        traverse(root.left);
        /// 右
        traverse(root.right);
        /// 在返回上一级的时候确保depth回到正确的深度
        ///         1
        ///        / \
        ///       2   3
        /// 在遍历到2的时候depth通过加一变为2(中)，然后遍历2的左右subtree(左右)。此时完成对2的前序遍历。然后返回上一层，depth应该变为1，再递归遍历1的右子树，而不能以depth=2继续遍历1的右子树，我们的depth只有在遍历到3的时候才能进行加1的操作。
        depth--;
    };
    traverse(root);
    return res;
};
