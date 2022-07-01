//? 本题与主站 285 题相同
//? https://leetcode.cn/problems/P5rCT8/

var inorderSuccessor = function (root, p) {
    const visited = [];
    function traverse(node) {
        if (node === null) return;
        traverse(node.left);
        visited.push(node);
        traverse(node.right);
    }

    traverse(root);
    for (let i = 1; i < visited.length; i++) {
        if (visited[i - 1] === p) return visited[i];
    }

    return null;
};
