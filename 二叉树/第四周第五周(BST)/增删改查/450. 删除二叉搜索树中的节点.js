/* 
! 前序遍历
? https://leetcode.cn/problems/delete-node-in-a-bst/solution/450-shan-chu-er-cha-sou-suo-shu-zhong-de-jie-dia-6/ 
? 代码随想录 https://programmercarl.com/0450.%E5%88%A0%E9%99%A4%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html#%E9%80%92%E5%BD%92
* 函数作用：删除二叉搜索树中的key对应的节点，并保证二叉搜索树的性质不变
* 输入：二叉搜索树的根节点root和要删除的值key
* 输出：删除key后的二叉搜索树的根节点的引用
*/
var deleteNode = function (root, key) {
    if (root === null) return root;

    //# 中
    //* 当前节点等于key，则需要删除当前节点，并保证二叉搜索树的性质不变
    if (root.val === key) {
        if (root.left === null && root.right === null) return null;
        else if (root.left === null && root.right !== null)
            return root.right;
        else if (root.left !== null && root.right === null)
            return root.left;
        else {
            /* 
            # 下面代码的含义是 将待删除节点的左子树放到待删除节点的右子树的最下面的左叶子节点的左子树上
            在右子树中找到最左（最小）节点 minNode；
            把整棵左子树挂到 minNode.left（因为左子树所有值 < 根 < 右子树最小值，BST 仍然成立）；
            返回 root.right，也就是把“整棵右子树”提升为新的根；原来的 root 节点自然被丢弃（由上层接住返回值完成替换）。

            删除前：            删除后（提升右子树）
            root(k)                  root.right R
            /     \                     /    \
        L(<k)    R(>k)        ...   (min)   ...
                    /
                (min)               (min).left = L
            
            ! minNode 是右子树最左节点，一定没有左孩子，因此把 minNode.left = root.left 是安全的；
            */
            let temp = root.right;
            while (temp.left !== null) {
                temp = temp.left;
            }
            temp.left = root.left;
            return root.right;
        }
    }
    //# 左
    //* 当前节点值比key小, 则需要删除当前节点的左子树中 key 对应的节点, 并保证二叉搜索树的性质不变, 然后返回删除 key 后当前节点的左子树的引用
    if (root.val > key) root.left = deleteNode(root.left, key);

    //# 右
    //* 当前节点值比key大, 则需要删除当前节点的右子树中 key 对应的节点, 并保证二叉搜索树的性质不变, 然后返回删除 key 后当前节点的右子树的引用
    if (root.val < key) root.right = deleteNode(root.right, key);

    return root;
};
