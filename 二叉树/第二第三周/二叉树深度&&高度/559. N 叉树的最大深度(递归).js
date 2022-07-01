/* 
! 用后序遍历（左右中）来计算树的高度。
* 1. 确定递归函数的参数和返回值：参数就是传入树的根节点，返回就返回这棵树的深度，所以返回值为int类型。
* 2. 确定终止条件：如果为空节点的话，就返回0，表示高度为0。
* 3. 确定单层递归的逻辑：依次求所有子树的深度，并且取其所有子树深度的最大数值 再+1 （加1是因为算上当前中间节点）就是目前节点为根节点的树的深度。 
*/

var maxDepth = function (root) {
    if (root === null) return 0;
    let depth = 0;
    for (let i = 0; i < root.children.length; i++) {
        depth = Math.max(maxDepth(root.children[i]), depth);
    }
    return 1 + depth;
};
