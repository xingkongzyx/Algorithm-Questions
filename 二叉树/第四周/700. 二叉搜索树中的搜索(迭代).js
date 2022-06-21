/* 
* 因为二叉搜索树的特殊性，也就是节点的有序性，可以不使用辅助栈或者队列就可以写出迭代法。
* 对于一般二叉树，递归过程中还有回溯的过程，例如走一个左方向的分支走到头了，那么要调头，在走右分支。
> 对于二叉搜索树，不需要回溯的过程，因为节点的有序性就帮我们确定了搜索的方向。


*/


var searchBST = function (root, val) {
    while (root !== null) {
        if (root.val === val) return root;
        else if (root.val < val) root = root.right;
        else if (root.val > val) root = root.left;
    }
    return null;
};
