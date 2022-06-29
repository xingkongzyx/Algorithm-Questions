var levelOrder = function (root) {
    if (root === null) return [];
    let queue = [root];
    const result = [];

    while (queue.length > 0) {
        //! 唯一注意的是要把每一层放到一起，需要维护一个 currentLevelNodesNum 保存每一层的元素个数。
        const currentLevelNodesNum = queue.length;
        const currentLevelNodes = [];
        //* 处理当前层的元素，每个元素出队前将其左右子节点入队，作为下一层的元素
        for (let i = 0; i < currentLevelNodesNum; i++) {
            const poppedNode = queue.shift();
            currentLevelNodes.push(poppedNode.val);
            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);
        }
        result.push(currentLevelNodes);
    }
    return result;
};
