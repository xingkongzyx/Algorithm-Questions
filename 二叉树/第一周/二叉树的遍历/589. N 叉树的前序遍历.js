var preorder = function (root) {
    let res = [];
    traverseHelper(root, res);
    return res;
};
function traverseHelper(node, res) {
    if (node === null) return;
    res.push(node.val);
    for (let i = 0; i < node.children.length; i++) {
        traverseHelper(node.children[i], res);
    }
}
