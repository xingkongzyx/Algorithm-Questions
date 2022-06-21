var rob = function (root) {
    if (root === null) return 0;
    if (root.left === null && root.right === null) return root.val;

    // 偷当前节点
    let val1 = root.val;
    if (root.left) val1 += rob(root.left.left) + rob(root.left.right);
    if (root.right)
        val1 += rob(root.right.left) + rob(root.right.right);
    // 不偷当前节点
    let val2 = 0;
    val2 += rob(root.left);
    val2 += rob(root.right);

    return Math.max(val1, val2);
};

var rob_optimize = function (root) {
    let map = new Map();
    function recursion(root) {
        if (root === null) return 0;
        if (map.has(root)) return map.get(root);
        if (root.left === null && root.right === null)
            return root.val;

        // 偷当前节点
        let val1 = root.val;
        if (root.left)
            val1 +=
                recursion(root.left.left) +
                recursion(root.left.right);
        if (root.right)
            val1 +=
                recursion(root.right.left) +
                recursion(root.right.right);
        // 不偷当前节点
        let val2 = recursion(root.left) + recursion(root.right);

        map.set(root, Math.max(val1, val2));
        return map.get(root);
    }
    return recursion(root);
};
