//? 递归函数有返回值
/* 
* 1. 确定递归函数参数以及返回值
* 参数就是根节点指针，以及要插入元素，递归函数的返回类型为节点。
# 可以利用返回值完成新加入的节点与其父节点的赋值操作。

* 2. 确定终止条件
* 终止条件就是找到遍历的节点为null的时候，就是要插入节点的位置了，并把插入的节点返回。
# 这里把添加的节点返回给上一层，就完成了父子节点的赋值操作了

* 3. 确定单层递归的逻辑
* 搜索树是有方向的，可以根据插入元素的数值，决定递归方向。
*/

var insertIntoBST = function (root, val) {
    if (root === null) {
        return new TreeNode(val);
    }

    //> 大家应该能感受到，如何通过递归函数返回值完成了新加入节点的父子关系赋值操作了，下一层将加入节点返回，本层用root->left或者root->right将其接住。
    if (root.val > val) {
        root.left = insertIntoBST(root.left, val);
    }

    if (root.val < val) {
        root.right = insertIntoBST(root.right, val);
    }

    return root;
};

//? 递归函数没有返回值
// * 没有返回值，需要记录上一个节点 (prevNode)，遇到空节点了，就让 prevNode 左孩子或者右孩子指向新插入的节点。然后结束递归。
var insertIntoBST = function (root, val) {
    if (root === null) return new TreeNode(val);

    let prevNode = null;
    let preOrderTraverse = function (currentNode, val) {
        if (currentNode === null) {
            if (prevNode.val > val) prevNode.left = new TreeNode(val);
            else prevNode.right = new TreeNode(val);
            return;
        }
        prevNode = currentNode;
        if (currentNode.val > val) {
            preOrderTraverse(currentNode.left, val);
        }

        if (currentNode.val < val) {
            preOrderTraverse(currentNode.right, val);
        }

        return;
    };

    preOrderTraverse(root, val);
    return root;
};
