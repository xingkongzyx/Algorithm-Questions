/* 
* 1. 确定递归函数参数以及返回值
* 说道递归函数的返回值，在二叉树：搜索树中的插入操作 (opens new window)中通过递归返回值来加入新节点， 这里也可以通过递归返回值删除节点。
 
* 2. 确定终止条件
* 遇到空返回，其实这也说明没找到删除的节点，遍历到空节点直接返回了

* 3. 确定单层递归的逻辑
* 如果 (root.val > key) 则递归左子树删除节点
* 如果 (root.val < key) 则递归右子树删除节点
* 如果当前节点就是要删除的节点，有四种情况: 
* 1. 第一种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
* 2. 第二种情况：删除节点的左孩子为空，右孩子不为空，删除节点，右孩子补位，返回右孩子为根节点
* 3. 第三种情况：删除节点的右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
* 3. 第四种情况：左右孩子节点都不为空，则将删除节点的左子树头结点（左孩子）放到删除节点的右子树的最左面节点的左孩子上，返回删除节点右孩子为新的根节点。
*/
var deleteNode = function (root, key) {
    if (root === null) return root;

    if (root.val > key) root.left = deleteNode(root.left, key);
    else if (root.val < key) root.right = deleteNode(root.right, key);
    // # 这里相当于把新的节点返回给上一层，上一层就要用 root.left 或者 root.right接住
    else {
        if (root.left === null && root.right !== null)
            return root.right;
        else if (root.left !== null && root.right === null)
            return root.left;
        else if (root.left === null && root.right === null)
            return null;
        else {
            let temp = root.right;
            while (temp.left !== null) {
                temp = temp.left;
            }
            temp.left = root.left;
            return root.right;
        }
    }
    return root;
};
