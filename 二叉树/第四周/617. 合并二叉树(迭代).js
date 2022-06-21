/* 


> 迭代法中，一般一起操作两个树都是使用队列模拟类似层序遍历，同时处理两个树的节点

* 这里是把第2棵树合并到第1棵树上，
* 
* 1，如果树1的左子节点为空，直接把第2棵树的左子节点赋给第1棵树的左子节点即可
* 2，如果树1的左子节点不为空，树2的左子节点为空，保留树1的左子节点即可，说明这个左子节点及其之后的节点全部采用树1的
* 3，如果树1的左子节点和树2的左子节点都不为空，将其一起加入队列等候处理
*/

var mergeTrees = function (root1, root2) {
    let queue = [];
    if (root1 === null) return root2;
    if (root2 === null) return root1;

    queue.push([root1, root2]);

    while (queue.length > 0) {
        let [node1, node2] = queue.pop();

        let newNodeVal = node1.val + node2.val;
        node1.val = newNodeVal;

        //* 只要两颗树的左节点都不为 null，就把将他们放入队列中；
        if (node1.left !== null && node2.left !== null) {
            queue.push([node1.left, node2.left]);
        }
        //* 同理只要两棵树的右节点都不为 null 了，也将他们放入队列中。
        if (node1.right !== null && node2.right !== null) {
            queue.push([node1.right, node2.right]);
        }

        //* 如果出现 树 1 的 left 节点为 null，树 2 的 left 不为 null，直接将树 2 的 left 赋给树 1 就可以了；
        if (node1.left === null && node2.left !== null) {
            node1.left = node2.left;
        }
        //* 同理如果树 1 的 right 节点为 null，树 2 的不为 null，将树 2 的 right 节点赋给树 1。
        if (node1.right === null && node2.right !== null) {
            node1.right = node2.right;
        }
    }

    return root1;
};
