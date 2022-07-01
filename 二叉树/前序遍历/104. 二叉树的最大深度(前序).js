//* 相比于代码随想录的讲解这个是更加普遍的求深度的解法
var maxDepth = function (root) {
    let depth = 0;
    let res = 0;
    let traverse = (root) => {
        if (root == null) return;
        //# 中
        depth++;
        //* 遍历的过程中记录最大深度
        res = Math.max(res, depth);
        //# 左
        traverse(root.left);
        //# 右
        traverse(root.right);
        //# 回溯
        depth--;
    };
    traverse(root);
    return res;
};
