/* 
https://leetcode.cn/problems/count-good-nodes-in-binary-tree/solutions/2272022/dfs-shen-du-you-xian-sou-suo-bfs-yan-du-jplgf/?envType=study-plan-v2&envId=leetcode-75
*/
var goodNodes = function (root, maxVal = -Infinity) {
    if (root === null) {
        return 0;
    }

    let leftRes = goodNodes(root.left, Math.max(maxVal, root.val));
    let rightRes = goodNodes(root.right, Math.max(maxVal, root.val));

    return leftRes + rightRes + (root.val >= maxVal ? 1 : 0);
};
