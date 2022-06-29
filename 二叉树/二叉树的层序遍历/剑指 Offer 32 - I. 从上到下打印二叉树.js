//? 层序遍历的动画讲解 https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/solution/mian-shi-ti-32-i-cong-shang-dao-xia-da-yin-er-ch-4/

var levelOrder = function (root) {
    if (root === null) return [];
    let queue = [root];
    const result = [];

    while (queue.length > 0) {
        const poppedNode = queue.shift();
        result.push(poppedNode.val);
        if (poppedNode.left) queue.push(poppedNode.left);
        if (poppedNode.right) queue.push(poppedNode.right);
    }
    return result;
};
