// ! 前序遍历「」
// * 一个节点为「左叶子」节点，当且仅当它是某个节点的「左子节点」，并且它是一个「叶子结点」。因此我们可以考虑对整棵树进行遍历，当我们遍历到节点 node 时，如果它的左子节点是一个叶子结点，那么就将它的左子节点的值累加计入答案。
// ? https://leetcode.cn/problems/sum-of-left-leaves/solution/javadi-gui-yu-die-dai-shi-xian-si-lu-by-ggb2312/

var sumOfLeftLeaves = function (root) {
    let queue = [];
    let sum = 0;
    if (root !== null) queue.push(root);
    while (queue.length > 0) {
        let poppedNode = queue.shift();
        //# 访问当前Node(中)
        if (
            poppedNode.left !== null &&
            poppedNode.left.left === null &&
            poppedNode.left.right === null
        )
            sum += poppedNode.left.val;
        //# 处理左边node(左)
        if (poppedNode.right !== null) queue.push(poppedNode.right);
        //# 处理右边node(右)
        if (poppedNode.left !== null) queue.push(poppedNode.left);
    }

    return sum;
};
