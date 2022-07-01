var findMode = function (root) {
    let inOrderTraversalResult = {};

    //* 在中序遍历的过程中将各个 node.val 的出现次数记录在哈希表中
    let inOrderTraversal = function (node) {
        if (node === null) return;

        inOrderTraversal(node.left);
        if (node.val in inOrderTraversalResult)
            inOrderTraversalResult[node.val]++;
        else inOrderTraversalResult[node.val] = 1;
        inOrderTraversal(node.right);
    };
    inOrderTraversal(root);

    let result = [];
    let times = 0;

    //* 遍历一遍哈希表找到「最大的出现次数」
    for (let key in inOrderTraversalResult) {
        if (inOrderTraversalResult[key] > times) {
            times = inOrderTraversalResult[key];
        }
    }

    //* 根据上面找到的「最大的出现次数」找寻其对应的字符，无论有几个都加入结果数组中，最后返回
    for (let key in inOrderTraversalResult) {
        if (inOrderTraversalResult[key] == times) {
            result.push(key);
        }
    }

    return result;
};
