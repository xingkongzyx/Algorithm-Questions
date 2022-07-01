/* 
* 1. 确定递归函数参数以及返回值
* 函数作用：将 val 插入「二叉搜索树」中应在的位置
* 输入：「二叉搜索树」的根节点 root 和要插入的值 val
* 输出：在「以 root 为根节点的子树」完成插入操作后的子树根节点的引用
# 可以利用返回值完成新加入的节点与其父节点的赋值操作。

* 2. 确定终止条件
* 终止条件就是遍历到节点为 null 的时候，说明找到了插入的位置，将插入的节点返回。
# 这里把添加的节点返回给上一层，就完成了父子节点的赋值操作了

* 3. 确定单层递归的逻辑
* 搜索树是有方向的，可以根据插入元素的数值，决定递归方向。
*/

var insertIntoBST = function (root, val) {
    //# 既是递归终止条件，也可以理解为前序遍历中对当前节点的操作
    if (root === null) {
        return new TreeNode(val);
    }
    //# 左
    if (root.val > val) {
        root.left = insertIntoBST(root.left, val);
    }

    //# 右
    if (root.val < val) {
        root.right = insertIntoBST(root.right, val);
    }

    return root;
};
