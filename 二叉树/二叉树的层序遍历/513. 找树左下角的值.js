//? 链接：https://leetcode.cn/problems/find-bottom-left-tree-value/solution/javascript-bfs-dfsqian-xu-by-yi-xiao-i-nc2z/
var findBottomLeftValue = function (root) {
    if (!root) return null;
    const queue = [root];
    let mostLeft = null;
    while (queue.length > 0) {
        let curLevelSize = queue.length;
        //因为是层序遍历，所以每次层的queue的第一个必然是最左边的节点
        mostLeft = queue[0];
        for (let i = 0; i < curLevelSize; i++) {
            const curNode = queue.shift();

            curNode.left && queue.push(curNode.left);
            curNode.right && queue.push(curNode.right);
        }
    }

    return mostLeft.val;
};
