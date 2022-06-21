// # 与100.一样，本题遍历只能是“后序遍历”，因为我们要通过递归函数的返回值来判断两个树的左侧节点和右侧节点是否各自相等，只有他们全部相等才能说明两树完全相同

var isSameTree = function (p, q) {
    if (p === null && q !== null) return false;
    else if (p !== null && q === null) return false;
    else if (p === null && q === null) return true;
    else if (p.val !== q.val) return false;
    else {
        let leftCheck = isSameTree(p.left, q.left); //* 左
        let rightCheck = isSameTree(p.right, q.right); //* 右
        return leftCheck && rightCheck; //* 中
    }
};
