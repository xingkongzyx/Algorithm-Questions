/* 
* 递归法使用中序遍历将二叉搜索树转化为有序序列的时间复杂度为 O(n)，有序序列构造平衡二叉树时每个元素都要访问到，且构造单个节点的时间复杂度为 O(1)，即有序序列构造平衡二叉树的时间复杂度也为 O(n)，所以最终的时间复杂度为 O(n)。

? https://leetcode.cn/problems/balance-a-binary-search-tree/solutions/2101516/acm-xuan-shou-tu-jie-leetcode-jiang-er-c-25y3/
*/
var balanceBST = function (root) {
    const arr = [];

    function convertToArr(node) {
        if (node === null) return;
        convertToArr(node.left);
        arr.push(node.val);
        convertToArr(node.right);
    }

    convertToArr(root);

    function buildTree(left, right) {
        if (left > right) return null;

        let midPos = Math.floor((left + right) / 2);
        let midNode = new TreeNode(arr[midPos]);

        midNode.left = buildTree(left, midPos - 1);
        midNode.right = buildTree(midPos + 1, right);

        return midNode;
    }

    return buildTree(0, arr.length - 1);
};
