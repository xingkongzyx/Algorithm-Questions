var postorder = function (root) {
    let res = [];
    traverseHelper(root, res);
    return res;
};

function traverseHelper(node, res) {
    if (node === null) return null;

    for (let i = 0; i < node.children.length; i++)
        traverseHelper(node.children[i], res);

    res.push(node.val);
}
