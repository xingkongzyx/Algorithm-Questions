var countNodes = function (root) {
    //* 注意sum是全局变量，根节点和孩子节点都能共享。孩子节点直接把计数加在 sum 上，而不传回给父亲节点。
    let sum = 0;
    function traverse(node) {
        if (node === null) return;
        //* 当前 node 先把自己算在总的节点数目中，再把任务交给孩子节点，让它们自己去把自己以及孩子的孩子节点们加到 sum 进行计数
        //# 中
        sum += 1;
        //# 左
        traverse(node.left);
        //# 右
        traverse(node.right);
    }
    traverse(root);
    return sum;
};
