const lowestCommonAncestor = function (root, p, q) {
    if (root === null) return null;
    if (root === p || root === q) return root;

    let left = lowestCommonAncestor(root.left, p, q);
    let right = lowestCommonAncestor(root.right, p, q);

    if (!left && !right) return null;
    else if (left !== null && right !== null) return root;
    else if (left !== null && right === null) return left;
    else return right;
};
