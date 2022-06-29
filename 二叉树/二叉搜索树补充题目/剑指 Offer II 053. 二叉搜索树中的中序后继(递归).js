var inorderSuccessor = function (root, p) {
    //* 中序遍历记录前一节点pre，若前一节点与p引用相同，则当前节点node就是p的中序后继，记为res即最终返回结果。
    let prevNode = null;
    function traverse(node) {
        if (node === null) return null;

        let leftRes = traverse(node.left);
        if (leftRes != null) return leftRes;

        if (prevNode != null && prevNode == p) {
            return node;
        }
        prevNode = node;

        let rightRes = traverse(node.right);
        if (rightRes != null) return rightRes;
    }

    let result = traverse(root);
    return result;
};
