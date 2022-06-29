/* 
! 本题依然是层序遍历，只不过在单层遍历的时候记录一下本层的头部节点，然后在遍历的时候让前一个节点指向本节点就可以了

*/

var connect = function (root) {
    let queue = [];
    if (root !== null) queue.push(root);

    while (queue.length > 0) {
        let size = queue.length;
        //* 使用 preNode 从而使得其next属性指向下一个同level的node
        let preNode;
        for (let i = 0; i < size; i++) {
            let poppedNode = queue.shift();
            //* i 为 0 时给 preNode初始化值。
            if (i === 0) {
                preNode = poppedNode;
            } else {
                //* i不为0时，也就是从同level的第二个节点开始，我们让上面i=0时的第一个节点的next属性指向这个节点，然后更新preNode
                preNode.next = poppedNode;
                preNode = preNode.next;
            }
            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);
        }
        preNode.next = null;
    }
    return root;
};
