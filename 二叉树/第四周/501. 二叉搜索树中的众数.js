//> 因为是BST才能使用如下方法，如果是一般的tree使用上面的方法
//> 中序遍历
var findMode = function (root) {
    let prevNode = null;
    let count = 0;
    let result = [];
    let maxCount = 0;
    function inOrderTraverse(currentNode) {
        //* 终止条件: 遇到空节点停止递归
        if (currentNode === null) return;
        //* 左
        inOrderTraverse(currentNode.left);

        //* 中
        //* 更新计数器, 只有在 prevNode 与 currentNode value 相同的时候 count 才会加1, 其余的情况说明遇到了一个新的值, count 恢复成1
        if (prevNode === null) count = 1;
        else if (prevNode.val === currentNode.val) count++;
        else count = 1;

        if (count === maxCount) result.push(currentNode.val);
        else if (count > maxCount) {
            //# 最妙的一点, 当目前的count比存储的最大的maxCount大的时候，直接清零 result 数组，并将新的出现次数最多的元素加入这个初始化的结果数组
            maxCount = count;
            result = [currentNode.val];
        }
        prevNode = currentNode;

        //* 右
        inOrderTraverse(currentNode.right);
    }

    inOrderTraverse(root);
    return result;
};
