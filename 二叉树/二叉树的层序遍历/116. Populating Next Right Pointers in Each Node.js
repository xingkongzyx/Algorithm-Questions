/* 
! 本题依然是层序遍历, 只不过在单层遍历的时候记录一下本层的头部节点, 然后在遍历的时候让前一个节点指向本节点就可以了
? https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html
/ Time Complexity : O(N), where N is the number of nodes in the given tree. We only traverse the tree once using BFS which requires O(N).
/ Space Complexity : O(W) = O(N), where W is the width of given tree. This is required to store the nodes in queue. Since the given tree is a perfect binary tree, its width is given as W = (N+1)/2 ≈ O(N)
*/

var connect = function (root) {
    let queue = [];
    if (root !== null) queue.push(root);

    while (queue.length > 0) {
        let size = queue.length;
        //* 使用 preNode 从而使得其 next属性指向下一个同 level 的 node
        let preNode;
        for (let i = 0; i < size; i++) {
            let poppedNode = queue.shift();
            //* i 为 0 时给 preNode 初始化值。
            if (i === 0) {
                preNode = poppedNode;
            } else {
                //* i不为0时, 也就是从同 level 的第二个节点开始, 我们让上面 "i=0" 时的第一个节点的 next 属性指向这个节点, 然后更新 preNode
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
